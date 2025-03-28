class Game {
    constructor(hero, enemies) {
        this.hero = hero;
        this.enemies = enemies;
        this.selectedEnemy = null;
        this.round = 0;
        this.completedRound = false;
        this.endGame = false;
    }

    //Metodo che... completa il turno.. come dice il nome e la riga di codice
    completeRound() {
        this.completedRound = true;
    }

    //Metodo che permette di passare al round successivo
    nextRound() {
        if (!this.completedRound) throw Error("Error round is not completed");
        this.completedRound = false;

        this.round += 1;
        // Controlla se l'eroe può usare magie
        if (this.round >= this.hero.cooldownMagic + 5) {
            this.hero.canUseMagic = true;
        }
        this.removeStatusEffects();
        return this.round;
    }

    //Metodo che seleziona un nemico casuale dalla lista di nemici
    selectEnemy() {
        return this.enemies[Math.floor(Math.random() * this.enemies.length)];
    }

    //Metodo che gestisce l'attacco del nemico
    enemyAttack() {
        if (this.round % 2 == 0) return;
        return this.selectedEnemy.attack(this.hero);
    }

    //Metodo che controlla se il gioco è finito
    checkEndGame() {
        let victoriousEntity = null;
        if (!this.hero.isAlive()) {
            victoriousEntity = this.selectedEnemy;
        } else if (!this.selectedEnemy.isAlive()) {
            victoriousEntity = this.hero;
        }

        if (victoriousEntity) this.endGame = true;

        return victoriousEntity;
    }

    //Metodo che aggiorna l'interfaccia utente con le informazioni attuali del gioco
    aggiornaUI() {
        document.getElementById("vitaGiocatore").textContent = this.hero.hp;
        document.getElementById("vitaMostro").textContent = this.selectedEnemy.hp;
        document.getElementById("turno").textContent = this.round;
    }

    //Metodo che genera un numero da 0 a max-1
    RNG(max) {
        return Math.floor(Math.random() * max);
    }
    
    //Metodo che controlla la rimozione degli effetti di stato
    removeStatusEffects() {
        if (this.selectedEnemy.status === "frozen" && this.RNG(3) === 0) {
            this.removeStatus();
        }
        if (this.selectedEnemy.status === "burned" && this.RNG(3) === 0) {
            this.removeStatus();
        }
        if (this.selectedEnemy.status === "paralyzed" && this.RNG(5) === 0) {
            this.removeStatus();
        }
    }

    //Metodo che rimuove lo stato attuale del nemico
    removeStatus(){
        this.selectedEnemy.status = "none";
        this.selectedEnemy.statusTurns = 0;
    }
}