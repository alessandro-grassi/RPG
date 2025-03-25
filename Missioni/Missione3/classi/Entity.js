class Entity {
    constructor(name, lvl, exp, atk, hp) {
        this.name = name;
        this.lvl = lvl;
        this.exp = exp;
        this.atk = atk;
        this.hp = hp;
    }

    //Metodo per controllare se l'entità è ancora viva. Utrile per il controllo del game over.
    isAlive() {
        return this.hp > 0;
    }

    //Metodo per attaccare un'altra entità. Ritorna il danno inflitto. Ereditata perchè utile a entrambi
    attack(target) {
        if (target.hp > 0) {
            let damage = this.atk;
            target.hp -= damage;
            return damage;
        }
        return 0;
    }

}