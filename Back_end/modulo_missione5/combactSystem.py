import random 
from Back_end import queryLib
import json

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

# !! da aggiungere vulnerabilita fisica e magica sul database

def enemy_attack(userName):
    player_set_healt(userName, 600)
    queue_defense_duration = None
    queue_attack_duration = None
    #get enemy name
    #enemy_set_boss_name(userName, "Guardiano di Rocciascura")
    enemyName = enemy_get_boss_name(userName)
    #get enemy possible attacks
    enemyData = enemy_get_data(enemyName)
    #choose random attack
    moveCount = len(enemyData["moves"])
    moveIndex = rand(0, moveCount - 1)
    move = enemyData["moves"][moveIndex]
    missed = False


    if move.get("chance") != None:
        chance = move["chance"]
        if rand(0, 100) > chance:
            print("miss")
            missed = True

    #execute move
    if not missed:



        if move.get("damage_type") != None:

            damage_type = move["damage_type"]
            if damage_type == "fisico":
                damage = enemyData["stats"]["danno_fis_base"]
                if enemy_get_attack_bonus_duration(userName, enemyName) > 0:
                    damage += enemy_get_attack_bonus(userName, enemyName)
            if damage_type == "magico":
                damage = enemyData["stats"]["danno_mag_base"]
                if enemy_get_attack_bonus_duration(userName, enemyName) > 0:
                    damage += enemy_get_attack_bonus(userName, enemyName)
            if damage_type == "both":
                damage = enemyData["stats"]["danno_fis_base"] + enemyData["danno_mag_base"]
                if enemy_get_attack_bonus_duration(userName, enemyName) > 0:
                    damage += enemy_get_attack_bonus(userName, enemyName)
            player_damage(userName, damage)
            print("damage: ", damage)
            print("damage type: ", damage_type)

        if move.get("bonus_defense") != None:
            bonus_defense = move["bonus_defense"]
            enemy_set_defense_bonus(userName, enemyName, bonus_defense)
            queue_defense_duration = move["durata"]
            print("bonus defense: ", bonus_defense)
            print("bonus defense duration: ", move["durata"])
        if move.get("bonus_attack") != None:
            bonus_attack = move["bonus_attack"]
            enemy_set_attack_bonus(userName, enemyName, bonus_attack)
            queue_attack_duration = move["durata"]
            print("bonus attack: ", bonus_attack)
            print("bonus attack duration: ", move["durata"])

        if move.get("recupero_vita") != None:
            recupero_vita = move["recupero_vita"]
            enemy_damage(userName, enemyName, -recupero_vita)
            print("recupero vita: ", recupero_vita)

        
    
        
        

    print("move: ", move)

    #decrement attack and defense duration
    enemy_decrement_attack_bonus_duration(userName, enemyName)
    enemy_decrement_defense_bonus_duration(userName, enemyName)

    #add duration to attack and defense
    if queue_attack_duration != None:
        enemy_set_attack_bonus_duration(userName,enemyName,queue_attack_duration)
    
    if queue_defense_duration != None:
        enemy_set_defense_bonus_duration(userName,enemyName,queue_defense_duration)

    print("enemyName: ", enemyName)
    print("enemy healt: ", enemy_get_healt(userName,enemyName))
    print(queryLib.execute(f"""
        SELECT *
        FROM m5_play_data
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """))
    print("enemyData: ", enemyData) 
    print("enemyData moves count: ", moveCount)

def enemy_get_data(enemyName):
    #read json file with enemy data
    # read the json file
    with open("Back_end/modulo_missione5/enemies.json", "r") as f:    
        data = json.load(f)
    # get the list of data
    # return the list
    for enemy in data:
        if enemy["name"] == enemyName:
            return enemy
    # if enemy not found return None
    print("enemy not found")
    return None

def enemy_get_boss_name(userName):
    enemyName = queryLib.execute(f"""
                        SELECT boss_name
                        FROM m5_play_data
                        WHERE utente = '{userName}'
                     """)[0][0]
    return enemyName

def enemy_set_boss_name(userName, enemyName):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
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
        SELECT boss_healt
        FROM m5_play_data
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)
    if len(healt) > 0:
        return healt[0][0]
    else:
        return 0

def enemy_set_healt(userName, enemyName, healt):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET boss_healt = {healt}
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)

def enemy_get_attack_bonus(userName, enemyName):
    attack = queryLib.execute(f"""
        SELECT boss_bonus_attack
        FROM m5_play_data
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)
    if len(attack) > 0:
        return attack[0][0]
    else:
        return 0

def enemy_set_attack_bonus(userName, enemyName, value):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET boss_bonus_attack = {value}
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)

def enemy_get_defense_bonus(userName, enemyName):
    defense = queryLib.execute(f"""
        SELECT boss_bonus_defense
        FROM m5_play_data
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)
    if len(defense) > 0:
        return defense[0][0]
    else:
        return 0

