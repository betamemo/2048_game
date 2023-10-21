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
