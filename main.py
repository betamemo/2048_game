class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = self.create_board(row, col)
        self.new_board = []

    def __str__(self):
        s = ''
        for row in self.board:
            s += ''.join([str(i) if i > 0 else '.' for i in row])
            s += '\n'
        return s

