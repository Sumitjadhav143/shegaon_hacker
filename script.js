document.addEventListener("DOMContentLoaded", function () {
  const paperCutRainContainer = document.querySelector('.paper-cut-rain');

  if (!paperCutRainContainer) {
      console.error("Error: .paper-cut-rain container not found.");
      return;
  }

  // Function to create a single paper cut
  function createPaperCut() {
      const paperCut = document.createElement('div');
      paperCut.classList.add('paper-cut');

      // Randomize color (vibrant colors)
      const colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff', '#ff8c00', '#8a2be2'];
      const randomColor = colors[Math.floor(Math.random() * colors.length)];
      paperCut.style.backgroundColor = randomColor;

      // Randomize size
      paperCut.style.width = `${Math.random() * 10 + 10}px`;
      paperCut.style.height = `${Math.random() * 40 + 40}px`;

      // Randomize starting position (top of the screen)
      paperCut.style.left = `${Math.random() * 100}vw`;
      paperCut.style.top = `-50px`;

      // Randomize animation duration (falling speed)
      const duration = Math.random() * 2 + 3; // Between 3s and 8s
      paperCut.style.animationDuration = `${duration}s`;

      // Add the paper cut to the container
      paperCutRainContainer.appendChild(paperCut);

      // Remove the paper cut after it falls out of view
      setTimeout(() => {
          paperCut.remove();
      }, duration * 1000);
  }

  // Generate paper cuts continuously
  function generatePaperCutRain() {
      const intervalId = setInterval(createPaperCut, 100);

      // Stop the rain after 30 seconds
      setTimeout(() => {
          clearInterval(intervalId);
      }, 10000);
  }

  // Start the paper cut rain
  generatePaperCutRain();

  // Load Lucide Icons
  if (window.lucide) {
      lucide.createIcons();
  }
});
