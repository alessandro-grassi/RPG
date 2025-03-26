class Game {
    constructor(hero) {
        this.hero = hero;
        this.enemy = new Enemy("Nome", 12, 100, 30, 500);
    }
    turno = 0;
}