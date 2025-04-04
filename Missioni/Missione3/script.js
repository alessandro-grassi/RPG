const atkButton = document.getElementById("atkButton");
const magicButton = document.getElementById("magicButton");
const output = document.getElementById("output")
var genericAudio = new Audio("http://localhost:8080/missione3/audio/Background.mp3-get_binary");
var attackAudio = new Audio("http://localhost:8080/missione3/audio/Attacco.mp3-get_binary");
var magicAudio = new Audio("http://localhost:8080/missione3/audio/Magia.mp3-get_binary");
    
const magieDescriptions = {
    1: "Palla di Fuoco ",
    2: "Esplosione Ghiacciata ",
    3: "Fulmine Devastante "
};

/**
 * Funzione chiamata quando il giocatore preme il pulsante "Attacca".
 * Gestisce l'attacco del giocatore.
 */
atkButton.addEventListener("click", (e) => {
    if (game.endGame) return;
    if (game.round % 2 != 0) return output.innerHTML = "Non è il tuo turno";

    // Sezione di attacco del giocatore
    const hero = game.hero;
    const enemy = game.selectedEnemy;

    if (!enemy.avoid()) {
        attackSound();
        const heroAtk = hero.attack(enemy);
        output.innerHTML = `Hai inflitto ${heroAtk} punti di danno a ${enemy.name}`;
        announceEndGame(game);
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

        // Dopo 3 secondi + ritardo casuale il nemico attacca
        const timeout = 3000 + Math.floor(Math.random() * 1000);
        setTimeout(() => {
            if (game.endGame) return;

            if (!hero.avoid()) {
                attackSound();
                const enemyAtk = game.enemyAttack();
                output.innerHTML = `${enemy.name} ti ha inflitto ${enemyAtk} punti di danno`;

                announceEndGame(game);
            } else {
                output.innerHTML = `${hero.name}, hai schivato l'attacco!`;
                console.log("Attacco schivato");
            }

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

/*Fine sezione attacco del nemico*/

/**
 * Funzione chiamata quando il giocatore preme il pulsante "Magia".
 * Determina quale magia usare in base all'input dell'utente.
 */

magicButton.addEventListener("click", (e) => {
    if (game.endGame) return;
    if (game.round % 2 != 0) return output.innerHTML = "Non è il tuo turno";

    const hero = game.hero;
    const enemy = game.selectedEnemy;

    if (!enemy.avoid()) {
        magicSound();
        hero.useMagic(hero.magia, enemy);

        // Prendo la descrizione della magia dal dizionario
        const magiaUsata = magieDescriptions[hero.magia] || "Magia Sconosciuta";
        output.innerHTML = `Hai usato <b>${magiaUsata}</b> su ${enemy.name}!`;

        announceEndGame(game);
    } else {
        output.innerHTML = `${enemy.name} ha schivato la magia`;
        console.log("Attacco schivato");
    }

    game.completeRound();
    game.aggiornaUI();
    game.nextRound();

    // Disabilita i pulsanti mentre il nemico pensa
    atkButton.disabled = true;
    magicButton.disabled = true;

    if ((!hero.isAlive()) || (!enemy.isAlive())) 
        return;
    // Dopo 2 secondi cambia il testo in "Il boss sta pensando..."
    setTimeout(() => {
        output.innerHTML = `${enemy.name} sta pensando...`;

        // Dopo 3 secondi + ritardo casuale il nemico attacca
        const timeout = 3000 + Math.floor(Math.random() * 1000);
        setTimeout(() => {
            if (game.endGame) return;

            if (!hero.avoid()) {
                attackSound();
                const enemyAtk = game.enemyAttack();
                output.innerHTML = `${enemy.name} ti ha inflitto ${enemyAtk} punti di danno`;

                announceEndGame(game);
            } else {
                output.innerHTML = `${hero.name}, hai schivato l'attacco!`;
                console.log("Attacco schivato");
            }

            game.completeRound();
            game.aggiornaUI();
            game.nextRound();

            atkButton.disabled = false;
            if (game.hero.canUseMagic) magicButton.disabled = false;
            else magicButton.disabled = true;
        }, timeout);
    }, 2000);
});
/*Fine sezione attacco del nemico*/

// Annuncia la fine del gioco
function announceEndGame(game) {
    const winner = game.checkEndGame();
    if (!winner) return;
    if (winner.constructor.name === "Hero") {
        output.innerHTML = 'Hai vinto!!';
    } else {
        output.innerHTML = 'Hai perso...';
    }

    atkButton.disabled = true;
    magicButton.disabled = true;
    game.endGame = true;

    output.style.pointerEvents = "none";
    output.style.userSelect = "none";
}



let game = new Game(new Hero("Super Tibet", 80, 7900, 29, 240)/*, new Hero("Antonio lo Gnomo", 80, 7900, 50, 80)*/, [new Enemy("Noce I", 85, 8400, 30, 255), new Enemy("Noce II", 90, 30, 60, 150), new Enemy("Noce Wittelsbach", 80, 30, 20, 400)]);
game.selectedEnemy = game.selectEnemy();
/* Inizio sezione chiamate REST */

document.addEventListener("DOMContentLoaded", async (e) => {
    document.getElementById("nomeGiocatore").textContent = game.hero.name;
    document.getElementById("nomeMostro").textContent = game.selectedEnemy.name;
    game.aggiornaUI();
    
});

/* Inzio Sezione Gestione Audio */
function playMusic() {
    if (genericAudio.volume == 0.05) {
        genericAudio.volume = 0;
        genericAudio.pause;
        console.log("Musica stop!");
        return;
    }
    genericAudio.play;
    genericAudio.volume = 0.05;
    genericAudio.play().then(() => {
        console.log("Musica avviata!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
        
    });
    //musicButton.disabled = true;
}

function attackSound() {
    attackAudio.volume = 0.2;
    attackAudio.play().then(() => {
        console.log("Suono attacco avviato!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
    });
}

function magicSound() {
    magicAudio.volume = 0.2;
    magicAudio.play().then(() => {
        console.log("Suono magia avviato!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
    });
}

let audioMuted = false; // variabile globale!

function GestisciAudio() {
    if (!audioMuted) {
        genericAudio.volume = 0;
        attackAudio.volume = 0;
        magicAudio.volume = 0;
        audioMuted = true;
        document.getElementById("muteSound").src = "http://localhost:8080/missione3/media/unmute.png-get_binary"
        console.log("Audio disattivato!");
    } else {
        genericAudio.volume = 0.05;
        attackAudio.volume = 0.2;
        magicAudio.volume = 0.2;
        audioMuted = false;
        document.getElementById("muteSound").src = "http://localhost:8080/missione3/media/mute.png-get_binary"
        console.log("Audio attivato!");
    }
}
/* Fine Sezione Gestione audio*/