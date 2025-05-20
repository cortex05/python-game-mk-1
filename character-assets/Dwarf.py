from Player import Player

class Dwarf(Player):
  player_class = "Dwarf"
  standard_attack = "Slash"
  special_attack = "Earth shaker"
  heavy_attack = "Guillotine"
  description = '''a well balanced fighter.'''

  health = 120
  baseHealth = 120
  strength = 50
  defense = 30
  agility = 15
  def __init__(self, name):
    self.name = name
    print(f"\nDwarf Selected! Heavy hitter I see. Congrats {name}!\n\n\n")