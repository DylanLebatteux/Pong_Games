# Import
import os
import turtle
import simpleaudio as sa

# Screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.tracer()

# Score
score_A = 0
score_B = 0

# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_A.color("white")
paddle_A.penup()
paddle_A.goto(-350, 0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_B.color("white")
paddle_B.penup()
paddle_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0        Player B : 0", align="center", font=("Courrier", 24, "normal"))

# Functions
def paddle_A_Up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_Down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_B_Up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_B_Down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

# Keyboard binding
screen.listen()
screen.onkeypress(paddle_A_Up, "w")
screen.onkeypress(paddle_A_Down, "s")
screen.onkeypress(paddle_B_Up, "Up")
screen.onkeypress(paddle_B_Down, "Down")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        sa.WaveObject.from_wave_file('bounce.wav').play()

	# Border checking bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        sa.WaveObject.from_wave_file('bounce.wav').play()

	# Border checking right
    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A : {}        Player B : {}".format(score_A, score_B), align="center", font=("Courrier", 24, "normal"))

	# Border checking left
    if ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A : {}        Player B : {}".format(score_A, score_B), align="center", font=("Courrier", 24, "normal"))

    # Paddles and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_A.ycor() + 50 and ball.ycor() > paddle_A.ycor() - 50:
        ball.dx *= -1
        sa.WaveObject.from_wave_file('bounce.wav').play()
    elif ball.xcor() > 340 and ball.ycor() < paddle_B.ycor() + 50 and ball.ycor() > paddle_B.ycor() - 50:
        ball.dx *= -1
        sa.WaveObject.from_wave_file('bounce.wav').play()
