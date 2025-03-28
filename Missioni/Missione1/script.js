let timeLeft = 60; // Tempo iniziale
let clicks = 0; // Click effettuati
let clicksRequired = 10; // Click richiesti
let timerInterval = null;

const grass = document.getElementById('grass');
const resultDisplay = document.getElementById('result');

// Funzione per spostare la ciocca d'erba casualmente
function moveGrass() {
    const container = document.getElementById('game-container');
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
grass.addEventListener('click', () => {
    clicks++;
    if (clicks >= clicksRequired) {
        endGame();
    }
});

// Fine partita
function endGame() {
    clearInterval(timerInterval);
    grass.style.display = 'none'; // Nascondi l'erba
    resultDisplay.textContent = clicks >= clicksRequired ? 'Missione Completata!' : 'Missione Fallita!';
    resultDisplay.style.display = 'block'; // Mostra il risultato
    restartButton.style.display = 'block'; // Mostra il pulsante "Rigioca"
}

// Rigioca
function restartGame() {
    // Resetta variabili
    timeLeft = 60;
    clicks = 0;
    clicksRequired = 10;

    // Resetta UI
    resultDisplay.style.display = 'none';
    restartButton.style.display = 'none';
    grass.style.display = 'block';
    timerDisplay.textContent = `Tempo rimasto: ${timeLeft}s`;

    // Riavvia il gioco
    startGame();
}