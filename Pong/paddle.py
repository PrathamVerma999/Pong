from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.setpos(position)
        self.up()
        self.down()
        
    def up(self):
        new_ycor = self.ycor() + 20
        self.setpos(x=self.xcor(), y=new_ycor)
    
    def down(self):
        new_ycor = self.ycor() - 20
        self.setpos(x=self.xcor(), y=new_ycor)
        