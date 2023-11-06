from turtle import Turtle
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    
    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(x=100, y=200)
        self.write(self.r_score, align="center", font=FONT)
        
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    
    def print_score(self):
        self.goto(x=0, y=0)
        if self.l_score == 10:
            self.write("The left player won!", align="center", font=("Courier", 40, "normal"))
        elif self.r_score == 10:
            self.write("The right player won!", align="center", font=("Courier", 40, "normal"))
    