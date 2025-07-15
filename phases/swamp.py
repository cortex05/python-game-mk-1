import os
import random
from Player import Player
# from utility import swamp_functions
from utility.battle_functions import battle_launch


def swamp_loop(player: Player):
    is_running = True
    nav_coord = {
        "x_val": 0,
        "y_val": 0
    }

    while is_running:
        if battle_launch(player):
            continue
        else:
            break
