import random


class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = self.create_board(row, col)
        self.add_tiles()
        self.new_board = []

    def __str__(self):
        s = ''
        for row in self.board:
            s += ''.join([str(i) if i > 0 else '.' for i in row])
            s += '\n'
        return s

    def create_board(self, row, col):
        board = []
        for i in range(col):
            board.append([0] * row)
        return board

    def add_tiles(self):

        # check empty
        empty = []
        for row in range(self.row):
            for col in range(self.col):
                if self.board[row][col] == 0:
                    empty.append((row, col))

        if empty:
            row, col = random.choice(empty)
            self.board[row][col] = 2

            row, col = random.choice(empty)
            self.board[row][col] = 2

    def update_board(self):
        tmp = self.board
        self.board = self.new_board
        self.new_board = tmp

    def move(self, direction):
        self.new_board = []
        for row in self.board:
            row = [i for i in row if i > 0]

            if direction == 'left':
                for i in range(len(row) - 1):
                    if row[i] == row[i + 1]:
                        row[i] *= 2
                        row[i + 1] = 0

                while len(row) < self.row:
                    row.append(0)

            elif direction == 'right':
                for i in range(len(row) - 1):
                    if row[i] == row[i + 1]:
                        row[i + 1] *= 2
                        row[i] = 0

                while len(row) < self.row:
                    row.insert(0, 0)
            self.new_board.append(row)
        self.update_board()
        # self.random_tiles(self.board)

    def transpose(self):
        self.new_board = []
        for c in range(self.col):
            row = []
            for r in range(self.row):
                row.append(self.board[r][c])
            self.new_board.append(row)
        self.update_board()


board = Board(4, 4)

game_is_on = True
while game_is_on:
    print(board)
    key = input('wasd?: ')
    if key == 'w':  # move up
        board.transpose()
        board.move('left')
        board.transpose()
    elif key == 'a':  # move left
        board.move('left')
    elif key == 's':  # move down
        board.transpose()
        board.move('right')
        board.transpose()
    elif key == 'd':  # move right
        board.move('right')
    elif key == 'q':  # quit
        print('quit')
        game_is_on = False
    else:
        print('invalid key!')
    board.add_tiles()

    # count score
    # game over
