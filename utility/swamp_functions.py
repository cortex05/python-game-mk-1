import random
from Enemy import Enemy
from characters import Player
from enemy_assets import Donkey, Dragon, Godmother, Farquad


def random_enemy():
    enemy_selector = random.randint(1, 4)
    enemy = None

    if (enemy_selector == 1):
        enemy = Donkey.Donkey()
    elif (enemy_selector == 2):
        enemy = Dragon.Dragon()
    elif (enemy_selector == 3):
        enemy = Godmother.Godmother()
    elif (enemy_selector == 4):
        enemy = Farquad.Farquad()

    return enemy


def battle_loop(player: Player, enemy: Enemy):
    while True:
        print('What will you do?\n')
        selection = input(
            '''1 - Attack!\n2 - Check stats\n3 - Go Back\n4 - Quit\n''')

        if int(selection) != 1:
            print('try again\n')
        else:
            break
