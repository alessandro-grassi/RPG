class Game {
    constructor(hero, enemies) {
        this.hero = hero;
        this.enemies = enemies;
        this.selectedEnemy = null;
        this.round = 0;
        this.completedRound = false;
        this.endGame = false;
    }
    completeRound() {
        this.completedRound = true;
    }
    nextRound() {
        if (!this.completedRound) throw Error("Error round is not completed");
        this.completedRound = false;
        this.round += 1;
        return this.round;
    }
    selectEnemy() {
        return this.enemies[Math.floor(Math.random() * this.enemies.length)];
    }
    enemyAttack() {
        if (this.round % 2 == 0) return;
        return this.selectedEnemy.attack(this.hero);
    }
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
}