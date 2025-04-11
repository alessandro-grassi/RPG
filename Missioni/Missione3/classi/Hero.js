class Hero extends Entity {
    constructor(name, lvl, exp, atk, hp) {
        super(name, lvl, exp, atk, hp);
        this.magia=2; // Magia dell'eroe (1: fuoco, 2: fulmine, 3: cura)
        this.cooldownMagic = 0;  // Tiene traccia del turno dell'ultima magia
        this.canUseMagic = true; // Indica se l'eroe può usare magie
    }

    useMagic(magic, enemy) {
        if (!this.canUseMagic) {
            alert("Non puoi usare magie in questo turno!");
            return;
        }

        switch (magic) {
            case 1:
                this.fire(enemy);
                break;
            case 2:
                this.thunder(enemy);
                break;
            case 3:
                this.heal
                break;
            default:
                alert("Errorrrrrr: magic does not exist");
        }

        // Dopo aver usato una magia, avvia il cooldown
        this.cooldownMagic = game.round;
        this.canUseMagic = false;
    }

    fire(enemy){
    if (enemy.status !== "none") return; // Se il nemico ha uno stato non si può sovrascriver
    enemy.status = "burned";
    enemy.statusTurns = 1;
    console.log(`${enemy.name} è stato bruciato!`);
    }

    heal() {
        if (this.hp >= this.maxHp){
            console.log (`${this.name} non può curarsi, è già al massimo della salute!`);
            return;
        } // Se l'eroe è già al massimo della salute non può curarsi
        console.log(`${hero.name} si è curato!`);
        }

    thunder(enemy) { /* Implementazione futura */ }
}