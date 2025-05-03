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
            let damage = Math.floor(Math.random() * this.atk) + 10;
            damage > target.hp ? target.hp = 0 : target.hp -= damage;
            return damage;
        }
        return 0;
    }

    //Metodo utilizzabile sia dal mostro che dall'eroe, per schivare
    avoid(){
        let avoid = RNG(8);
        if (avoid == 0)
            return true;
        return false;
    }
}