from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

position_x = -375
position_y = 0
segments = []

for i in range(3):
    paddle = Turtle()
    paddle.shape("square")
    paddle.color("white")
    paddle.penup()
    paddle.setpos(position_x, position_y)
    position_y -=20


screen.tracer(0)







game_is_on = True




screen.exitonclick()