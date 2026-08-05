import random
import sys
import enemylist

## Player Stats
player_lv: int = 1
player_hp = {
    "current": 5,
    "max": 5
    }
player_dmg: int = 1
player_def: int = 0
player_exp = {
    "current": 0,
    "max" : 100
    }
player_spd: int = 2


## Player Slots
weapon_id: int = 0
armour_id: int = 0
# second_id = int(0)
# trinket_id = int(0)


## Cycle through player stats "'slot'_check()"
def level_check() -> None:
    global player_lv, player_hp, player_dmg, player_def, player_exp

    if player_exp["current"] >= player_exp["max"]:

        player_exp["current"] = player_exp["current"] - player_exp["max"]

        player_lv += 1

        player_hp["max"] = player_hp["max"] * 2

def weapon_check() -> None:
    global player_dmg

    match weapon_id:
        case 0:
            player_dmg = 1
        case 1:
            player_dmg = 2

def armour_check() -> None:
    global player_def

    match armour_id:
        case 0:
            player_def = 0
        case 1:
            player_def = 5



## Developper/Debbug functions
def dexit(x) -> str:
    print(f"{x} BREAK")
    sys.exit(0)


## Variables for gameplay
GameLoop = True
turnCount = 0
in_battle = True
choice: int = 666
playFirst: bool = True

### todo
"""
evil_id
evil_LV
evil_name
evil_check()

"""

## Functions for battling
def rng(x, y) -> int:
    dice = random.randint(x, y)
    return dice

def battle_prep() -> None:
    global 'evil_id', turnCount
    if turnCount == 0:
        evil_id = rng(1, 2)

        ## TODO evil_check()
        weapon_check()
        armour_check()

        print(f"A level {'evil_LV'} {'evil_name'} approaches!")
        print("What will you do? 1 - attack 2 - run")

def turn_order() -> None:
    global player_spd, evil_spd, playFirst
    if player_spd > evil_spd:
        playFirst = True
    else:
        playFirst = False


# def battle_aftermath():

## Enters umbrella loop of the game
while GameLoop:
    print("Game Start")

    ## Enters battle loop of the game
    while in_battle:
        if player_hp["current"] > 0:
            battle_prep()

            turnCount += 1

            turn_order()

            try:
                choice = int(input())
            except ValueError:
                print("Try again")

            ## Selects the option from the choice variable above through the integer type
            if choice == 1:
                ## Attack

                if playFirst:
                    'evil_hp' -= player_dmg
                    print(f"You dealt {player_dmg} points of damage.")

                    player_hp["current"] -= ('evil_dmg' - player_def)
                    print(f"{'evil_dmg' - player_def} damage taken.")
                elif not playFirst:
                    player_hp["current"] -= ('evil_dmg' - player_def)
                    print(f"{'evil_dmg' - player_def} damage taken.")

                    'evil_hp' -= player_dmg
                    print(f"You dealt {player_dmg} points of damage.")

            elif choice == 2:
                ## Retreat

                print("You Run.")
                turnCount = 0
                # in_battle = False

            if 'evil_hp' <= 0:
                ## Enemy Died
                print("You won!")
                turnCount = 0
                # in_battle = False


        else:
            ## Player Died
            print("You died")
            in_battle = False
    dexit("GAMELOOP")
