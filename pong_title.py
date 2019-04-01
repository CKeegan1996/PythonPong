#Pong Title Screen
import turtle


wn = turtle.Screen()
wn.title("PongTitle")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) 

pen = turtle.Turtle() #small t for module, captial for class name
pen.speed(0) #animation speed
pen.color("white")
pen.penup() #pen up to prevent a line showing between points
pen.hideturtle()

pen.goto(0,50)
pen.write("PONG", align="center", font=("Courier", 60, "normal"))
pen.goto(-200,-20)

pen.write("CONTROLS:", align="center", font=("Courier", 30, "normal"))
pen.goto(40,-60)

pen.write("Player 1: Up - W", align="center", font=("Courier", 15, "normal"))
pen.goto(130,-90)
pen.write("Down - S", align="center", font=("Courier", 15, "normal"))


pen.goto(90,-130)
pen.write("Player 2: Up - Up Arrow", align="center", font=("Courier", 15, "normal"))
pen.goto(195,-160)
pen.write("Down - Down Arrow", align="center", font=("Courier", 15, "normal"))

pen.goto(0,-270)
pen.write("Press S to Start", align="center", font=("Courier", 25, "normal"))

pen.goto(0,-290)
pen.write("Press Q to Quit", align="center", font=("Courier", 15, "normal"))


#Functions
def start_game():
    pen.clear()
    import pong

def quit_game():
    quit()

#Keyboard binding
wn.listen() 
wn.onkeypress(start_game, "s")
wn.onkeypress(quit_game, "q")

counter = 0

while True:
    wn.update()
