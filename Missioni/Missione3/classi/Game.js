class Game {
    constructor(heroInfo, enemies) {
        this.heroInfo = heroInfo;
        this.hero = new Hero(this.heroInfo.name, this.heroInfo.lvl, this.heroInfo.exp, this.heroInfo.atk, this.heroInfo.hp, this.heroInfo.magic);
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

    //Metodo che rimuove il nemico dall'array di nemici
    removeEnemy() {
        this.enemies.splice(this.enemies.indexOf(this.selectedEnemy), 1);
    }

    reset() {
        // Creo lo stesso eroe con le statistiche di partenza
        this.hero = null;
        this.hero = new Hero(this.heroInfo.name, this.heroInfo.lvl, this.heroInfo.exp, this.heroInfo.atk, this.heroInfo.hp, this.heroInfo.magic);

        this.removeEnemy();
        this.selectedEnemy = this.selectEnemy();

        this.round = 0;
        this.completedRound = false;
        this.endGame = false;
    }

    //Metodo che controlla se il gioco è finito
    getWinner() {
        let victoriousEntity = null;
        if (!this.hero.isAlive()) {
            victoriousEntity = this.selectedEnemy;
        } else if (!this.selectedEnemy?.isAlive()) {
            victoriousEntity = this.hero;
        }

        return victoriousEntity;
    }

    remaingEnemies() {
        if (this.enemies.length === 0) return false;
        return true;
    }

    //Metodo che aggiorna l'interfaccia utente con le informazioni attuali del gioco
    aggiornaUI() {
        /* Mostro */
        document.getElementById("immagineMostro").src = this.selectedEnemy.imageUrl;
        document.getElementById("nomeMostro").textContent = this.selectedEnemy.name;
        document.getElementById("vitaMostro").textContent = this.selectedEnemy.hp;
        /* Mostro */
        
        /* Eroe */
        document.getElementById("vitaGiocatore").textContent = this.hero.hp;
        /* Eroe */

        document.getElementById("turno").textContent = this.round;

        magicButton.disabled = !this.hero.canUseMagic;
    }
    
    //Metodo che controlla la rimozione degli effetti di stato
    removeStatusEffects() {
        if (this.selectedEnemy.status === "burned" && !RNG(5)){
            this.removeStatus();
        }
        if (this.selectedEnemy.status === "paralyzed" && RNG(5) === 0) {
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
            let burnDamage = Math.floor((this.hero.atk / 3) + RNG(10));
            this.selectedEnemy.hp -= burnDamage;
            console.log(`Il nemico subisce ${burnDamage} danni da bruciatura!`);
            setTimeout(() => {
                output.innerHTML = `Il nemico subisce ${burnDamage} danni da bruciatura!`;
            }, 1000);
            }   
    }
}