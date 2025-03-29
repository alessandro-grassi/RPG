class Enemy extends Entity {
    constructor(name, lvl, exp, atk, hp) {
        super(name, lvl, exp, atk, hp);
        this.status = "none";       // Stato attuale ("none", "frozen", "paralyzed", "burned")
        this.statusTurns = 0;       // Turni sotto effetto dello status
    }
}