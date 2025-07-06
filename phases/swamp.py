import random
from characters import Player
import enemy_assets
import enemy_assets.Farquad
import enemy_assets.Godmother

def swampLoop(player: Player):
    # Call swampOptions with "start" and position variables
  is_running = True
  nav_coord = {
    "x_val": 0,
    "y_val": 0
  }

  while is_running:
    enemy_selector = random.randint(4,4)
    enemy = None

    if(enemy_selector == 1):
      enemy = enemy_assets.Donkey.Donkey()
    elif(enemy_selector == 2):
      enemy = enemy_assets.Dragon.Dragon()
    elif(enemy_selector == 3):
      enemy = enemy_assets.Godmother.Godmother()
    elif(enemy_selector == 4):
      enemy = enemy_assets.Farquad.Farquad()

    print(f'A {enemy.name} appeared!')

    return
  