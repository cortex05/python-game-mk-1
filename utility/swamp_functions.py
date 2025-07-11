import random
from Enemy import Enemy
from Player import Player
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
        print(f'What will {player.name} do?\n')
        selection = int(input(
            '''1 - Attack!\n2 - Check stats\n3 - Go Back\n4 - Quit\n'''))

        if selection == 1:
            damage_dealt = player.strength
            print(f'{player.name} attacks for {damage_dealt}!\n\n')
            if enemy.max_enemy_health - damage_dealt > 0:
                enemy.max_enemy_health = enemy.max_enemy_health - damage_dealt

                enemy_damage = enemy.enemy_attack_damage
                print(f'The {enemy.name} stands strong!\n\n The {enemy.name} attacks for {enemy_damage} damage!\n\n')

                if player.health - enemy_damage > 0:
                    player.health = player.health - enemy_damage
                    print('You stand strong.\n\n')
                else:
                    print('You are defeated!')
                    break
            else:
                print(f'The {enemy.name} is defeated!')
                break
        elif selection == 4:
            print('Bye\n')
            break
        else:
            print('')