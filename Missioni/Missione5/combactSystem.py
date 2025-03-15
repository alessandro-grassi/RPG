import random 

lifes = {
    "player" : 10,
    "enemy1" : 5
}

def mele(attackedName):
    pass
def fire_ball(attackedName):
    pass

attacks = {
    "mele" : mele,
}

def set_seed(seed):
    random.seed(seed)

def rand(min, max):
    return random.randint(min,max)

def has_attack(name, attackedName):
    return True

def attack(attackerName, attackedName, attackName):
    if(has_attack(attackerName,attackName)):
        attacks[attackName](attackName)
    pass

def set_life(name, value):
    if(lifes.get(name)):
        lifes[name] = value

def get_life(name):
    return lifes[name]
    

def do_damage(attackedName, value):
    pass


if __name__ == "__main__":
    set_seed(123)
    print(random.random())
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))
    print(rand(0,3))