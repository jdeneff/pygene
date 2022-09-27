import turtle as tu
from itertools import product
from copy import copy
import constants as c
from player import Player
from grid import Grid

# Sensing done on orthogonal points and center. Notation using numpad numbers: [8, 4, 5, 6, 2]
# 7 8 9
# 4 5 6
# 1 2 3

class PlayerHandler:
    def __init__(self):
        self.sense_matrix = list(product([0,1,2], repeat=5))
        sense_copy = copy(self.sense_matrix)
        for item in sense_copy:
            if item[2] == 2:
                self.sense_matrix.remove(item)
            elif item.count(2) > 2:
                self.sense_matrix.remove(item)
            elif (item[0] == 2 and item[4] == 2) or (item[1] == 2 and item[3] == 2):
                self.sense_matrix.remove(item)

    def sense(self, player:Player, grid:Grid):
        p_row, p_col = player.get_position()
        sense_input = []
        sense_input.append(grid.food_grid[p_row-1][p_col])
        sense_input.append(grid.food_grid[p_row][p_col-1])
        sense_input.append(grid.food_grid[p_row][p_col])
        sense_input.append(grid.food_grid[p_row][p_col+1])
        sense_input.append(grid.food_grid[p_row+1][p_col])

        tup_sense_input = tuple(sense_input)
        #print(f'Senses = {tup_sense_input}')

        return tup_sense_input

    def act(self, player:Player, grid:Grid):
        sense_input = self.sense(player, grid)
        index = self.sense_matrix.index(sense_input)
        action = player.genes[index]
        #print(f'Action = {action}')

        # Movement
        if action == 0:
            tar_row, tar_col = player.move_target('n')
        elif action == 1:
            tar_row, tar_col = player.move_target('w')
        elif action == 2:
            tar_row, tar_col = player.move_target('e')
        elif action == 3:
            tar_row, tar_col = player.move_target('s')
        elif action == 4:
            tar_row, tar_col = player.get_position()
            if grid.is_food(tar_row, tar_col):
                player.set_score(10)
                grid.remove_food(tar_row, tar_col)
            else:
                player.set_score(-5)
        
        if grid.food_grid[tar_row][tar_col] == 2:
            player.set_score(-15)
        else:
            player.set_position(tar_row, tar_col)
    
    def update(self, player:Player, grid:Grid):
        self.act(player, grid)
        grid.player_turtle.clear()
        grid.food_turtle.clear()
        #grid.draw_grid()
        grid.draw_food()
        grid.draw_player(player)


class RunHandler:
    def __init__(self, player_handler:PlayerHandler):
        self.player_handler = player_handler
        self.grid = Grid()

    def single_run(self, player:Player):
        self.grid.clear_grid()
        self.grid.add_food(10)
        self.grid.draw_grid()
        self.grid.draw_food()
        player.set_position(1,1)
        self.grid.draw_player(player)
        steps = 10
        while steps > 0:
            self.grid.screen.ontimer(self.player_handler.update(player, self.grid), 50)
            steps -= 1
        print('Run')
        return player.get_score()
    
    def multi_run(self, player, number):
        avg_score = 0
        for i in range(number):
            avg_score += self.single_run(player)
        print('set')
        return avg_score
