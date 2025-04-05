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
    startGame(); // Avvia il gioco
}