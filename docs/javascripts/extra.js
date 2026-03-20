// Open external nav links in a new tab
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".md-nav a[href^='http']").forEach(function (link) {
    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener");
  });
});
