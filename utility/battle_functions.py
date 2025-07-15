import os
import random
from enemy_assets import Donkey, Dragon, Farquad, Godmother
from utility import swamp_functions


def random_enemy():
    enemy_selector = random.randint(1, 4)
    enemy = None

    if enemy_selector == 1:
        enemy = Donkey.Donkey()
    elif enemy_selector == 2:
        enemy = Dragon.Dragon()
    elif enemy_selector == 3:
        enemy = Godmother.Godmother()
    elif enemy_selector == 4:
        enemy = Farquad.Farquad()

    return enemy


def battle_loop(player):
    enemy = random_enemy()
    print(f'{enemy.name_tense} appeared!\n')

    result, player = swamp_functions.battle_loop(player, enemy)

    if result:
        print('You won!\n\n')
        print(f'Your health is {player.health}')
        input('Press anything to continue')
        os.system('cls')
        return True
    else:
        return False
