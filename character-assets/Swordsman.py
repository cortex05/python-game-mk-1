# swordsman
from Player import Player
# public class Swordsman extends Hero{
class Swordsman(Player):
  player_class = "Swordsman"
  standard_attack = "Slash"
  special_attack = "Overhead Smash"
  heavy_attack = "Thrust"
  description = '''a well balanced fighter.'''
  def __init__(self, name):
    self.name = name
    print(f"\nSwordsman Selected! Hack and slash it is. Congrats {name}!\n\n\n")