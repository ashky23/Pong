import turtle  
import os
import time
wn=turtle.Screen()
wn.title("Pong By @Ashky")
wn.bgcolor("skyblue")
wn.setup(width=800,height=600)
wn.tracer(0)


#score
score_a=0
score_b=0

#bool value to check if one should end the game or not
end_game=False

#mid-line
m_l = turtle.Turtle()
m_l.speed(0)
m_l.shape("square")
m_l.color("blue")
m_l.shapesize(stretch_len=0.01,stretch_wid=30)
m_l.penup()
m_l.goto(0,0)

#Paddle A
p_a = turtle.Turtle()
p_a.speed(0)
p_a.shape("square")
p_a.color("blue")
p_a.shapesize(stretch_len=1,stretch_wid=5)
p_a.penup()
p_a.goto(-350,0)

#Paddle B
p_b = turtle.Turtle()
p_b.speed(0)
p_b.shape("square")
p_b.color("blue")
p_b.shapesize(stretch_len=1,stretch_wid=5)
p_b.penup()
p_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
# ball.shapesize(stretch_len=1,stretch_wid=5)
ball.penup()
ball.goto(0,0)
ball.dx =0.2
ball.dy =0.2

#score_tab
tab=turtle.Turtle()
tab.speed(0)
tab.color("gray")
tab.penup()
tab.hideturtle()
tab.goto(0,260)
tab.write("Player A: 0     Player B: 0",align="center", font=("Courier",22,"normal"))


#whowins
win=turtle.Turtle()
win.speed()
win.color("Red")
win.penup()
win.hideturtle()
win.goto(0,0)

## Function 

def p_a_up():
    y=p_a.ycor()
    y+=20
    if y>250:
        y=250
    p_a.sety(y)

def p_a_down():
    y=p_a.ycor()
    y-=20
    if y<-250:
        y=-250
    p_a.sety(y)

def p_b_up():
    y=p_b.ycor()
    y+=20
    if y>250:
        y=250
    p_b.sety(y)

def p_b_down():
    y=p_b.ycor()
    y-=20
    if y<-250:
        y=-250
    p_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(p_a_up,"w")
wn.onkeypress(p_a_down,"s")
wn.onkeypress(p_b_up,"Up")
wn.onkeypress(p_b_down,"Down")


while True:
    # ball.dx+=0.001
    # ball.dy+=0.001
    wn.update()
    
    #ball movement
    ball.setx( ball.xcor() + ball.dx )
    ball.sety( ball.ycor() + ball.dy )
    

    #walls reflection
    #top and bottom
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        os.system("aplay bounce.wav&") 
        #aplay is used in linux and afplay is used in mac , without & there is a stopping of a game for a while so one should use &
        #for windows
        #import winsound
        #winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    elif ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&") 
    #left and right
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        # os.system("aplay bounce.wav&") ##Sound Play for right side wall .....not using right now:
    elif ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx*=-1
        #os.system("aplay bounce.wav&") ##Sound Play for right side wall .....not using right now:
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor()<p_b.ycor()+40 and ball.ycor()>p_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
        os.system("aplay paddle.wav&") 
        score_b+=1
        

        
        tab.clear()
        tab.write("Player A: {}     Player B: {}".format(score_a,score_b),align="center", font=("Courier",22,"normal"))

    if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor()<p_a.ycor()+40 and ball.ycor()>p_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
        os.system("aplay paddle.wav&") 
        score_a+=1
        tab.clear()
        tab.write("Player A: {}     Player B: {}".format(score_a,score_b),align="center", font=("Courier",22,"normal"))

    if score_a>5 or score_b>5:
        if (score_a - score_b) >=2:
            print("clearA")
            m_l.clear()
            win.write("Player A wins! Hurray", align="center", font=("Courier",22,"normal"))
            end_game=True
        elif (score_b-score_a)>=2:
            print("clearB")
            m_l.clear()
            win.write("Player B wins! Hurray", align="center", font=("Courier",22,"normal"))
            end_game=True
        if end_game:
            time.sleep(10)
            break

