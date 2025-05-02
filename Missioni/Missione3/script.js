const atkButton = document.getElementById("atkButton");
const magicButton = document.getElementById("magicButton");

const continueButton = document.getElementById("continueButton");
const retryButton = document.getElementById("retryButton");
const exitButtons = document.getElementsByClassName("exitButton");


const output = document.getElementById("output")
const endGameScreen = document.getElementById("messaggioFineGioco");

var genericAudio = new Audio("http://localhost:8080/missione3/audio/Background.mp3-get_binary");
var attackAudio = new Audio("http://localhost:8080/missione3/audio/Attacco.mp3-get_binary");
var magicAudio = new Audio("http://localhost:8080/missione3/audio/Magia.mp3-get_binary");
var audioMuted = false; // variabile globale!

const magieDescriptions = {
    1: "Palla di Fuoco ",
    2: "Aromaterapia",
    3: "Fulmine Devastante "
};

document.addEventListener("DOMContentLoaded", (e) => {
    game.aggiornaUI();
    // Aggiorno l'input con l'utente preso dai cookie
    const idPersonaggio = get_personaggio();
    console.log(idPersonaggio);
    const inputHiddenUserId = document.getElementById("uid");
    inputHiddenUserId?.value = idPersonaggio;
});

continueButton.addEventListener("click", (e) => {
    const winner = game.getWinner();
    if (winner?.constructor.name !== "Hero") return;
    game.reset();
    if (!game.remaingEnemies()) {
        endGameScreen.style.display = "flex";
        game.endGame = true;
        // Chiamare funzione completion
        //completion();
        return;
    }
    game.aggiornaUI();
    atkButton.disabled = false;
    magicButton.disabled = false;
    e.target.style.display = "none";
});

retryButton.addEventListener("click", () => {
    const winner = game.getWinner();
    if (winner?.constructor.name !== "Enemy") return;

    // Aggiorno la pagina
    window.location.reload();
});

// Pulsante per uscire dalla missione in caso di sconfitta
Array.from(exitButtons).forEach(exitButton => {
    exitButton.addEventListener("click", () => {
        const winner = game.getWinner();
        if (winner?.constructor.name !== "Enemy") return;
        window.location.href = "../SceltaMissione/sm_home.html";
    }); 
});

function useActionButton(button, action) {
    button.addEventListener("click", (e) => {
        if (game.endGame) return;
        if (game.round % 2 != 0) return output.innerHTML = "Non è il tuo turno";

        // Sezione di attacco del giocatore
        const hero = game.hero;
        const enemy = game.selectedEnemy;

        if (!enemy.avoid()) {
            action(hero, enemy);
            // Controllo lo stato della partita
            /*
                Vince l'eroe (si prosegue)
                Termina la partita:
                 - Sconfitta da parte dell'eroe (Ricomincia il gioco)
                 - Non ci sono più mostri da combattere (salvo lo stato della partita)
            */
            checkGameStatus();
        } else {
            output.innerHTML = `${enemy.name} ha schivato l'attacco`;
            console.log("Attacco schivato");
        }

        game.completeRound();
        game.aggiornaUI();
        game.nextRound();

        //Fine sezione attacco del giocatore
        // Disabilita i pulsanti mentre il nemico pensa
        atkButton.disabled = true;
        magicButton.disabled = true;

        if ((!hero.isAlive()) || (!enemy.isAlive()))
            return;
        //Inizio sezione attacco del nemico
        // Dopo 2 secondi cambia il testo in "Il boss sta pensando..."
        setTimeout(() => {
            output.innerHTML = `${enemy.name} sta pensando...`;

            // Dopo 2 secondi + ritardo casuale il nemico attacca
            const timeout = 2000 + Math.floor(Math.random() * 1000);
            setTimeout(() => {
                if (game.endGame) return;

                if (!hero.avoid()) {
                    attackSound();
                    const enemyAtk = game.enemyAttack();
                    output.innerHTML = `${enemy.name} ti ha inflitto ${enemyAtk} punti di danno`;
                } else {
                    output.innerHTML = `${hero.name}, hai schivato l'attacco!`;
                    console.log("Attacco schivato");
                }

                checkGameStatus();

                game.completeRound();
                game.aggiornaUI();
                game.nextRound();

                //Fine sezione attacco del nemico
                // Riattiva i pulsanti
                atkButton.disabled = false;
                magicButton.disabled = !game.hero.canUseMagic;
            }, timeout);

        }, 2000);
    });
}

