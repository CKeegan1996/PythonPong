#Simple Pong

import turtle
import winsound

#This section creates the window information
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #this stops window from auto updating, must be done manually

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #set speed of animation (required for turtle. Maximum speed)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #strech to right size
paddle_a.penup()
paddle_a.goto(-350, 0) #sets starting location for paddle

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #set speed of animation (required for turtle. Maximum speed)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) #sets starting location for paddle (-350 changed to +350 for opposite side

#Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4 #dx is delta/change. X coord, move by 2px, now 0.4 #play with this
ball.dy = 0.4

#Pen
pen = turtle.Turtle() #small t for module, captial for class name
pen.speed(0) #animation speed
pen.color("white")
pen.penup() #pen up to prevent a line showing between points
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#counter
counter = 0

#Functions
def paddle_a_up(): #def defines function
    y = paddle_a.ycor() #paddle a = name of object, .ycor method is from turtle, returns y coord. sets to variable
    y += 20 #adds 20px to y coord
    paddle_a.sety(y) #updates the y coord

def paddle_a_down(): 
    y = paddle_a.ycor() 
    y -= 20 
    paddle_a.sety(y)
    
def paddle_b_up(): 
    y = paddle_b.ycor() 
    y += 20 
    paddle_b.sety(y) 

def paddle_b_down(): 
    y = paddle_b.ycor() 
    y -= 20 
    paddle_b.sety(y)
    
def quit_game():
    quit()

def win():
    pen.clear()
    pen.write("GAME OVER!", align="center", font=("Courier", 24, "normal"))
    ball.dx = 0
    ball.dy = 0
    pen.goto(0,-200)
    pen.write("Final Score:", align="center", font=("Courier", 24, "normal"))
    pen.goto(0,-275)
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
#Keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #when the user presses w (lowercase), call function
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") #Up capitalised means arrow keys
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(quit_game, "q")
    
#main game loop
while True:
    wn.update() #updates screen when loops run

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border checking
    #Top
    if ball.ycor() > 290: #compare borders y cor against height of window
        ball.sety(290)
        ball.dy *= -1 #reverses direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
     #bottom   
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    #right
    if ball.xcor() > 390:
        ball.setx(0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    #left
    if ball.xcor() < -390:
        ball.setx(0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #paddle collision with border
    #new
    if paddle_a.ycor() > 250: 
        paddle_a.sety(250)

    if paddle_a.ycor() < -250: 
        paddle_a.sety(-250)    

    if paddle_b.ycor() > 250: 
        paddle_b.sety(250)
        
    if paddle_b.ycor() < -250: 
        paddle_b.sety(-250)


    #Paddle and Ball Collision
        #if the ball is touching the edge of the paddles x coord, and between the coords of the paddle as a whole
        #send in reverse direction,
    if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40)):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40)):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    ##Win Condition
    if counter == 0 and (score_a == 10 or score_b == 10):
        win();
        counter = 1
