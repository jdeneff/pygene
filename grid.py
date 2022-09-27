import turtle as tu
import constants as c
from player import Player
from copy import deepcopy
from random import randint

class Grid:
    def __init__(self):
        self.food_count = 0

        self.zero_grid = []
        for row in range(c.GRID_SIZE):
            zero_row = []
            if row == 0 or row == c.GRID_SIZE - 1:
                for col in range(c.GRID_SIZE):
                    zero_row.append(2)
            else:
                for col in range(c.GRID_SIZE):
                    if col == 0 or col == c.GRID_SIZE - 1:
                        zero_row.append(2)
                    else:
                        zero_row.append(0)
            self.zero_grid.append(zero_row)
        
        self.food_grid = deepcopy(self.zero_grid)

        self.screen = tu.Screen()
        self.screen.setup(c.GRID_PIXELS + c.CELL_PIXELS, c.GRID_PIXELS + c.CELL_PIXELS)
        self.screen.setworldcoordinates(0 - c.CELL_PIXELS, c.GRID_PIXELS + c.CELL_PIXELS, c.GRID_PIXELS + c.CELL_PIXELS, 0 - c.CELL_PIXELS)
        self.screen.tracer(0)
        tu.hideturtle()

        self.grid_turtle = tu.Turtle()
        self.grid_turtle.hideturtle()
        self.grid_turtle.pencolor('gray')
        self.grid_turtle.fillcolor('black')
        self.grid_turtle.pensize(2)
        self.grid_turtle.penup()

        self.food_turtle = tu.Turtle()
        self.food_turtle.hideturtle()
        self.food_turtle.penup()
        
        self.player_turtle = tu.Turtle()
        self.player_turtle.hideturtle()
        self.player_turtle.pencolor('black')
        self.player_turtle.pensize(c.MARGIN)
        self.player_turtle.penup()
        
    def add_food(self, count):
        while self.food_count < count:
            rand_row = randint(0, c.GRID_SIZE - 2)
            rand_col = randint(0,c.GRID_SIZE - 2)
            
            if self.food_grid[rand_row][rand_col] == 0:
                self.food_grid[rand_row][rand_col] = 1
                self.food_count += 1
    
    def is_food(self, row, col):
        if self.food_grid[row][col] == 1:
            return True
        else:
            return False
    
    def remove_food(self, row, col):
        if self.food_grid[row][col] == 1:
            self.food_grid[row][col] = 0
            self.food_count -= 1

    def draw_food(self):
        for row in range(c.GRID_SIZE):
            for col in range(c.GRID_SIZE):
                food_row = row * c.CELL_PIXELS
                food_col = col * c.CELL_PIXELS
                if self.food_grid[row][col] == 1:
                    self.food_turtle.fillcolor('red')
                    self.food_turtle.goto(food_col + c.MARGIN, food_row + c.MARGIN)
                    self.food_turtle.seth(90)
                    self.food_turtle.pd()
                    self.food_turtle.begin_fill()
                    for i in range(4):
                        self.food_turtle.fd(c.CELL_PIXELS - c.MARGIN * 2)
                        self.food_turtle.rt(90)
                    self.food_turtle.end_fill()
                    self.food_turtle.pu()
        self.screen.update()
    
    def draw_line(self, row1, col1, row2, col2):
        self.grid_turtle.goto(col1 * c.CELL_PIXELS, row1 * c.CELL_PIXELS)
        self.grid_turtle.pd()
        self.grid_turtle.goto(col2 * c.CELL_PIXELS, row2 * c.CELL_PIXELS)
        self.grid_turtle.pu()
    
    def draw_grid(self):
        # Draws the grid and walls - they don't change so only need to be drawn once
        for i in range(c.GRID_SIZE + 1):
            self.draw_line(i, 0, i, c.GRID_SIZE)
            self.draw_line(0, i, c.GRID_SIZE, i)
        for row in range(c.GRID_SIZE):
            for col in range(c.GRID_SIZE):
                food_row = row * c.CELL_PIXELS
                food_col = col * c.CELL_PIXELS
                if self.food_grid[row][col] == 2:
                    self.grid_turtle.goto(food_col, food_row)
                    self.grid_turtle.seth(90)
                    self.grid_turtle.pd()
                    self.grid_turtle.begin_fill()
                    for i in range(4):
                        self.grid_turtle.fd(c.CELL_PIXELS)
                        self.grid_turtle.rt(90)
                    self.grid_turtle.end_fill()
                    self.grid_turtle.pu()
        self.screen.update()
    
    def draw_player(self, player:Player):
        pos_row, pos_col = player.get_position()
        self.player_turtle.goto(pos_col * c.CELL_PIXELS, pos_row * c.CELL_PIXELS)
        self.player_turtle.seth(90)
        self.player_turtle.pd()
        for i in range(4):
            self.player_turtle.fd(c.CELL_PIXELS)
            self.player_turtle.rt(90)
        self.player_turtle.pu()
        self.screen.update()

    def update_drawing(self):
        self.

    def clear_grid(self):
        self.food_grid = deepcopy(self.zero_grid)
        self.food_count = 0
        self.player_turtle.clear()
        self.grid_turtle.clear()
        self.food_turtle.clear()
