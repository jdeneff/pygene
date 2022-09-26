from itertools import combinations_with_replacement
import constants as c
from player import Player
from grid import Grid


class PlayerHandler:
    def __init__(self):
        self.sense_matrix = list(combinations_with_replacement([1,2,3], 5))
        

    def sense(self, player, grid):
        pass

    def act(self, player, grid):
        pass

