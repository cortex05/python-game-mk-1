# ELF 
from Player import Player

class Elf(Player):
  player_class = "Elf"
  standard_attack = "Swipes"
  special_attack = "Precision Arrow"
  heavy_attack = "Drop Kick"
  description = '''a well balanced fighter.'''

  health = 70
  baseHealth = 70
  strength = 18
  defense = 18
  agility = 40
  def __init__(self, name):
    self.name = name
    print(f"\nElf Selected! Quick and nimble is the way. Congrats {name}!\n\n\n")