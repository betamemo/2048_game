from turtle import Turtle, Screen

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
        self.tiles = [
            [0, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 4],
            [0, 0, 0, 0]
        ]
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
        # test
        print(self.tiles)

        self.draw_tiles()
        self.screen.update()

    def get_num(self, l):
        return [i for i in l if i > 0]

    def get_zero(self, l):
        return [i for i in l if i == 0]

    def move_left(self):
        for i in range(len(self.tiles)):
            self.tiles[i] = self.get_num(self.tiles[i]) + self.get_zero(self.tiles[i])

    def move_right(self):
        for i in range(len(self.tiles)):
            self.tiles[i] = self.get_zero(self.tiles[i]) + self.get_num(self.tiles[i])

    def go_left(self):

        # move
        self.move_left()

        # merge
        # for x in range(len(self.tiles)):
        #     for y in range(len(self.new_tiles[x]) - 1):
        #         if self.new_tiles[x][y] > 0 and self.new_tiles[x][y] == self.new_tiles[x][y + 1]:
        #             self.new_tiles[x][y] += self.new_tiles[x][y + 1]
        #             self.new_tiles[x][y + 1] = 0

        # display
        self.update_tiles()


screen = Screen()
screen.setup(500, 500)
screen.tracer(0)

board = Board(screen)

screen.listen()
# screen.onkeypress(fun=board.go_up, key='Up')
# screen.onkeypress(fun=board.go_down, key='Down')
screen.onkeypress(fun=board.go_left, key='Left')
# screen.onkeypress(fun=board.go_right, key='Right')

screen.update()

screen.exitonclick()
