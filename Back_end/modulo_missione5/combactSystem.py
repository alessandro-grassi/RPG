import random 


moves = [
    {
        "mossa" : "pugno",
        "danno" : 100
    },
    {
        "mossa" : "ammasso",
        "danno" : 120
    },
    {
        "mossa" : "carica",
        "danno" : 150
    },
    {
        "mossa" : "folgorazione",
        "danno" : 50
    }
]

stats = {
    "Vita" : 700,
    "Vigore" : 7,
    "Forza" : 10,
    "Destrezza" : 0,
    "Intelligenza" : 1,
    "Fede" : 3
}

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

def do_damage_boss():
    num = rand(1, 100)
    if num <= 60:
        return {"mossa": moves[0]["mossa"], "danno": moves[0]["danno"]}
    elif num > 60 and num <= 80:
        return {"mossa": moves[1]["mossa"], "danno": moves[1]["danno"]}
    elif num > 80 and num <= 95:
        return {"mossa": moves[2]["mossa"], "danno": moves[2]["danno"]}
    else:
        return {"mossa": moves[3]["mossa"], "danno": moves[3]["danno"]}
    
def get_stats():
    return stats

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