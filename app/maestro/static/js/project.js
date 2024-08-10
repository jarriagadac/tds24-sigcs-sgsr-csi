const el = document.getElementById("wrapper");
const toggleButton = document.getElementById("menu-toggle");

if (toggleButton) {
  toggleButton.onclick = function () {
    el.classList.toggle("toggled");
    toggleButton.innerHTML =
      toggleButton.innerHTML === "close" ? "menu" : "close";
  };
}
