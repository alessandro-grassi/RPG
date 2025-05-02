import random 
from Back_end import queryLib
import json


def enemy_attack(userName):

    
    initialize_boss(userName)

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
        randn = rand(0, 100)
        if randn > chance:
            print("miss: ", randn)
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

    player_attack(userName, "Katana")



def player_attack(userName, attackName):
    initialize_boss(userName)

    #get enemy name
    enemyName = enemy_get_boss_name(userName)

    abData = get_ability_data(attackName) 
    missed = False
    if abData.get("chance") != None:
        chance = abData["chance"]
        randn = rand(0, 100)
        if randn > chance:
            print("miss: ", randn)
            missed = True
            return
    if not missed:
        damage = 0
        if abData.get("damage_type") != None:
            damage_type = abData["damage_type"]
            if damage_type == "fisico":
                damage = abData["damage_value"] + get_bonuses_sums(userName, "player", "attack")
            if damage_type == "magico":
                damage = abData["damage_value"] + get_bonuses_sums(userName, "player", "attack")
            if damage_type == "both":
                damage = abData["damage_value"] + get_bonuses_sums(userName, "player", "attack")
            
            damage -= get_bonuses_sums(userName, "boss", "defense")

            enemy_damage(userName, enemyName, damage)
            print("damage: ", damage)
            print("damage type: ", damage_type)

        if abData.get("heal") != None:
            heal = abData["heal"]
            player_set_healt(userName, player_get_healt(userName) + heal)
            print("heal: ", heal)        
    

    #decrement attack and defense duration
    decrement_bonuses_duration(userName, "player")
    #add duration to attack and defense
    if not missed:
        if abData.get("bonus_value") != None:
            bonus_value = abData["bonus_value"]
            if abData["bonus_type"] == "attack":
                add_bonuses(userName, "attack", bonus_value, abData["bonus_duration"], "player")
                print("bonus attack: ", bonus_value)
                print("bonus attack duration: ", abData["bonus_duration"])
            if abData["bonus_type"] == "defense":
                add_bonuses(userName, "defense", bonus_value, abData["bonus_duration"], "player")
                print("bonus defense: ", bonus_value)
                print("bonus defense duration: ", abData["bonus_duration"])
    

    


def get_character_abilities(characterId):
    data = queryLib.execute(f"""
        SELECT *
        FROM relazione_abilità
        WHERE personaggio = {characterId};
    """) 
    if len(data) > 0:
        data = data[0]
        out = {
            "ab1": data[1],
            "ab2": data[2],
            "ab3": data[3],
        }
    else:
        out = None
    return out

def get_ability_data(abilityName):
    data = queryLib.execute(f"""
        SELECT *
        FROM abilita
        WHERE id = '{abilityName}';
    """)
    data2 = queryLib.execute(f"""
        SELECT *
        FROM m5_ability_effects
        WHERE abilita = '{abilityName}';
    """)
    out = None
    if len(data) > 0:
        data = data[0]
        out = {
            "name": data[0],    
            "forza": data[1],
            "destrezza": data[2],
            "intelligenza": data[3],
            "fede": data[4],
            "descrizione": data[5],
        }
        if len(data2) > 0:
            data2 = data2[0]
            out["chance"] = data2[1]
            out["damage_type"] = data2[2]
            out["damage_value"] = data2[3]
            out["bonus_value"] = data2[4]
            out["bonus_type"] = data2[5]
            out["bonus_duration"] = data2[6]
            out["heal"] = data2[7]
    
            
    return out
                            

def initialize_boss(userName):
    index = get_current_index(userName)
    with open("Missioni/Missione5/assets/dialogs.json", "r") as f:
        data = json.load(f)
        print("data: ", data[0])
        fight = None
        if isinstance(data[index][0], dict):
            fight = data[index][0].get("fight")
        else:
            print(f"Unexpected data format: {data[index][0]}")
    if fight != None:
        bossNumber = int(fight.split("-")[-1])-1
        with open("Back_end/modulo_missione5/enemies.json", "r") as f:    
            enemiesData = json.load(f)
        bossName = enemiesData[bossNumber]["name"]
        if enemy_get_boss_name(userName) != bossName:
            enemy_set_boss_name(userName, bossName)
            set_page(userName, bossName)



def set_page(userName, page):
    bossName = enemy_get_data(page)

    if bossName != None:
        queryLib.execute_no_return(f"""
            UPDATE m5_play_data
            SET boss_name = '{bossName["name"]}',
                boss_healt = {bossName["stats"]["vita"]}
            WHERE utente = '{userName}';
        """)
    else:
        queryLib.execute_no_return(f"""
            UPDATE m5_play_data
            SET boss_name = '{page}',
                boss_healt = 0
            WHERE utente = '{userName}';
        """)
    remove_all_bonuses(userName)

def get_max_player_healt(characterId):
    vigore = queryLib.execute(f"""
        SELECT "Vigore"
        FROM personaggi
        WHERE id = {characterId};
    """)   
    print("vigore: ", vigore)
    return vigore[0][0] * 100

def player_die(userName):
    page = enemy_get_boss_name(userName)                        
    set_page(userName, page)
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

def enemy_get_max_healt(userName):
    enemyName = enemy_get_boss_name(userName)
    enemyData = enemy_get_data(enemyName)
    if enemyData != None:
        return enemyData["stats"]["vita"]
    else:
        return 0

def enemy_damage(userName, enemyName, damage):
    currentHealt = enemy_get_healt(userName, enemyName)
    if currentHealt > 0:
        newHealt = currentHealt - damage
        if newHealt < 0:
            newHealt = 0
        if newHealt > enemy_get_max_healt(userName):
            newHealt = enemy_get_max_healt(userName)
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
        if newHealt > get_max_player_healt(userName):
            newHealt = get_max_player_healt(userName)
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
        if bonuses[0][0] != None:
            return bonuses[0][0]
        else:
            return 0
    else:
        return 0

def get_dialog_index(userName):
    return {
        "current_index": get_current_index(userName),
        "last_image": get_last_image(userName)
    }

def get_current_index(userName):
    current_index = queryLib.execute(f"""
        SELECT current_index
        FROM m5_play_data
        WHERE utente = '{userName}';
    """)
    if len(current_index) > 0:
        return current_index[0][0]
    else:
        return 0
def get_last_image(userName):
    last_image = queryLib.execute(f"""
        SELECT last_image
        FROM m5_play_data
        WHERE utente = '{userName}';
    """)
    if len(last_image) > 0:
        return last_image[0][0]
    else:
        return 0
def set_current_index(userName, current_index):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET current_index = {current_index}
        WHERE utente = '{userName}';
    """)
def set_last_image(userName, last_image):
    queryLib.execute_no_return(f"""
        UPDATE m5_play_data
        SET last_image = {last_image}
        WHERE utente = '{userName}';
    """)


def set_seed(seed):
    random.seed(seed)

def rand(min, max):
    return random.randint(min,max)



if __name__ == "__main__":
    set_seed(123)
    print(random.random())
    print(rand(0,3))

