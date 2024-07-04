import turtle
import random

win = turtle.Screen()  
win.setup(width=800, height=600)
win.bgcolor('black')
win.tracer(0)
win.title('Breakout Game')

paddle = turtle.Turtle()
paddle.shape('square')
paddle.shapesize(stretch_len=5, stretch_wid=1)
paddle.color('white')
paddle.up()
paddle.goto(0, -270)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.up()
ball.dx = random.choice((-2, -3, -4, 2, 3, 4))  # Adjust the values to decrease the speed
ball.dy = random.choice((-2, -3, -4, 2, 3, 4))  # Adjust the values to decrease the speed


pen = turtle.Turtle()
pen.color('red')
pen.up()
pen.hideturtle()
pen.goto(250,-220)
pen.write('Score: 0', align='center', font=('Courier', 24, 'normal'))

colors = ['red', 'blue', 'green', 'cyan', 'purple', 'yellow', 'orange']
score = 0


def paddle_right():
    if paddle.xcor()<350:
        paddle.setx(paddle.xcor()+50)


def paddle_left():
    if paddle.xcor()>-350:
        paddle.setx(paddle.xcor()-50)


def border_check():
    if ball.ycor()>280:
        ball.dy *= -1
    if ball.xcor()>380 or ball.xcor()<-380:
        ball.dx *= -1


def paddle_check():
    if ball.ycor() -10 <= paddle.ycor()+10 and ball.dy<0:
        if ball.xcor()-10 <= paddle.xcor()+50 and ball.xcor()+10>= paddle.xcor()-50:
            ball.dy *= -1

def falling_block():
    for i in block_list:
        if i.state == 'falling':
            i.shape('circle')
            i.l = i.xcor()-10
            i.r = i.xcor()+10
            i.shapesize(1,1)
            i.goto(i.xcor(),i.ycor()+i.dy)
        
            
        
    
win.listen()
win.onkey(paddle_right, 'Right')
win.onkey(paddle_left, 'Left')


x_list = [-340, -230, -120, -10, 100, 210, 320]
y_list = [280, 255, 230, 205, 180]
block_list = []

for i in x_list:
    for j in y_list:
        block = turtle.Turtle()
        block.shape('square')
        block.shapesize(stretch_len=5, stretch_wid=1)
        block.c = (random.choice(colors))
        block.color(block.c)
        block.up()
        block.goto(i, j)
        block.state = 'ready'
        block.l = block.xcor()-50
        block.r = block.xcor()+50
        block_list.append(block)
    
block_count = len(block_list)

while block_count > 0:
        
    win.update()
    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)
    border_check()
    paddle_check()
    falling_block()
    
    # # Autopilot
    # if ball.xcor()>-350 and ball.xcor()<350:
    #     paddle.setx(ball.xcor())


    if ball.ycor() <= -300:
        ball.goto(0,0)
        if score > 0:
            score -= 1
        pen.clear()
        pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))
        
    # Block collisions:
    for i in block_list:
        if (i.l <= ball.xcor() <= i.r) and (i.ycor()-10 <= ball.ycor() <= i.ycor()+10) and i.state == 'ready':
                ball.dy *= -1
                i.state = 'falling'
                i.dy = -2
                score += 1
                pen.clear()
                paddle.color(i.c)
                pen.clear()
                pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

        if i.ycor()<-320:
            block_list.remove(i)
            block_count = len(block_list)

      

# Game Over
pen.clear()
pen.goto(0,0)
pen.write(f'GAME OVER\nScore: {score}', align='center', font=('Courier', 40, 'normal'))
win.exitonclick()
