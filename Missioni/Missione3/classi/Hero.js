class Hero extends Entity {
    constructor(name, lvl, exp, atk, hp) {
        super(name, lvl, exp, atk, hp);
        this.magia=1; // Magia dell'eroe (1: fuoco, 2: ghiaccio, 3: fulmine)
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
                this.ice(enemy);
                break;
            case 3:
                this.thunder(enemy);
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
    }

    ice(enemy) { /* Implementazione futura */ }

    thunder(enemy) { /* Implementazione futura */ }
}