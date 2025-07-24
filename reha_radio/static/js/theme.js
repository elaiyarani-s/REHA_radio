
document.addEventListener("DOMContentLoaded", function () {
  const themeToggle = document.getElementById("themeToggle");
  const html = document.documentElement;

  function setTheme(mode) {
    html.setAttribute("data-bs-theme", mode);
    localStorage.setItem("theme", mode);
  }

  const savedTheme = localStorage.getItem("theme");
  if (savedTheme) {
    setTheme(savedTheme);
  }

  themeToggle.addEventListener("click", () => {
    const current = html.getAttribute("data-bs-theme");
    const next = current === "light" ? "dark" : "light";
    setTheme(next);
  });
});
