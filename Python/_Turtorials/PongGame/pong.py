import turtle
import time
wn = turtle.Screen()
wn.title("Pong by Tulan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score

score_a = 0
score_b = 0

#wisual
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0,0)
#How fast move ball (2px if 2)
ball.dx = 0.2
ball.dy = 0.2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


#Function

def paddle_a_up():
  y = paddle_a.ycor()
  if paddle_a.ycor() < 241 and paddle_a.ycor() > -241:
      y += 20
      paddle_a.sety(y)
  elif paddle_a.ycor() > 241:
      paddle_a.sety(240)
  elif paddle_a.ycor() < -241:
      paddle_a.sety(-240)


def paddle_a_down():
  y = paddle_a.ycor()
  if paddle_a.ycor() < 241 and paddle_a.ycor() > -241:
      y -= 20
      paddle_a.sety(y)
  elif paddle_a.ycor() > 241:
      paddle_a.sety(240)
  elif paddle_a.ycor() < -241:
      paddle_a.sety(-240)

def paddle_b_up():
    y = paddle_b.ycor()
    if paddle_b.ycor() < 241 and paddle_b.ycor() > -241:
        y += 20
        paddle_b.sety(y)
    elif paddle_b.ycor() > 241:
        paddle_b.sety(240)
    elif paddle_b.ycor() < -241:
        paddle_b.sety(-240)

def paddle_b_down():
    y = paddle_b.ycor()
    if paddle_b.ycor() < 241 and paddle_b.ycor() > -241:
        y -= 20
        paddle_b.sety(y)
    elif paddle_b.ycor() > 241:
        paddle_b.sety(240)
    elif paddle_b.ycor() < -241:
        paddle_b.sety(-240)

#Keyboard
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#main loop
while True:
    wn.update()

    #ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        paddle_a.goto(-350,0)
        paddle_b.goto(350,0)
        ball.dx *= -1
        time.sleep(0.5)

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        paddle_a.goto(-350,0)
        paddle_b.goto(350,0)
        ball.dx *= -1
        time.sleep(0.5)

  #Collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
      ball.dx *= -1

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
      ball.dx *= -1
