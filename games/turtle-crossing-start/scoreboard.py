from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.create_score()

    def create_score(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.create_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)
