const timerDisplay = document.getElementById("timer");
const gameContainer = document.getElementById("game-container");
const restartButton = document.getElementById("restart-button");
const backButton = document.getElementById("back-button");

// Elementi di gioco
const grass = document.getElementById("grass");
const resultDisplay = document.getElementById("result");
const clickCounter = document.getElementById("click-counter");

const finalMusic = new Audio("http://localhost:8080/missione1/final.mp3");

// Audio
const backgroundMusic = new Audio("http://localhost:8080/missione1/music.mp3");
backgroundMusic.currentTime = 3;
backgroundMusic.loop = true;

let musicStarted = false;

function startBackgroundMusic() {
  if (!musicStarted) {
    backgroundMusic.play().catch((error) => {
      console.error("Errore durante la riproduzione della musica:", error);
    });
    musicStarted = true;
  }
}

const audio = new Audio("http://localhost:8080/missione1/grassSound.mp3");
let clicks = 0;
let timeLeft = 60;
let clicksRequired = 10;
let timerInterval = null;

// Avvia il gioco
function startGame() {
  // Resetta l'area di gioco
  grass.style.display = "block";
  moveGrass(); // Posiziona subito l'erba

  gameContainer.style.display = "block";

  // Sposta l'erba ogni 2 secondi
  setInterval(moveGrass, 2000);

  // Avvia il timer
  startTimer();

  // Avvia la musica
  startBackgroundMusic();
}

// Inizia la missione
function startMission() {
  const playerClass = document.getElementById("classe").value;

  const abilities = Array.from(
    document.querySelectorAll('input[name="abilita"]:checked')
  ).map((checkbox) => checkbox.value);

  // Simulazione dei dati ricevuti dal server
  const data = {
    tempo:
      playerClass === "assassino" ? 50 : playerClass === "clerico" ? 70 : 60,
    click_richiesti:
      playerClass === "guerriero" ? 13 : playerClass === "mago" ? 8 : 10,
  };

  timeLeft = data.tempo || 60;
  clicksRequired = data.click_richiesti || 10;

  alert(`Tempo: ${timeLeft}s, Click richiesti: ${clicksRequired}`);

  // Nascondi la barra di selezione
  document.querySelector(".selection-bar").style.display = "none";

  startGame(); // Avvia il gioco
}

// Funzione per spostare la ciocca d'erba casualmente
function moveGrass() {
  const container = document.getElementById("game-container");
  const maxWidth = container.offsetWidth - grass.offsetWidth;
  const maxHeight = container.offsetHeight - grass.offsetHeight;

  const randomX = Math.floor(Math.random() * maxWidth);
  const randomY = Math.floor(Math.random() * maxHeight);

  grass.style.left = `${randomX}px`;
  grass.style.top = `${randomY}px`;
}

// Timer
function startTimer() {
  clearInterval(timerInterval); // Pulisce eventuali timer esistenti
  timerInterval = setInterval(() => {
    timeLeft--;
    timerDisplay.textContent = `Tempo rimasto: ${timeLeft}s`;

    if (timeLeft <= 0) {
      clearInterval(timerInterval);
      endGame();
    } else if (timeLeft < 20) {
      switchMusic();
    }
  }, 1000);
}

//da finire e mettere apposto
function switchMusic() {
  // Ferma la musica corrente
  backgroundMusic.pause();
  backgroundMusic.currentTime = 2; // Resetta al secondo 2

  // Avvia la nuova musica
  finalMusic.loop = true;
  finalMusic.play().catch((error) => {
    console.error("Errore durante la riproduzione della nuova musica:", error);
  });
}

// Conteggio click
grass.addEventListener("click", () => {
  clicks++;
  clickCounter.textContent = `Click effettuati: ${clicks}`;

  audio.currentTime = 0;
  audio
    .play()
    .catch((error) =>
      console.error("Errore durante la riproduzione dell'audio:", error)
    );

  moveGrass(); // Sposta immediatamente l'erba

  if (clicks >= clicksRequired) {
    endGame();
  }
});

// Fine partita
function endGame() {
  clearInterval(timerInterval);
  grass.style.display = "none"; // Nasconde l'erba
  resultDisplay.textContent =
    clicks >= clicksRequired ? "Missione Completata!" : "Missione Fallita!";
  resultDisplay.style.display = "block";

  if (clicks < clicksRequired) {
    restartButton.style.display = "block";
    backButton.style.display = "block";
  } else {
    backButton.style.display = "block";
  }
}

// Rigioca
function restartGame() {
  // Reset variabili
  timeLeft = 60;
  clicks = 0;
  clicksRequired = 10;

  // Reset UI
  resultDisplay.style.display = "none";
  restartButton.style.display = "none";
  backButton.style.display = "none";

  // Reset erba
  grass.style.display = "block";
  moveGrass(); // Riposiziona subito l'erba

  timerDisplay.textContent = `Tempo rimasto: ${timeLeft}s`;
  clickCounter.textContent = `Click effettuati: ${clicks}`;

  // Riavvia il gioco
  startGame();
}
