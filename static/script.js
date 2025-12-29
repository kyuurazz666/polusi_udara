// Update nilai slider secara real-time
const sliders = document.querySelectorAll(".slider");

sliders.forEach(slider => {
  const valueSpan = document.getElementById(slider.dataset.value);

  valueSpan.innerText = slider.value;

  slider.addEventListener("input", () => {
    valueSpan.innerText = slider.value;
  });
});

// Efek futuristik tombol
const btn = document.getElementById("simulateBtn");
btn.addEventListener("mouseenter", () => {
  btn.style.boxShadow = "0 0 20px cyan";
});
btn.addEventListener("mouseleave", () => {
  btn.style.boxShadow = "none";
});
