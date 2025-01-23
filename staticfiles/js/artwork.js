document.addEventListener("DOMContentLoaded", function () {
  const carousel = document.querySelector("#artworkCarousel");
  const items = carousel.querySelectorAll(".carousel-item");
  const prevButton = carousel.querySelector(".carousel-control-prev");
  const nextButton = carousel.querySelector(".carousel-control-next");

  if (items.length <= 1) {
    // Disable auto-slide
    carousel.removeAttribute("data-bs-ride");
    carousel.classList.remove("slide");

    // Hide navigation buttons
    prevButton.style.display = "none";
    nextButton.style.display = "none";
  }
});
