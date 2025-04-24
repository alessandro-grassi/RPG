import random 
from Back_end import queryLib


lifes = {
    "player" : 10,
    "enemy1" : 5
}
manas = {
    "player" : 10,
    "enemy1" : 5
}


def mele(attackedName, attackerName):
    do_damage(attackedName,rand(3,7))
    
def fire_ball(attackedName, attackerName):
    do_damage( attackedName,rand(6,10))
    use_mana(attackerName, 3)

attacks = {
    "mele" : mele,
    "fire_ball": fire_ball,
}

def set_seed(seed):
    random.seed(seed)

def rand(min, max):
    return random.randint(min,max)

def has_attack(name, attackedName):
    return True

def attack(attackerName, attackedName, attackName):
    if(has_attack(attackerName,attackName)):
        attacks[attackName](attackedName, attackerName)

def set_life(name, value):
    if lifes.get(name) != None:
        lifes[name] = value
    else:
        print("Entità: ",name," inesistente")

def get_life(name):
    print(queryLib.execute("""
CREATE SEQUENCE m5_current_boss_id_seq;

CREATE TABLE m5_current_boss (
    current_boss_id INTEGER PRIMARY KEY DEFAULT NEXTVAL('m5_current_boss_id_seq'),
    utente VARCHAR(255) UNIQUE REFERENCES utenti(username),
    boss_name VARCHAR(255),
    healt INTEGER,
    bonus_attack INTEGER,
    bonus_attack_duration INTEGER,
    bonus_defense INTEGER,
    bonus_defense_duration INTEGER
);
"""))
    return lifes.get(name)

def set_mana(name,value):
    if manas.get(name) != None:
        manas[name] = value
    else:
        print("Entità: ",name," inesistente")

def get_mana(name):
    return manas.get(name)


def do_damage(name, value):
    current_life = get_life(name)
    if current_life != None:
        set_life(name, current_life - value)
    else:
        print("Entità: ",name," inesistente")

def use_mana(name, value):
    current_mana = get_mana(name)
    if current_mana != None:
        set_mana(name,current_mana-value)
    else:
        print("Entità: ",name," inesistente")

if __name__ == "__main__":
    set_seed(123)
    print(random.random())
    print(rand(0,3))
    print(set_mana("playe",3))

