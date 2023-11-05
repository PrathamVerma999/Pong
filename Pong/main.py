from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

paddle = Turtle("square")
paddle.color("white")
paddle.penup()
paddle.turtlesize(stretch_len=1, stretch_wid=5)
paddle.setpos(x=350, y=0)

def up():
    new_ycor = paddle.ycor() + 20
    paddle.setpos(350, new_ycor)

def down():
    new_ycor = paddle.ycor() - 20
    paddle.setpos(350, new_ycor)
    
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")

game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()