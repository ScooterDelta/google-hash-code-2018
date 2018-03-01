class Pos:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def distance_to(self, pos):
        abs(self.row - pos.row) + abs(self.column - pos.column)
