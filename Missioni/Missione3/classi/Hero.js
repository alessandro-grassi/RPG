class Hero extends Entity {
    constructor(name, lvl, exp, atk, hp) {
        super(name, lvl, exp, atk, hp);
    }

    //Metodo per usare la magia in base a quale magia ha scelto l'utente. Io l'ho immaginata così ne parliamo domani
    useMagic(magic, enemy){
        switch(magic){
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
    }

    //Vedere come implemetare
    fire(enemy){

    }
    
    //Vedere come implemetare
    ice(enemy){

    }

    //Vedere come implemetare
    thunder(enemy){

    }
}