from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
            
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)
        
    
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9
    
    def bounce_x_l_paddle(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9
 
    def bounce_x_r_paddle(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9
        
    def reset(self):
        self.goto(x=0, y=0)
        self.bounce_x_r_paddle()
        self.move_speed = 0.1