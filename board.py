from turtle import Turtle

FONT = ('verdana', 30, 'normal')
STARTING_X = -120
STARTING_Y = 100
SPACE = 80


class Board():

    def __init__(self, screen):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(STARTING_X, STARTING_Y)
        self.screen = screen
        self.tiles = [[]]
        self.tiles = [
            [0, 2, 0, 8],
            [0, 0, 0, 0],
            [0, 0, 0, 4],
            [0, 0, 0, 0]
        ]
        self.new_tiles = []
        self.draw_tiles()

    def draw_tiles(self):
        self.turtle.clear()
        self.turtle.goto(STARTING_X, STARTING_Y)
        for row in self.tiles:
            for col in row:
                self.turtle.write(f'{col}', align='center', font=FONT)
                self.turtle.goto(self.turtle.xcor() + SPACE, self.turtle.ycor())
            self.turtle.goto(STARTING_X, self.turtle.ycor() - SPACE)

    def update_tiles(self):
        # print(self.tiles)
        # print(self.new_tiles)

        tmp = self.tiles
        self.tiles = self.new_tiles
        self.new_tiles = tmp

        self.draw_tiles()
        self.screen.update()

    def go_left(self):
        for row in self.tiles:
            # move
            num = [i for i in row if i > 0]
            zero = [i for i in row if i == 0]
            self.new_tiles.append(num + zero)

        self.update_tiles()
