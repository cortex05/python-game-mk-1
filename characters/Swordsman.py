# swordsman
from Player import Player

class Swordsman(Player):
  player_class = "Swordsman"
  standard_attack = "Slash"
  special_attack = "Overhead Smash"
  heavy_attack = "Thrust"
  description = '''a well balanced fighter.'''

  health = 100
  baseHealth = 100
  strength = 30
  defense = 25
  agility = 20
  def __init__(self, name):
    self.name = name
    print(f"\nSwordsman Selected! Hack and slash it is. Congrats {name}!\n\n\n")