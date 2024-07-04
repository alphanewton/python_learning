from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = -1
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = -1
        self.update_scoreboard()
