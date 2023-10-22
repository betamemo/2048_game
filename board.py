import random
from turtle import Turtle, Screen

FONT = ('verdana', 30, 'normal')
STARTING_X = -120
STARTING_Y = 100
SPACE = 80


class Board():

    def __init__(self, screen, row=4, col=4):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(STARTING_X, STARTING_Y)
        self.screen = screen
        # self.board = [
        #     [0, 2, 2, 2],
        #     [0, 0, 0, 0],
        #     [0, 0, 0, 4],
        #     [0, 0, 0, 0]
        # ]
        self.row = row
        self.col = col
        self.board = self.create_board(row, col)
        self.add_tiles()
        self.draw_tiles()

        self.new_board = []

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

    def draw_tiles(self):
        self.turtle.clear()
        self.turtle.goto(STARTING_X, STARTING_Y)
        for row in self.board:
            for col in row:
                self.turtle.write(f'{col}', align='center', font=FONT)
                self.turtle.goto(self.turtle.xcor() + SPACE, self.turtle.ycor())
            self.turtle.goto(STARTING_X, self.turtle.ycor() - SPACE)

    def update_board(self):
        tmp = self.board
        self.board = self.new_board
        self.new_board = tmp

        self.draw_tiles()
        self.screen.update()

    def move(self, direction):
        self.new_board = []
        for row in self.board:
            while 0 in row:
                row.remove(0)

                # merge
                for i in range(len(row) - 1):
                    if row[i] == row[i + 1]:
                        row[i] *= 2
                        row[i + 1] = 0

            if direction == 'Left':
                while len(row) < self.row:
                    row.append(0)
            elif direction == 'Right':
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

    def go_left(self):
        self.move('Left')

    def go_right(self):
        self.move('Right')

    def go_up(self):
        self.transpose()
        self.move('Left')
        self.transpose()

    def go_down(self):
        self.transpose()
        self.move('Right')
        self.transpose()


screen = Screen()
screen.setup(500, 500)
screen.tracer(0)

board = Board(screen)

screen.listen()
screen.onkeypress(fun=board.go_up, key='Up')
screen.onkeypress(fun=board.go_down, key='Down')
screen.onkeypress(fun=board.go_left, key='Left')
screen.onkeypress(fun=board.go_right, key='Right')

screen.update()

screen.exitonclick()
