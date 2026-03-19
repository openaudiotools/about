"""Fetch initiative status from GitHub Projects v2 and generate docs/status.md."""

import json
import os
import re
import urllib.request
import urllib.error

GRAPHQL_URL = "https://api.github.com/graphql"
ORG = "openaudiotools"
PROJECT_NUMBER = 2
FIELD_NAME = "Innitiative Status"
STATUS_FIELD_NAME = "Status"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "docs", "status.md")
DEVICES_PATH = os.path.join(os.path.dirname(__file__), "..", "docs", "devices", "index.md")

INTRO = """\
# Project Status

Open Audio Tools is a side project — I contribute as much time as I can
but have other priorities. The goal is to reach a working prototype by the
end of 2026.

For the full project board, see
[GitHub Projects](https://github.com/orgs/openaudiotools/projects/2).
"""

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

FALLBACK_PAGE = INTRO + """
!!! warning "Live data unavailable"

    Could not fetch project data from GitHub. Visit the
    [project board](https://github.com/orgs/openaudiotools/projects/2)
    to see current initiative status.
"""


def write_output(content: str) -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
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


def build_page(project: dict, items: list[dict]) -> str:
    fields_nodes = (project.get("fields") or {}).get("nodes", [])
    phases = get_phases(fields_nodes)

    lines = [INTRO]

    # Phases table
    if phases:
        lines.append("## Phases\n")
        lines.append("| Phase | Description |")
        lines.append("|-------|-------------|")
        for phase in phases:
            desc = phase.get("description") or ""
            lines.append(f"| {phase['name']} | {desc} |")
        lines.append("")

    # Group items by initiative_status (phase)
    phase_order = [p["name"] for p in phases] if phases else []
    groups: dict[str, list] = {}
    for item in items:
        key = item["initiative_status"] or "Other"
        groups.setdefault(key, []).append(item)

    # Order: phases in board order, then any extras alphabetically
    ordered_keys = [k for k in phase_order if k in groups]
    extras = sorted(k for k in groups if k not in phase_order)
    ordered_keys.extend(extras)

    if ordered_keys:
        lines.append("## Initiatives\n")
        for key in ordered_keys:
            lines.append(f"### {key}\n")
            lines.append("| Initiative | Repository | Status |")
            lines.append("|------------|------------|--------|")
            for item in groups[key]:
                cell = f"[{item['title']}]({item['url']})" if item["url"] else item["title"]
                lines.append(f"| {cell} | {item['repo']} | {item['status']} |")
            lines.append("")
    elif not items:
        lines.append(
            "!!! note\n\n"
            "    No items found in the project board.\n"
        )

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
        print("No GITHUB_TOKEN set — writing fallback page.")
        write_output(FALLBACK_PAGE)
        return

    try:
        data = fetch_project_data(token)
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        print(f"GitHub API error: {exc} — writing fallback page.")
        write_output(FALLBACK_PAGE)
        return

    errors = data.get("errors")
    if errors:
        print(f"GraphQL errors: {errors} — writing fallback page.")
        write_output(FALLBACK_PAGE)
        return

    project = (data.get("data") or {}).get("organization", {}).get("projectV2")
    if not project:
        print("Project not found — writing fallback page.")
        write_output(FALLBACK_PAGE)
        return

    items = collect_items(project)
    page = build_page(project, items)
    write_output(page)
    update_devices_page(items)
    print(f"Wrote {len(items)} items to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
