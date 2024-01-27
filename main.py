#imported turtle module
import turtle


###################Wind#######################
window= turtle.Screen() #intialize screen
window.title("Ping Pong Tn") #set the title of the window
window.bgpic("background/e.png") #set background color of the window
window.setup(width=800 , height=600) #set resoltution of the window
window.tracer(0) #stop the window from updating automatically
###################Wind#######################


 
#ping1
ping1= turtle.Turtle()
ping1.speed(0)
ping1.shape("square")
ping1.color("blue")
ping1.shapesize(stretch_wid=5 , stretch_len=1)
ping1.penup()
ping1.goto(-350,0)
#ping2
ping2= turtle.Turtle()
ping2.speed(0)
ping2.shape("square")
ping2.color("red")
ping2.shapesize(stretch_wid=5 , stretch_len=1)
ping2.penup()
ping2.goto(350,0)
#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1 #you can chnage the speed
ball.dy = 0.1 #you can chnage the speed

#score
score1= 0
score2 =0
score =turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player1:0 Player2:0" , align="center" , font=("Courier" , 24 ,"normal"))

#blue
def ping1_up():
    y = ping1.ycor()
    y = y+20
    ping1.sety(y)
def ping1_down():
    y = ping1.ycor()
    y = y-20
    ping1.sety(y)

#red
def ping2_up():
    y = ping2.ycor()
    y = y+20
    ping2.sety(y)
def ping2_down():
    y = ping2.ycor()
    y = y-20
    ping2.sety(y)

#key bindings
window.listen()

window.onkeypress(ping1_up, "z")
window.onkeypress(ping1_down, "s")

window.onkeypress(ping2_up, "Up")
window.onkeypress(ping2_down, "Down")
###################################################################

while True:
    window.update() #updates the screen evreytime the ping pong game

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 +=1
        score.clear()
        score.write("Player1 : {} Player2: {}".format(score1 , score2) , align="center" , font=("Courier" , 24 ,"normal"))

    if ball.xcor()  <-390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write("Player1 : {} Player2: {}".format(score1 , score2) , align="center" , font=("Courier" , 24 ,"normal"))
    
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < ping2.ycor() + 40 and ball.ycor() > ping2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < ping1.ycor() + 40 and ball.ycor() > ping1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1


    
