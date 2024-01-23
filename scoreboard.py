from turtle import Turtle,Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0,275)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score = {self.score} highscore = {self.highscore}",False,align="center",font=('Arial', 15 , 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
            self.score = 0
            self.update_scoreboard()

#    def game_over(self):
#        self.hideturtle()
#        self.goto(0,0)
#        self.write(f"GAME OVER!",False,align="center",font=('Arial', 15 , 'normal'))