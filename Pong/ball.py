from turtle import Turtle, Screen

class Ball(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        
            
    def move(self):
        self.goto(x=self.xcor() + 10, y=self.ycor() + 10)