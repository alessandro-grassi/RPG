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
    criticoMissed = False
    if enemyData.get("critico") != None:
        critico = enemyData["critico"]
        if rand(0, 100) > critico:
            print("critico")
            criticoMissed = True

    #execute move
    if not missed:
        if move.get("damage_type") != None:

            damage_type = move["damage_type"]
            if move.get("damge_fis_perc") != None:
                damage = player_get_healt * move["damge_fis_perc"] / 100
            if move.get("damge_mag_perc") != None:
                damage = player_get_healt * move["damge_mag_perc"] / 100
            else:
                if damage_type == "fisico":
                    damage = enemyData["stats"]["danno_fis_base"]
                if damage_type == "magico":
                    damage = enemyData["stats"]["danno_mag_base"]
                if damage_type == "both":
                    damage = enemyData["stats"]["danno_fis_base"] + enemyData["danno_mag_base"]
            
            damage += get_bonuses_sums(userName, "boss", "attack")
            damage -= get_bonuses_sums(userName, "player", "defense")

            player_damage(userName, damage)
            print("damage: ", damage)
            print("damage type: ", damage_type)



        if move.get("recupero_vita") != None:
            recupero_vita = move["recupero_vita"]
            enemy_damage(userName, enemyName, -recupero_vita)
            print("recupero vita: ", recupero_vita)
        

    print(get_bonuses(userName))

        
    
        
        

    print("move: ", move)

    #decrement attack and defense duration
    decrement_bonuses_duration(userName, "boss")



    #add duration to attack and defense
    if not missed:
        if move.get("bonus_defense") != None:
            bonus_defense = move["bonus_defense"]
            add_bonuses(userName, "defense", bonus_defense, move["durata"], "boss")
            print("bonus defense: ", bonus_defense)
            print("bonus defense duration: ", move["durata"])
        if move.get("bonus_attack") != None:
            bonus_attack = move["bonus_attack"]
            add_bonuses(userName, "attack", bonus_attack, move["durata"], "boss")
            print("bonus attack: ", bonus_attack)
            print("bonus attack duration: ", move["durata"])


    print("enemyName: ", enemyName)
    print("enemy healt: ", enemy_get_healt(userName,enemyName))
    print(queryLib.execute(f"""
        SELECT *
        FROM m5_play_data
        WHERE boss_name = '{enemyName}' AND utente = '{userName}';
    """))
    print("enemyData: ", enemyData) 
    print("enemyData moves count: ", moveCount)



def set_level(userName, level):
    if not level.startswith("pagina"):
        bossName = enemy_get_data(level)
        queryLib.execute_no_return(f"""
            UPDATE m5_play_data
            SET boss_name = '{bossName["name"]}',
                boss_healt = {bossName["stats"]["healt"]}
            WHERE utente = '{userName}';
        """)
    else:
        queryLib.execute_no_return(f"""
            UPDATE m5_play_data
            SET boss_name = '{level}',
                boss_healt = 0
            WHERE utente = '{userName}';
        """)
    remove_all_bonuses(userName)

def get_max_player_healt(userName):
    return 300

def player_die(userName):
    level = enemy_get_boss_name(userName)                        
    set_level(userName, level)
    player_set_healt(userName, get_max_player_healt(userName))
        

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

def get_status(userName):
    status = queryLib.execute(f"""
        SELECT status
        FROM m5_play_data
        WHERE utente = '{userName}';
    """)
    if len(status) > 0:
        return status[0][0]
    else:
        return None

def set_status(userName, status):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET status = '{status}'
        WHERE utente = '{userName}';
    """)

def get_bonuses(userName):
    bonuses = queryLib.execute(f"""
        SELECT *
        FROM m5_bonuses
        WHERE utente = '{userName}';
    """)
    if len(bonuses) > 0:
        return bonuses
    else:
        return None
    
def decrement_bonuses_duration(userName,target):
    bonuses = get_bonuses(userName)

    if bonuses != None:
        for bonus in bonuses:
            print("bonus: ", bonus)
            if bonus[5] == target:
                duration = bonus[4]
                if duration > 0:
                    duration -= 1
                    if duration == 0:
                        remove_bonus(userName, bonus[0])
                        print("bonus rimosso")
                    else:
                        update_bonus_duration(userName, bonus[0], duration)
                        print("bonus aggiornato")
                else:
                    remove_bonus(userName, bonus[0])
                    print("bonus rimosso")
    else:
        print("Nessun bonus trovato")

def remove_bonus(userName, bonus_id):
    queryLib.execute_no_return(f"""
        DELETE FROM m5_bonuses
        WHERE utente = '{userName}' AND bonus_id = {bonus_id};
    """)
 
def remove_all_bonuses(userName):
    queryLib.execute_no_return(f"""
        DELETE FROM m5_bonuses
        WHERE utente = '{userName}';
    """)

def update_bonus_duration(userName, bonus_id, duration):
    queryLib.execute_no_return(f"""
        UPDATE m5_bonuses
        SET duration = {duration}
        WHERE utente = '{userName}' AND bonus_id = {bonus_id};
    """)

def add_bonuses(userName, name, value, duration, target):
    queryLib.execute_no_return(f"""
        INSERT INTO m5_bonuses (utente, name, value, duration, target)
        VALUES ('{userName}', '{name}', {value}, {duration}, '{target}');
    """)

def get_bonuses_sums(userName, target, name):
    bonuses = queryLib.execute(f"""
        SELECT SUM(value)
        FROM m5_bonuses
        WHERE utente = '{userName}' AND target = '{target}' AND name = '{name}';
    """)
    if len(bonuses) > 0:
        return bonuses[0][0]
    else:
        return 0


def set_seed(seed):
    random.seed(seed)

def rand(min, max):
    return random.randint(min,max)



if __name__ == "__main__":
    set_seed(123)
    print(random.random())
    print(rand(0,3))
    print(set_mana("playe",3))

