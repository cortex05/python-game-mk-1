import os
import random
from Player import Player
# from utility import swamp_functions
from utility.battle_functions import battle_loop


def swamp_loop(player: Player):
    is_running = True
    nav_coord = {
        "x_val": 0,
        "y_val": 0
    }

    while is_running:
        if battle_loop(player):
            continue
        else:
            break
