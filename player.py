import constants as c

class Player:
    def __init__(self, genes):
        self.genes = genes
        self.pos_row = 0
        self.pos_col = 0
        self.score = 0

    def set_position(self, inc_row, inc_col):
        self.pos_row += inc_row
        self.pos_col += inc_col
    
    def get_position(self):
        return self.pos_row, self.pos_col

    def set_score(self, inc_score):
        self.score += inc_score

    def get_score(self):
        return self.score