/**
 * Funzione chiamata quando il giocatore preme il pulsante "Attacca".
 * Gestisce l'attacco del giocatore.
 */

useActionButton(atkButton, function (hero, enemy) {
    attackSound();
    const heroAtk = hero.attack(enemy);
    output.innerHTML = `Hai inflitto ${heroAtk} punti di danno a ${enemy.name}`;
});

/*Fine sezione attacco del nemico*/

/**
 * Funzione chiamata quando il giocatore preme il pulsante "Magia".
 * Determina quale magia usare in base all'input dell'utente.
 */

useActionButton(magicButton, function (hero, enemy) {
    magicSound();
    hero.useMagic(enemy);

    // Prendo la descrizione della magia dal dizionario
    const magiaUsata = magieDescriptions[hero.magic] || "Magia Sconosciuta";
    output.innerHTML = `Hai usato <b>${magiaUsata}</b> su ${enemy.name}!`;
});
/*Fine sezione attacco del nemico*/

// Annuncia la fine del gioco
function checkGameStatus() {
    const winner = game.getWinner();
    if (!winner) return;
    if (winner.constructor.name === "Hero") {
        continueButton.style.display = "block";
        output.innerHTML = 'Hai vinto!!';
    } else {
        retryButton.style.display = "block";
        exitButton.style.display = "block";
        output.innerHTML = 'Hai perso...';
    }
}

const heroesInfos = [
    {
        name: "Super Tibet",
        lvl: 80,
        exp: 7900,
        atk: 29,
        hp: 240,
        magic: 1,
    },
    {
        name: "Mario il Grande",
        lvl: 100,
        exp: 10000,
        atk: 50,
        hp: 2000,
        magic: 2,
    }
];

const selectedHeroInfo = heroesInfos[Math.round(Math.random() * heroesInfos.length)];

console.log(selectedHeroInfo);

let game = new Game(selectedHeroInfo, [new Enemy("Noce I", 85, 8400, 30, 255, "http://localhost:8080/missione3/media/mostro.png-get_binary"), new Enemy("Noce II", 90, 30, 60, 150, "http://localhost:8080/missione3/media/mostro2.png-get_binary"), new Enemy("Noce Wittelsbach", 80, 30, 20, 400, "http://localhost:8080/missione3/media/mostro3.png-get_binary")]);
game.selectedEnemy = game.selectEnemy();
/* Inizio sezione chiamate REST */

/* Inzio Sezione Gestione Audio */
function playMusic() {
    if (genericAudio.volume == 0.05) {
        genericAudio.volume = 0;
        genericAudio.pause();
        console.log("Musica stop!");
        return;
    }
    genericAudio.play();
    genericAudio.volume = 0.05;
    genericAudio.play().then(() => {
        console.log("Musica avviata!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");

    });
    //musicButton.disabled = true;
}

function attackSound() {
    if (audioMuted) return;
    attackAudio.volume = 0.2;
    attackAudio.play().then(() => {
        console.log("Suono attacco avviato!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
    });
}

function magicSound() {
    if (audioMuted) return;
    magicAudio.volume = 0.2;
    magicAudio.play().then(() => {
        console.log("Suono magia avviato!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
    });
}

function GestisciAudio() {
    if (!audioMuted) {
        genericAudio.volume = 0;
        attackAudio.volume = 0;
        magicAudio.volume = 0;
        audioMuted = true;
        document.getElementById("muteSound").querySelector("img").src = "http://localhost:8080/missione3/media/unmute.png-get_binary";

        console.log("Audio disattivato!");
    } else {
        genericAudio.volume = 0.05;
        attackAudio.volume = 0.2;
        magicAudio.volume = 0.2;
        audioMuted = false;
        document.getElementById("muteSound").querySelector("img").src = "http://localhost:8080/missione3/media/mute.png-get_binary";

        console.log("Audio attivato!");
    }
}
/* Fine Sezione Gestione audio*/