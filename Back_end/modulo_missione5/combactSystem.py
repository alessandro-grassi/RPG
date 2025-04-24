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

    enemyName = enemy_get_boss_name(userName)
    #get enemy possible attacks
    print("enemyName: ", enemyName)
    print("enemy healt: ", enemy_get_healt(userName,enemyName))

def enemy_get_boss_name(userName):
    enemyName = queryLib.execute(f"""
                        select boss_name
                        from m5_current_boss join utenti on m5_current_boss.utente = utenti.username
                        where username = '{userName}'
                     """)[0][0]
    return enemyName

def enemy_set_boss_name(userName, enemyName):
    queryLib.execute_no_return(f"""
        UPDATE m5_current_boss
        SET boss_name = '{enemyName}'
        WHERE utente = '{userName}';
    """)

def enemy_damage(userName, enemyName, damage):
    currentHealt = enemy_get_healt(userName, enemyName)
    if currentHealt > 0:
        newHealt = currentHealt - damage
        if newHealt < 0:
            newHealt = 0
        enemy_set_healt(userName, enemyName, newHealt)
    else:
        enemy_set_healt(userName, enemyName, 0)

def enemy_get_healt(userName, enemyName):
    healt = queryLib.execute(f"""
        SELECT healt
        FROM m5_current_boss
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)
    if len(healt) > 0:
        return healt[0][0]
    else:
        return 0

def enemy_set_healt(userName, enemyName, healt):
    queryLib.execute_no_return(f"""
        UPDATE m5_current_boss
        SET healt = {healt}
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)

def enemy_get_attack(userName, enemyName):
    attack = queryLib.execute(f"""
        SELECT bonus_attack
        FROM m5_current_boss
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)
    if len(attack) > 0:
        return attack[0][0]
    else:
        return 0

def enemy_set_attack(userName, enemyName, value):
    queryLib.execute_no_return(f"""
        UPDATE m5_current_boss
        SET bonus_attack = {value}
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)

def enemy_get_defense(userName, enemyName):
    defense = queryLib.execute(f"""
        SELECT bonus_defense
        FROM m5_current_boss
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)
    if len(defense) > 0:
        return defense[0][0]
    else:
        return 0

def enemy_set_defense(userName, enemyName, value):
    queryLib.execute_no_return(f"""
        UPDATE m5_current_boss
        SET bonus_defense = {value}
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)

def enemy_set_attack_duration(userName, enemyName, attack_duration):
    queryLib.execute_no_return(f"""
        UPDATE m5_current_boss
        SET bonus_attack_duration = {attack_duration}
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)

def enemy_set_defense_duration(userName, enemyName, defense_duration):
    queryLib.execute_no_return(f"""
        UPDATE m5_current_boss
        SET bonus_defense_duration = {defense_duration}
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)

def enemy_get_attack_duration(userName, enemyName):
    attack_duration = queryLib.execute(f"""
        SELECT bonus_attack_duration
        FROM m5_current_boss
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)
    if len(attack_duration) > 0:
        return attack_duration[0][0]
    else:
        return 0

def enemy_get_defense_duration(userName, enemyName):
    defense_duration = queryLib.execute(f"""
        SELECT bonus_defense_duration
        FROM m5_current_boss
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)
    if len(defense_duration) > 0:
        return defense_duration[0][0]
    else:
        return 0

def enemy_decrement_attack_duration(userName, enemyName):
    attack_duration = enemy_get_attack_duration(userName, enemyName)
    if attack_duration > 0:
        enemy_set_attack_duration(userName, enemyName, attack_duration - 1)
    else:
        enemy_set_attack_duration(userName, enemyName, 0)
 
def enemy_decrement_defense_duration(userName, enemyName):
    defense_duration = enemy_get_defense_duration(userName, enemyName)
    if defense_duration > 0:
        enemy_set_defense_duration(userName, enemyName, defense_duration - 1)
    else:
        enemy_set_defense_duration(userName, enemyName, 0)

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

