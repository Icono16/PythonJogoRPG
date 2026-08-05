# ## Cycle through current enemy stats
# def evil_check() -> None:
#     global evil_id, evil_name, evil_hp, evil_LV, evil_dmg, evil_spd
#
#     # evil_name =
#     # evil_hp =
#     # evil_dmg =
#     # evil_LV =
#
#     match evil_id:
#         case 0:
#             evil_name = "Default"
#             evil_hp = 5
#             evil_dmg = 1
#             evil_LV = 1
#             evil_spd = 1
#         case 1:
#             evil_name = "Slime"
#             evil_hp = 3
#             evil_dmg = 1
#             evil_LV = 1
#             evil_spd = 1
#         case 2:
#             evil_name = "Moth"
#             evil_hp = 2
#             evil_dmg = 2
#             evil_LV = 1
#             evil_spd = 3

class Enemy:
    def __init__(self, name = "default", hp = 5, dmg = 1, spd = 1, lv = 1):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.spd = spd
        self.LV = lv
    def return_evil(self):


if __name__ == '__main__':
    Moth = Enemy('Moth', 3, 1, 1, 1)
    print(Moth.name, Moth.hp, Moth.dmg, Moth.spd, Moth.LV)