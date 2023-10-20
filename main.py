from turtle import Screen

from board import Board

screen = Screen()
screen.setup(500, 500)
screen.tracer(0)

board = Board(screen)

screen.listen()
# screen.onkeypress(fun=board.go_up, key='Up')
# screen.onkeypress(fun=board.go_down, key='Down')
screen.onkeypress(fun=board.go_left, key='Left')
screen.onkeypress(fun=board.go_right, key='Right')

screen.update()

screen.exitonclick()