def enemy_set_defense_bonus(userName, enemyName, value):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET boss_bonus_defense = {value}
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)

def enemy_set_attack_bonus_duration(userName, enemyName, attack_duration):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET boss_bonus_attack_duration = {attack_duration}
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)

def enemy_set_defense_bonus_duration(userName, enemyName, defense_duration):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET boss_bonus_defense_duration = {defense_duration}
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)

def enemy_get_attack_bonus_duration(userName, enemyName):
    attack_duration = queryLib.execute(f"""
        SELECT boss_bonus_attack_duration
        FROM m5_play_data
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)
    if len(attack_duration) > 0:
        return attack_duration[0][0]
    else:
        return 0

def enemy_get_defense_bonus_duration(userName, enemyName):
    defense_duration = queryLib.execute(f"""
        SELECT boss_bonus_defense_duration
        FROM m5_play_data
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """)
    if len(defense_duration) > 0:
        return defense_duration[0][0]
    else:
        return 0

def enemy_decrement_attack_bonus_duration(userName, enemyName):
    attack_duration = enemy_get_attack_bonus_duration(userName, enemyName)
    if attack_duration > 0:
        enemy_set_attack_bonus_duration(userName, enemyName, attack_duration - 1)
    else:
        enemy_set_attack_bonus_duration(userName, enemyName, 0)
 
def enemy_decrement_defense_bonus_duration(userName, enemyName):
    defense_duration = enemy_get_defense_bonus_duration(userName, enemyName)
    if defense_duration > 0:
        enemy_set_defense_bonus_duration(userName, enemyName, defense_duration - 1)
    else:
        enemy_set_defense_bonus_duration(userName, enemyName, 0)

def player_get_healt(userName):
    player_healt = queryLib.execute(f"""
        SELECT player_healt
        FROM m5_play_data
        WHERE utente = '{userName}';
    """)
    if len(player_healt) > 0:
        return player_healt[0][0]
    else:
        return 0

def player_set_healt(userName, healt):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET player_healt = {healt}
        WHERE utente = '{userName}';
    """)

def player_damage(userName, damage):
    currentHealt = player_get_healt(userName)
    if currentHealt > 0:
        newHealt = currentHealt - damage
        if newHealt < 0:
            newHealt = 0
        player_set_healt(userName, newHealt)
    else:
        player_set_healt(userName, 0)

def player_get_attack_bonus(userName):
    attack_bonus = queryLib.execute(f"""
        SELECT player_bonus_attack
        FROM m5_play_data
        WHERE utente = '{userName}';
    """)
    if len(attack_bonus) > 0:
        return attack_bonus[0][0]
    else:
        return 0

def player_set_attack_bonus(userName, value):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET player_bonus_attack = {value}
        WHERE utente = '{userName}';
    """)

def player_get_defense_bonus(userName):
    defense_bonus = queryLib.execute(f"""
        SELECT player_bonus_defense
        FROM m5_play_data
        WHERE utente = '{userName}';
    """)
    if len(defense_bonus) > 0:
        return defense_bonus[0][0]
    else:
        return 0

def player_set_defense_bonus(userName, value):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET player_bonus_defense = {value}
        WHERE utente = '{userName}';
    """)

def player_get_attack_bonus_duration(userName):
    attack_duration = queryLib.execute(f"""
        SELECT player_bonus_attack_duration
        FROM m5_play_data
        WHERE utente = '{userName}';
    """)
    if len(attack_duration) > 0:
        return attack_duration[0][0]
    else:
        return 0

def player_set_attack_bonus_duration(userName, duration):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET player_bonus_attack_duration = {duration}
        WHERE utente = '{userName}';
    """)

def player_get_defense_bonus_duration(userName):
    defense_duration = queryLib.execute(f"""
        SELECT player_bonus_defense_duration
        FROM m5_play_data
        WHERE utente = '{userName}';
    """)
    if len(defense_duration) > 0:
        return defense_duration[0][0]
    else:
        return 0

def player_set_defense_bonus_duration(userName, duration):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET player_bonus_defense_duration = {duration}
        WHERE utente = '{userName}';
    """)

def player_decrement_attack_bonus_duration(userName):
    attack_duration = player_get_attack_bonus_duration(userName)
    if attack_duration > 0:
        player_set_attack_bonus_duration(userName, attack_duration - 1)
    else:
        player_set_attack_bonus_duration(userName, 0)

def player_decrement_defense_bonus_duration(userName):
    defense_duration = player_get_defense_bonus_duration(userName)
    if defense_duration > 0:
        player_set_defense_bonus_duration(userName, defense_duration - 1)
    else:
        player_set_defense_bonus_duration(userName, 0)

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

