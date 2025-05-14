// Handle theme toggle and store in localStorage
const themeToggle = document.getElementById("themeToggle");

function applySavedTheme() {
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme) {
    document.body.className = savedTheme;
  } else {
    document.body.className = "light";
  }
}

themeToggle.addEventListener("click", () => {
  const currentTheme = document.body.classList.contains("light") ? "dark" : "light";
  document.body.className = currentTheme;
  localStorage.setItem("theme", currentTheme);
});

applySavedTheme(); // Set theme on page load

// Animate image on click
const yogaImage = document.getElementById("yogaImage");

yogaImage.addEventListener("click", () => {
  yogaImage.classList.add("animate");

  // Remove the class after animation ends so it can be triggered again
  yogaImage.addEventListener("animationend", () => {
    yogaImage.classList.remove("animate");
  }, { once: true });
});
