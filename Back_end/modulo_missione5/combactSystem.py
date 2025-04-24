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

# defaul insert
#  INSERT INTO m5_current_boss (utente, boss_name, healt, bonus_attack, bonus_attack_duration, bonus_defense, bonus_defense_duration)
#  VALUES ('nome utente', 'pagina 0', 0, 0, 0, 0, 0);

#  UPDATE m5_current_boss
#  SET boss_name = 'Nuovo Nome Boss',
#      healt = 100,
#      bonus_attack = 5,
#      bonus_attack_duration = 10,
#      bonus_defense = 2,
#      bonus_defense_duration = 5
#  WHERE utente = 'nome utente';


def enemy_attack(userName):
    #get enemy name
    set_boss_name(userName, "pagina 0")

    enemyName = queryLib.execute(f"""
                        select boss_name
                        from m5_current_boss join utenti on m5_current_boss.utente = utenti.username
                        where username = '{userName}'
                     """)[0][0]
    #get enemy possible attacks
    print("enemyName: ", enemyName)

def set_boss_name(userName, enemyName):
    queryLib.execute_no_return(f"""
        UPDATE m5_current_boss
        SET boss_name = '{enemyName}'
        WHERE utente = '{userName}';
    """)

def enemy_set_healt(enemyName, value):
    queryLib.execute_no_return(f"""
        UPDATE m5_current_boss
        SET healt = {value}
        WHERE boss_name = '{enemyName}';
    """)

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
    enemy_attack("prova")
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

