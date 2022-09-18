# IMPORTY MODULE TURTLE
import turtle

wind = turtle.Screen()
wind.bgcolor("black")
wind.title("PING PONG BY MOHAMED")
wind.setup(width=800 , height=600)
wind.tracer(0)

# MADRAP 1
madrap1 = turtle.Turtle()
madrap1.speed(0)
madrap1.shape("square")
madrap1.color("blue")
madrap1.shapesize(stretch_wid=5 , stretch_len=1)
madrap1.penup()
madrap1.goto(-350,0)

# MADRAP 2
madrap2 = turtle.Turtle()
madrap2.speed(0)
madrap2.shape("square")
madrap2.color("red")
madrap2.shapesize(stretch_wid = 5 , stretch_len = 1)
madrap2.penup()
madrap2.goto(350,0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5
# SCORE
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.hideturtle()
score.goto(0,260)
score.write("Player 1 : 0 VS Player 2 : 0" , align = "center" , font =("courier" , 24 , "normal"))
# FUNCTIONS OF ACTION
def madrap1_up():
    y = madrap1.ycor()
    y += 20
    madrap1.sety(y)

def madrap1_down():
    y = madrap1.ycor()
    y -= 20
    madrap1.sety(y)

def madrap2_up():
    y = madrap2.ycor()
    y += 20
    madrap2.sety(y)


def madrap2_down():
    y = madrap2.ycor()
    y -= 20
    madrap2.sety(y)

# KEYBOARD BLINDING
wind.listen()
wind.onkeypress(madrap1_up , "w")
wind.onkeypress(madrap1_down , "s")
wind.onkeypress(madrap2_up , "Up")
wind.onkeypress(madrap2_down , "Down")

while True :
    wind.update()
    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor() + ball.dy )
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390 :
        ball.setx(390)
        ball.dx *= -1
    
    if ball.xcor() < -390 :
        ball.setx(-390)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1 : {score1} VS Player 2 : {score2} " , align = "center" , font =("courier" , 24 , "normal"))

        
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor()< madrap2.ycor() +40 and ball.ycor() > madrap2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1 : {score2} VS Player 2 : {score2} " , align = "center" , font =("courier" , 24 , "normal"))

        
    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor()< madrap1.ycor() +40 and ball.ycor() > madrap1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
