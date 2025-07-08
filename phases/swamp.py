import random
from characters import Player
from enemy_assets import Donkey, Dragon, Godmother, Farquad


def swampLoop(player: Player):
  is_running = True
  nav_coord = {
    "x_val": 0,
    "y_val": 0
  }

  while is_running:
    enemy_selector = random.randint(4,4)
    enemy = None

    if(enemy_selector == 1):
      enemy = Donkey.Donkey()
    elif(enemy_selector == 2):
      enemy = Dragon.Dragon()
    elif(enemy_selector == 3):
      enemy = Godmother.Godmother()
    elif(enemy_selector == 4):
      enemy = Farquad.Farquad()

    print(f'A {enemy.name} appeared!')

    return
  