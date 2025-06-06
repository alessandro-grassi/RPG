const timerDisplay = document.getElementById("timer");
const gameContainer = document.getElementById("game-container");
const restartButton = document.getElementById("restart-button");
const backButton = document.getElementById("back-button");
const audio = new Audio('http://localhost:8080/missione1/grassSound.mp3'); // URL dell'audio

//const character = get_personaggio();

let clicks = 0;

const clickCounter = document.getElementById("click-counter");

// Avvia il gioco
function startGame() {
  gameContainer.style.display = "block"; // Mostra l'area di gioco
  moveGrass(); // Sposta l'erba inizialmente
  setInterval(moveGrass, 2000);
  startTimer(); // Avvia il timer
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

let timeLeft = 60; // Tempo iniziale
let clicksRequired = 10; // Click richiesti
let timerInterval = null;

const grass = document.getElementById("grass");
const resultDisplay = document.getElementById("result");

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
  timerInterval = setInterval(() => {
    timeLeft--;
    timerDisplay.textContent = `Tempo rimasto: ${timeLeft}s`;

    if (timeLeft <= 0) {
      clearInterval(timerInterval);
      endGame();
    }
  }, 1000);
}

// Conteggio click
grass.addEventListener("click", () => {
  clicks++; // Incrementa il numero di click
  clickCounter.textContent = `Click effettuati: ${clicks}`; // Aggiorna il testo dell'elemento
  
  audio.play().catch(error => {
                console.error("Errore durante la riproduzione dell'audio:", error);
            });


  moveGrass(); // Sposta l'erba

  // Controlla se il giocatore ha raggiunto il numero di click richiesti
  if (clicks >= clicksRequired) {
    endGame();
  }
});

// Fine partita
function endGame() {
  clearInterval(timerInterval);
  grass.style.display = "none"; // Nascondi l'erba
  resultDisplay.textContent =
    clicks >= clicksRequired ? "Missione Completata!" : "Missione Fallita!";

  if (clicks < clicksRequired) {
    resultDisplay.style.display = "block"; // Mostra il risultato
    restartButton.style.display = "block"; // Mostra il pulsante "Rigioca"
    backButton.style.display = "block"; // Mostra il pulsante "torna indietro"
  } else {
    resultDisplay.style.display = "block"; // Mostra il risultato
    backButton.style.display = "block"; // Mostra il pulsante "torna indietro"
  }
}

// Rigioca
function restartGame() {
  // Resetta variabili
  timeLeft = 60;
  clicks = 0; // Resetta il conteggio dei click
  clicksRequired = 10;

  // Resetta UI
  resultDisplay.style.display = "none";
  restartButton.style.display = "none";
  backButton.style.display = "none";
  grass.style.display = "block";
  timerDisplay.textContent = `Tempo rimasto: ${timeLeft}s`;
  clickCounter.textContent = `Click effettuati: ${clicks}`; // Resetta il conteggio dei click nell'UI

  // Riavvia il gioco
  startGame();
}
