import turtle

win = turtle.Screen()
pad1 = turtle.Turtle()
pad2 = turtle.Turtle()
ball = turtle.Turtle()
score = turtle.Turtle()

def window():
    win.title("Ping Pong Game")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(10)
window()

def paddle_1():
    pad1.speed(0)
    pad1.shape("square")
    pad1.color("red")
    pad1.shapesize(stretch_wid=6, stretch_len=1)
    pad1.penup()
    pad1.goto(-360, 0)
paddle_1()

def paddle_2():
    pad2.speed(0)
    pad2.shape("square")
    pad2.color("blue")
    pad2.shapesize(stretch_wid=6, stretch_len=1)
    pad2.penup()
    pad2.goto(360, 0)
paddle_2()

def ballon():
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    # ball.shapesize(stretch_wid=1, stretch_len=1)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.3
    ball.dy = 0.2
ballon()

def scoreup():
    score.speed(0)
    score.color("yellow")
    score.penup()
    score.hideturtle()
    score.goto(0, 270)
    score.write(f"--- Player Red: < 00 >  |  < 00 > :Blue Player ---", align="center", font=("Courier", 12, "normal"))
scoreup()

def paddle_1_up():
    y = pad1.ycor()
    y += 15
    pad1.sety(y)
win.listen()
win.onkeypress(paddle_1_up, "z")

def paddle_1_down():
    y = pad1.ycor()
    y -= 15
    pad1.sety(y)
win.listen()
win.onkeypress(paddle_1_down, "s")

def paddle_2_up():
    y = pad2.ycor()
    y += 15
    pad2.sety(y)
win.listen()
win.onkeypress(paddle_2_up, "Up")

def paddle_2_down():
    y = pad2.ycor()
    y -= 15
    pad2.sety(y)
win.listen()
win.onkeypress(paddle_2_down, "Down")
# -------------
sPlayer1 = 0
sPlayer2 = 0
while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >=290:
        ball.sety(290)
        ball.dy = ball.dy * -1
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
    
    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        sPlayer1 += 1
        score.clear()
        score.write(f"--- Player Red: < {str(sPlayer1).zfill(2)} >  |  < {str(sPlayer2).zfill(2)} > :Blue Player ---", align="center", font=("Courier", 12, "normal"))
    
    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        sPlayer2 += 1
        score.clear()
        score.write(f"--- Player Red: < {str(sPlayer1).zfill(2)} >  |  < {str(sPlayer2).zfill(2)} > :Blue Player ---", align="center", font=("Courier", 12, "normal"))

    if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < pad2.ycor() + 50 and ball.ycor() > pad2.ycor() -50):
        ball.setx(350)
        ball.dx = ball.dx * -1
    
    if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < pad1.ycor() + 50 and ball.ycor() > pad1.ycor() -50):
        ball.setx(-350)
        ball.dx = ball.dx * -1