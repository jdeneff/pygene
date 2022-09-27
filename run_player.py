import turtle as tu
from grid import Grid
from player import Player
from handlers import PlayerHandler, RunHandler
from random import randint
import constants as c


# Test Code
grid = Grid()
handler = PlayerHandler()
runner = RunHandler(handler)

players = []

for i in range(10):
    gene = []
    for i in range(len(handler.sense_matrix)):
        gene.append(randint(0,4))
    player = Player(gene)
    player.set_position(1, 1)
        #randint(1, c.GRID_SIZE - 2), randint(1, c.GRID_SIZE - 2))
    players.append(player)
for item in players:
    print(item.pos_row)
    print(item.pos_col)

scores = []

'''for item in players:
    grid.clear_grid()
    grid.add_food(10)
    steps = 10
    grid.draw_grid()
    grid.draw_food()
    grid.draw_player(item)
    while steps > 0:
        grid.screen.ontimer(handler.update(item, grid), 50) 
        steps -= 1
    scores.append(item.get_score())'''

for entity in players:
    scores.append(runner.multi_run(entity, 5))

print(scores)
best_scores = []
best_players = []
for i in range(4):
    max_val = max(scores)
    max_index = scores.index(max_val)
    best_scores.append(scores.pop(max_index))
    best_players.append(players.pop(max_index))

print(best_players)
print(best_scores)
print(scores)

grid.screen.mainloop()