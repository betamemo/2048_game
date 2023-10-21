import random


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

    def create_board(self, row, col):
        board = []
        for i in range(col):
            board.append([0] * row)

        self.add_tiles(board)
        return board

    def add_tiles(self, board):
        # board[random.randint(0, self.row - 1)][random.randint(0, self.col - 1)] = 2
        # board[random.randint(0, self.row - 1)][random.randint(0, self.col - 1)] = 2

        # check empty
        empty = []
        for row in range(self.row):
            for col in range(self.col):
                if board[row][col] == 0:
                    empty.append((row, col))
        print(empty)
        if empty:
            row, col = random.choice(empty)
            board[row][col] = 2

            row, col = random.choice(empty)
            board[row][col] = 2

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

    def transpose(self):
        self.new_board = []
        for c in range(self.col):
            row = []
            for r in range(self.row):
                row.append(self.board[r][c])
            self.new_board.append(row)
        self.update_board()


board = Board(4, 4)
print(board)

game_is_on = True
while game_is_on:
    key = input('wasd?: ')

    if key == 'w':  # move up
        board.transpose()
        board.move('left')
        board.transpose()
        board.add_tiles()
        print(board)
    elif key == 'a':  # move left
        board.move('left')
        print(board)
    elif key == 's':  # move down
        board.transpose()
        board.move('right')
        board.transpose()
        print(board)
    elif key == 'd':  # move right
        board.move('right')
        print(board)
    elif key == 'q':  # quit
        print('quit')
        game_is_on = False
    else:
        print('invalid key!')
