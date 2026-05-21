import random
import sys




## Player Stats
player_hp: int = 5
player_dmg: int = 1
player_def: int = 0
# player_spd = int(2)




## Player Slots
weapon_id: int = 0
armour_id: int = 0
# second_id = int(0)
# trinket_id = int(0)




## Enemy Stats
evil_id: int = 0
evil_name: str = "Abubu"
evil_hp: int = 5
evil_dmg: int = 1
evil_LV: int = 1




## Cycle through player slots "'slot'_check()"
def weapon_check():
   global player_dmg


   match weapon_id:
       case 0:
           player_dmg = 1
       case 1:
           player_dmg = 2
def armour_check():
   global player_def


   match armour_id:
       case 0:
           player_def = 0
       case 1:
           player_def = 5


## Cycle through current enemy stats
def evil_check():
   global evil_id, evil_name, evil_hp, evil_LV, evil_dmg


   # evil_name =
   # evil_hp =
   # evil_dmg =
   # evil_LV =


   match evil_id:
       case 0:
           evil_name = "Default"
           evil_hp = 5
           evil_dmg = 1
           evil_LV = 1
       case 1:
           evil_name = "Slime"
           evil_hp = 3
           evil_dmg = 1
           evil_LV = 1
       case 2:
           evil_name = "Moth"
           evil_hp = 2
           evil_dmg = 2
           evil_LV = 1


## Developper/Debbug functions
def exit(x):
   print(f"{x} BREAK")
   sys.exit(0)




## Variables for gameplay
GameLoop = True
turnCount = 0
in_battle = True
choice: int




## Functions for battling
def rng(x, y):
   dice = random.randint(x, y)
   return dice
def battle_prep():
   global evil_id, turnCount
   if turnCount == 0:
       evil_id = rng(1, 2)


       evil_check()
       weapon_check()
       armour_check()


       print(f"A level {evil_LV} {evil_name} approaches!")
       print("What will you do? 1 - attack 2 - run")


## Enters umbrella loop of the game
while GameLoop:
   print("Game Start")


   ## Enters battle loop of the game
   while in_battle:
       if player_hp > 0:
           battle_prep()


           turnCount += 1
           choice = int(input())


           ## Selects the option from the choice variable above through the integer type
           if choice == 1:
               ## Attack


               evil_hp -= player_dmg
               print(f"You dealt {player_dmg} points of damage.")


               player_hp -= (evil_dmg - player_def)
               print(f"{evil_dmg - player_def} damage taken.")


           elif choice == 2:
               ## Retreat


               print("You Run.")
               turnCount = 0
               # in_battle = False
       else:
           print("You died")
           in_battle = False
   exit("GAMELOOP")

