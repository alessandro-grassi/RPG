/**
 * Oggetto che contiene i dati del gioco.
 * @type {Object}
 */
let dati = {};

/**
 * Variabile che tiene traccia del turno corrente.
 * @type {number}
 */
let turno = 1;

/**
 * Funzione chiamata quando il giocatore preme il pulsante "Attacca".
 * Gestisce l'attacco del giocatore.
 */
function attacca() {
    // Implementazione dell'attacco del giocatore
}

/**
 * Funzione chiamata quando il giocatore preme il pulsante "Magia".
 * Determina quale magia usare in base all'input dell'utente.
 */
function magia() {
    // Capire che magia ha utente, i 3 casi
    if (magia == 1) {
        fuoco();
    } else if (magia == 2) {
        ghiaccio();
    } else if (magia == 3) {
        tuono();
    } else {
        // alert("ERROREEE");
    }
}

/**
 * Funzione che gestisce l'uso della magia "Fuoco".
 */
function fuoco() {
    // Implementazione della magia "Fuoco"
}

/**
 * Funzione che gestisce l'uso della magia "Ghiaccio".
 */
function ghiaccio() {
    // Implementazione della magia "Ghiaccio"
}

/**
 * Funzione che gestisce l'uso della magia "Tuono".
 */
function tuono() {
    // Implementazione della magia "Tuono"
}

/**
 * Funzione che gestisce l'attacco del mostro.
 * @returns {number} Il danno inflitto dal mostro.
 */
function attaccoMostro() {
    let danno = 0;
    return danno;
}

/**
 * Funzione che gestisce il turno del giocatore.
 */
function tuoTurno() {
    // Implementazione del turno del giocatore
}

/**
 * Funzione che gestisce il turno del mostro.
 */
function turnoMostro() {
    // Implementazione del turno del mostro
}

/**
 * Funzione che determina di chi è il turno corrente.
 * Se il turno è pari, è il turno del giocatore.
 * Se il turno è dispari, è il turno del mostro.
 */
function turni() {
    if (turno & 1 == 0) {
        tuoTurno();
    } else {
        turnoMostro();
    }
}

/* Inzio Sezione Gestione Audio */
function playMusic() {
    let audio = new Audio("http://localhost:8080/missione3%/audio/Background.mp3-get_binary_file");
    audio.volume = 0.05;
    audio.play().then(() => {
        console.log("Musica avviata!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
    });
}

function attackSound(){
    let audio = new Audio("http://localhost:8080/missione3%/audio/Attacco.mp3-get_binary_file");
    audio.volume = 0.2;
    audio.play().then(() => {
        console.log("Suono attacco avviato!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
    });
}

function magicSound(){
    let audio = new Audio("http://localhost:8080/missione3%/audio/Magia.mp3-get_binary_file");
    audio.volume = 0.2;
    audio.play().then(() => {
        console.log("Suono magia avviato!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
    });
}
/* Fine Sezione Gestione audio*/