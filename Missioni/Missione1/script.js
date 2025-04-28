const timerDisplay = document.getElementById('timer');
const gameContainer = document.getElementById('game-container');
const restartButton = document.getElementById('restart-button');


// Avvia il gioco
function startGame() {
    gameContainer.style.display = 'block'; // Mostra l'area di gioco
    moveGrass(); // Sposta l'erba inizialmente
    setInterval(moveGrass, 2000);
    startTimer(); // Avvia il timer
}


// Inizia la missione
function startMission() {
    const playerClass = document.getElementById('classe').value;
    const abilities = Array.from(document.querySelectorAll('input[name="abilita"]:checked'))
                          .map(checkbox => checkbox.value);


    // Simulazione dei dati ricevuti dal server
    const data = {
        tempo: playerClass === 'assassino' ? 50 : playerClass === 'clerico' ? 70 : 60,
        click_richiesti: playerClass === 'guerriero' ? 13 : playerClass === 'mago' ? 8 : 10
    };


    timeLeft = data.tempo || 60;
    clicksRequired = data.click_richiesti || 10;


    alert(`Tempo: ${timeLeft}s, Click richiesti: ${clicksRequired}`);


    // Nascondi la barra di selezione
    document.querySelector('.selection-bar').style.display = 'none';


    startGame(); // Avvia il gioco
}


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
    moveGrass();
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