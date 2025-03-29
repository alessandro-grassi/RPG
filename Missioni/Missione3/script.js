const atkButton = document.getElementById("atkButton");
const magicButton = document.getElementById("magicButton");
const output = document.getElementById("output")

/**
 * Funzione chiamata quando il giocatore preme il pulsante "Attacca".
 * Gestisce l'attacco del giocatore.
 */
atkButton.addEventListener("click", (e) => {
    if (game.endGame) return;
    if (game.round % 2 != 0) return output.innerHTML = "Non è il tuo turno";

    /* Sezione di attacco del giocatore */
    const hero = game.hero;
    const enemy = game.selectedEnemy;
 
    if(!enemy.avoid()){
        attackSound();
        const heroAtk = hero.attack(enemy);
        output.innerHTML = `Hai inflitto ${heroAtk} punti di danno a ${enemy.name}`;
        announceEndGame(game);
    }
    else {
        output.innerHTML = `${enemy.name} ha schivato l'attacco`;
        console.log("Attacco schivato");
    }
    setTimeout(() => {}, 1000);
    game.completeRound();
    game.aggiornaUI();
    game.nextRound();

    /* Fine sezione di attacco del giocatore*/


    /*Inizio sezione attacco del nemico*/
    // Disabilito i pulsanti al giocatore
    atkButton.disabled = true;
    magicButton.disabled = true;

    const timeout = 1000 + Math.floor(Math.random() * 4000);

    console.log(`Vita eroe: ${game.hero.hp}, vita nemico: ${game.selectedEnemy.hp}`);

    setTimeout(() => {
        if (game.endGame) return;
        
    if(!hero.avoid()){
        attackSound();
        const enemyAtk = game.enemyAttack();
        output.innerHTML = `${enemy.name} ti ha inflitto ${enemyAtk} punti di danno`;

        announceEndGame(game);
    }
    else {
        output.innerHTML = `${hero.name}, hai schivato l'attacco!`;
        console.log("Attacco schivato");
    }
    setTimeout(() => {}, 1000);
        game.completeRound();
        game.aggiornaUI();
        game.nextRound();

        atkButton.disabled = false;
        if(game.hero.canUseMagic)
            magicButton.disabled = false
        else   
            magicButton.disabled = true;
        console.log(`Vita eroe: ${game.hero.hp}, vita nemico: ${game.selectedEnemy.hp}`);
    }, timeout);

});
/*Fine sezione attacco del nemico*/

/**
 * Funzione chiamata quando il giocatore preme il pulsante "Magia".
 * Determina quale magia usare in base all'input dell'utente.
 */

magicButton.addEventListener("click", (e) => {
    const hero = game.hero;
    const enemy = game.selectedEnemy;
 
    if (game.endGame) return;
    if (game.round % 2 != 0) return output.innerHTML = "Non è il tuo turno";

    /*Inizio sezione magia dell'eroe*/
    if(!enemy.avoid()){
        magicSound();
        const hero = game.hero;
        const enemy = game.selectedEnemy;
    
        hero.useMagic(hero.magia, enemy);
    
        announceEndGame(game);
    }
    else {
        output.innerHTML = `${enemy.name} ha schivato l'attacco`;
        console.log("Attacco schivato");
    }

    game.completeRound();
    game.aggiornaUI();
    game.nextRound();

    /*Fine sezione magia dell'eroe*/

    // Disabilito i pulsanti al giocatore
    atkButton.disabled = true;
    magicButton.disabled = true;

    const timeout = 1000 + Math.floor(Math.random() * 4000);

    console.log(`Vita eroe: ${game.hero.hp}, vita nemico: ${game.selectedEnemy.hp}`);

    setTimeout(() => {
        if (game.endGame) return;
        
    if(!hero.avoid()){
        attackSound();
        const enemyAtk = game.enemyAttack();
        output.innerHTML = `${enemy.name} ti ha inflitto ${enemyAtk} punti di danno`;

        announceEndGame(game);
    }
    else {
        output.innerHTML = `${hero.name}, hai schivato l'attacco!`;
        console.log("Attacco schivato");
    }
        game.completeRound();
        game.aggiornaUI();
        game.nextRound();

        atkButton.disabled = false;
        magicButton.disabled = false;
        console.log(`Vita eroe: ${game.hero.hp}, vita nemico: ${game.selectedEnemy.hp}`);
    }, timeout);

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
}



let game = new Game(new Hero("Super Tibet", 80, 7900, 29, 240), [new Enemy("Noce I", 85, 8400, 30, 255)/*, new Enemy("Noce II", 3, 30, 4, 80), new Enemy("Noce Wittelsbach", 4, 30, 5, 100)*/]);
game.selectedEnemy = game.selectEnemy();
/* Inizio sezione chiamate REST */

document.addEventListener("DOMContentLoaded", async (e) => {
    document.getElementById("nomeGiocatore").textContent = game.hero.name;
    document.getElementById("nomeMostro").textContent = game.selectedEnemy.name;
    game.aggiornaUI();
    
});

/* Inzio Sezione Gestione Audio */
function playMusic() {
    let audio = new Audio("http://localhost:8080/missione3%/audio/Background.mp3-get_binary_file");
    audio.volume = 0.05;
    audio.play().then(() => {
        console.log("Musica avviata!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
        
    });
    musicButton.disabled = true;
}

function attackSound() {
    let audio = new Audio("http://localhost:8080/missione3%/audio/Attacco.mp3-get_binary_file");
    audio.volume = 0.2;
    audio.play().then(() => {
        console.log("Suono attacco avviato!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
    });
}

function magicSound() {
    let audio = new Audio("http://localhost:8080/missione3%/audio/Magia.mp3-get_binary_file");
    audio.volume = 0.2;
    audio.play().then(() => {
        console.log("Suono magia avviato!");
    }).catch(error => {
        console.log("Autoplay bloccato! Il browser richiede un'interazione.");
    });
}
/* Fine Sezione Gestione audio*/