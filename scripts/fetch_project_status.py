"""Fetch initiative status from GitHub Projects v2 and update docs/status.md.

The script looks for a placeholder block in the existing status.md:

    <!-- DEVICE_STATUS_TABLE_START -->
    ... (replaced by the script) ...
    <!-- DEVICE_STATUS_TABLE_END -->

Only the content between the markers is replaced. Everything else in the
file is left untouched, so hand-written sections are preserved.
"""

import json
import os
import re
import urllib.request
import urllib.error

GRAPHQL_URL = "https://api.github.com/graphql"
ORG = "openaudiotools"
PROJECT_NUMBER = 2
FIELD_NAME = "Innitiative Status"
STATUS_FIELD_NAME = "Phase"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "docs", "status.md")
DEVICES_PATH = os.path.join(os.path.dirname(__file__), "..", "docs", "devices", "index.md")

TABLE_START = "<!-- DEVICE_STATUS_TABLE_START -->"
TABLE_END = "<!-- DEVICE_STATUS_TABLE_END -->"

FALLBACK_TABLE = """\
!!! warning "Live data unavailable"

    Could not fetch project data from GitHub. Visit the
    [Project Board](https://github.com/orgs/openaudiotools/projects/2)
    to see current device status."""

# Devices with dedicated repos (org-level)
REPO_DEVICES = {"syntee", "mixtee", "despee"}
# Concept devices with local spec files
CONCEPT_DEVICES = {
    "voicee": "devices/voicee.md",
    "stringee": "devices/stringee.md",
    "hubtee": "devices/hubtee.md",
}

QUERY = """
query {
  organization(login: "%s") {
    projectV2(number: %d) {
      title
      fields(first: 20) {
        nodes {
          ... on ProjectV2SingleSelectField {
            name
            options { id name description }
          }
        }
      }
      items(first: 100) {
        nodes {
          content {
            ... on Issue { title url state repository { name } }
            ... on DraftIssue { title }
            ... on PullRequest { title url state repository { name } }
          }
          fieldValues(first: 20) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue {
                name
                field { ... on ProjectV2SingleSelectField { name } }
              }
              ... on ProjectV2ItemFieldTextValue {
                text
                field { ... on ProjectV2Field { name } }
              }
            }
          }
        }
      }
    }
  }
}
""" % (ORG, PROJECT_NUMBER)

def replace_table_block(content: str, table: str) -> str:
    """Replace the content between TABLE_START and TABLE_END markers."""
    pattern = re.compile(
        re.escape(TABLE_START) + r".*?" + re.escape(TABLE_END),
        re.DOTALL,
    )
    replacement = f"{TABLE_START}\n{table}\n{TABLE_END}"
    new_content, count = pattern.subn(replacement, content)
    if count == 0:
        raise ValueError(
            f"Placeholder {TABLE_START} ... {TABLE_END} not found in {OUTPUT_PATH}"
        )
    return new_content


def write_output(table: str) -> None:
    if not os.path.exists(OUTPUT_PATH):
        raise FileNotFoundError(
            f"{OUTPUT_PATH} does not exist. Create it with the placeholder markers first."
        )
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    content = replace_table_block(content, table)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def fetch_project_data(token: str) -> dict:
    payload = json.dumps({"query": QUERY}).encode()
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def get_field_value(field_values_nodes: list, field_name: str) -> str:
    for node in field_values_nodes:
        field = node.get("field")
        if not field:
            continue
        if field.get("name", "") == field_name:
            return node.get("name") or node.get("text") or ""
    return ""


def get_phases(fields_nodes: list) -> list[dict]:
    """Extract phase options from the project fields definition."""
    for node in fields_nodes:
        if node.get("name") == FIELD_NAME and "options" in node:
            return node["options"]
    return []


def device_link(title: str) -> str:
    """Return a markdown link to the device repo or concept file."""
    key = title.lower().replace(" ", "")
    if key in REPO_DEVICES:
        return f"[repo](https://github.com/openaudiotools/{key})"
    if key in CONCEPT_DEVICES:
        return f"[concept]({CONCEPT_DEVICES[key]})"
    return ""


def build_table(items: list[dict]) -> str:
    """Build just the devices table (without page chrome)."""
    if not items:
        return '!!! note\n\n    No items found in the project board.'

    lines = []
    lines.append("| Device | Phase | Link |")
    lines.append("|--------|--------|------|")
    for item in items:
        status = item["initiative_status"] or item["status"] or ""
        if item["url"] and status:
            status_cell = f"[{status}]({item['url']})"
        elif item["url"]:
            status_cell = f"[link]({item['url']})"
        else:
            status_cell = status
        link_cell = device_link(item["title"])
        lines.append(f"| {item['title']} | {status_cell} | {link_cell} |")
    return "\n".join(lines)


def collect_items(project: dict) -> list[dict]:
    """Extract item dicts from project data."""
    items_nodes = (project.get("items") or {}).get("nodes", [])
    items = []
    for item in items_nodes:
        content = item.get("content")
        if not content:
            continue
        fv_nodes = (item.get("fieldValues") or {}).get("nodes", [])
        items.append({
            "title": content.get("title", ""),
            "url": content.get("url", ""),
            "repo": (content.get("repository") or {}).get("name", ""),
            "initiative_status": get_field_value(fv_nodes, FIELD_NAME),
            "status": get_field_value(fv_nodes, STATUS_FIELD_NAME),
        })
    return items


def update_devices_page(items: list[dict]) -> None:
    """Replace **Status:** lines in the devices index with live initiative status."""
    if not os.path.exists(DEVICES_PATH):
        print(f"Devices page not found at {DEVICES_PATH} — skipping update.")
        return

    # Build a lookup: lowercase device name -> initiative_status
    status_map: dict[str, str] = {}
    for item in items:
        if item["initiative_status"]:
            status_map[item["title"].lower()] = item["initiative_status"]

    if not status_map:
        return

    with open(DEVICES_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    current_heading = ""
    lines = content.split("\n")
    changed = False
    for i, line in enumerate(lines):
        # Track current ## heading
        heading_match = re.match(r"^## (.+)$", line)
        if heading_match:
            current_heading = heading_match.group(1).strip().lower()
            continue
        # Replace **Status:** line if we have data for this device
        if current_heading and line.startswith("**Status:**"):
            new_status = status_map.get(current_heading)
            if new_status and line != f"**Status:** {new_status}":
                lines[i] = f"**Status:** {new_status}"
                changed = True

    if changed:
        with open(DEVICES_PATH, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Updated device statuses in {DEVICES_PATH}")


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        print("No GITHUB_TOKEN set — writing fallback table.")
        write_output(FALLBACK_TABLE)
        return

    try:
        data = fetch_project_data(token)
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        print(f"GitHub API error: {exc} — writing fallback table.")
        write_output(FALLBACK_TABLE)
        return

    errors = data.get("errors")
    if errors:
        print(f"GraphQL errors: {errors} — writing fallback table.")
        write_output(FALLBACK_TABLE)
        return

    project = (data.get("data") or {}).get("organization", {}).get("projectV2")
    if not project:
        print("Project not found — writing fallback table.")
        write_output(FALLBACK_TABLE)
        return

    items = collect_items(project)
    table = build_table(items)
    write_output(table)
    update_devices_page(items)
    print(f"Updated {len(items)} items in {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
