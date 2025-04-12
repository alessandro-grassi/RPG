class Hero extends Entity {
    constructor(name, lvl, exp, atk, hp, magic) {
        super(name, lvl, exp, atk, hp);
        this.cooldownMagic = 0;  // Tiene traccia del turno dell'ultima magia
        this.canUseMagic = true; // Indica se l'eroe può usare magie
        this.maxHp = hp; // Salute massima dell'eroe
        this.magic = magic;
        console.log("magia nel costruttore: " + this.magic);   
    }

    useMagic(enemy) {
        if (!this.canUseMagic) {
            alert("Non puoi usare magie in questo turno!");
            return;
        }
        console.log("Magia prima di switch:" + this.magic)
        switch (this.magic) {
            case 1:
                this.fire(enemy);   
                break;
            case 2:
                this.heal();
                break;
            case 3:
                this.thunder(enemy);
                break;
            default:
                console.log("Caso:" +   this.magic);
                alert("Error: magic does not exist");
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
            console.log (`${this.name} non può curarsi, e' gia' al massimo della salute!`);
            return;
        } // Se l'eroe è già al massimo della salute non può curarsi
        this.hp += this.maxHp*2/10 // Cura il 20% della vita

        if(this.hp > this.maxHp) // Se la vita supera il massimo, la riporta al massimo
            this.hp = this.maxHp;
        console.log(`${this.name} si è curato!`);
        output.innerHTML = `${this.name} si è curato!`;
        }

    thunder(enemy) { /* Implementazione futura */ }
}