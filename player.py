import constants as c

class Player:
    def __init__(self, genes):
        self.genes = genes
        self.pos_row = 0
        self.pos_col = 0
        self.score = 0

    def move_target(self, direction:str):
        if direction == 'n':
            return self.pos_row - 1, self.pos_col
        if direction == 'w':
            return self.pos_row, self.pos_col - 1
        if direction =='e':
            return self.pos_row, self.pos_col + 1
        if direction == 's':
            return self.pos_row + 1, self.pos_col

    def set_position(self, tar_row, tar_col):
        self.pos_row = tar_row
        self.pos_col = tar_col
        print(f'Move to {self.pos_row}, {self.pos_col}')

    def get_position(self):
        return self.pos_row, self.pos_col

    def set_score(self, inc_score):
        self.score += inc_score

    def get_score(self):
        return self.score