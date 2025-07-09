import random
from characters import Player
from utility import swamp_functions


def swampLoop(player: Player):
    is_running = True
    nav_coord = {
        "x_val": 0,
        "y_val": 0
    }

    while is_running:
        enemy = swamp_functions.random_enemy()
        print(f'{enemy.name_tense} appeared!\n')

        swamp_functions.battle_loop(player, enemy)

        return
