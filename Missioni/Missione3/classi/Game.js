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
        if (this.round >= this.hero.cooldownMagic + 7) {
            this.hero.canUseMagic = true;
            if(this.round === this.hero.cooldownMagic + 7)
                setTimeout(() => {
                    output.innerHTML = `Puoi usare magie!`;
                }, 1000);
        }
        this.removeStatusEffects();
        this.applyStatusEffects();
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
        if(this.hero.hp < 0) 
            document.getElementById("vitaGiocatore").textContent = 0;
        else
            document.getElementById("vitaGiocatore").textContent = this.hero.hp;

        if(this.selectedEnemy.hp < 0)
            document.getElementById("vitaMostro").textContent = 0;
        else
        document.getElementById("vitaMostro").textContent = this.selectedEnemy.hp;

        document.getElementById("turno").textContent = this.round;
        if(this.hero.canUseMagic)
            magicButton.disabled = false
        else   
            magicButton.disabled = true;
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
        if (this.selectedEnemy.status === "burned" && !this.RNG(5)){
            this.removeStatus();
        }
        if (this.selectedEnemy.status === "paralyzed" && this.RNG(5) === 0) {
            this.removeStatus();
        }
    }

    //Metodo che rimuove lo stato attuale del nemico
    removeStatus(){
        setTimeout(() => {
            output.innerHTML = `Il nemico e' guarito dallo status`;
        }, 1000);
        console.log(`Il nemico e' guarito da ${this.selectedEnemy.status}`);
        this.selectedEnemy.status = "none";
        this.selectedEnemy.statusTurns = 0;
    }

    //Metodo che applica gli effetti di stato al nemico
    applyStatusEffects() {
        if ((!this.hero.isAlive()) || (!this.selectedEnemy.isAlive())) 
            return;
        if (this.selectedEnemy.status === "burned") {
            let burnDamage = Math.floor((this.hero.atk / 3) + this.RNG(10));
            this.selectedEnemy.hp -= burnDamage;
            console.log(`Il nemico subisce ${burnDamage} danni da bruciatura!`);
            setTimeout(() => {
                output.innerHTML = `Il nemico subisce ${burnDamage} danni da bruciatura!`;
            }, 1000);
            }   
        if (this.selectedEnemy.status === "frozen") {
            console.log(`Il nemico è congelato e non può attaccare!`);
            setTimeout(() => {
                output.innerHTML = `Il nemico è congelato e non può attaccare!`;
            }, 1000);
        }
    }
}