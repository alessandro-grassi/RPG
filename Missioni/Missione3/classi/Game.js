class Game {
    constructor(hero) {
        this.hero = hero;
        this.enemy = null;
        this.round = 0;
        this.roundCompleted = false;
    }
    nextRound() {
        if (!roundCompleted) throw Error("Error round is not completed");
        this.roundCompleted = false;
        this.round += 1;
    }
}