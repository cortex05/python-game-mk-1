import os
import random
from Player import Player
from utility import swamp_functions


def swamp_loop(player: Player):
    is_running = True
    nav_coord = {
        "x_val": 0,
        "y_val": 0
    }

    while is_running:
        enemy = swamp_functions.random_enemy()
        print(f'{enemy.name_tense} appeared!\n')

        result, player = swamp_functions.battle_loop(player, enemy)

        if result:
            print('You won!\n\n')
            print(f'Your health is {player.health}')
            input('Press anything to continue')
            os.system('cls')
        else:
            return
