from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score = {self.score} High score = {self.highscore}", align=ALLIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High score = {self.highscore}", align=ALLIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore :
            with open("high_score.txt" , "w") as file:
                file.write(str(self.score))
            self.highscore = self.score


            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1

        self.update_scoreboard()
