import random


class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = self.create_board(row, col)
        self.add_tiles()
        self.new_board = []
        self.score = 0

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
            while 0 in row:

                # remove 0 before merge
                row.remove(0)

                # merge
                for i in range(len(row) - 1):
                    if row[i] == row[i + 1]:
                        row[i] *= 2
                        row[i + 1] = 0
                        self.add_score(row[i])

            # add 0 after merge
            if direction == 'left':
                while len(row) < self.row:
                    row.append(0)
            elif direction == 'right':
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

    def add_score(self, score):
        self.score += score

    def game_over(self):
        print('game over')


board = Board(4, 4)

game_is_on = True
while game_is_on:
    print('Score:', board.score)
    print(board)
    key = input('Enter direction (w/a/s/d)?: ')
    key = key.lower()

    # move up
    if key == 'w':
        board.transpose()
        board.move('left')
        board.transpose()
        board.add_tiles()

    # move left
    elif key == 'a':
        board.move('left')
        board.add_tiles()

    # move down
    elif key == 's':
        board.transpose()
        board.move('right')
        board.transpose()
        board.add_tiles()

    # move right
    elif key == 'd':
        board.move('right')
        board.add_tiles()

    # quit game
    elif key == 'q':
        print('Turn off the game. Bye!')
        game_is_on = False

    else:
        print('Invalid key. Please try again.')

    # game over
