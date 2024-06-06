import turtle
import random

bob = turtle.Turtle()

points = 0
lives = 3


#ax definitions ax de antexo
def Italy():
    bob.penup()

    bob.goto(-300, 100)

    bob.pendown()
    bob.pencolor("green")

    bob.fillcolor("green")
    bob.begin_fill()
    for green in range(2):
        bob.fd(50)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
    bob.end_fill()

    bob.penup()
    bob.goto(-200, 100)

    bob.pendown()
    bob.pencolor("red")
    bob.fillcolor("red")
    bob.begin_fill()
    for red in range(2):
        bob.fd(50)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
    bob.end_fill()

def France():
    bob.penup()

    bob.goto(-300, 100)

    bob.pendown()
    bob.pencolor("blue")

    bob.fillcolor("blue")
    bob.begin_fill()
    for green in range(2):
        bob.fd(50)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
    bob.end_fill()

    bob.penup()
    bob.goto(-200, 100)

    bob.pendown()
    bob.pencolor("red")
    bob.fillcolor("red")
    bob.begin_fill()
    for red in range(2):
        bob.fd(50)
        bob.lt(90)
        bob.fd(100)
        bob.lt(90)
    bob.end_fill()

def Germany():
    bob.penup()

    bob.goto(-200, 200)

    bob.pendown()
    bob.pencolor("black")

    bob.fillcolor("black")
    bob.begin_fill()
    for black in range(2):
        bob.fd(120)
        bob.lt(90)
        bob.fd(35)
        bob.lt(90)
    bob.end_fill()

    bob.pendown()
    bob.pencolor("red")

    bob.fillcolor("red")
    bob.begin_fill()
    for red in range(2):
        bob.fd(120)
        bob.rt(90)
        bob.fd(35)
        bob.rt(90)
    bob.end_fill()


    bob.penup()
    bob.goto(-200,165)
    bob.pendown()
    bob.pencolor("yellow")

    bob.fillcolor("yellow")
    bob.begin_fill()
    for yellow in range(2):
        bob.fd(120)
        bob.rt(90)
        bob.fd(35)
        bob.rt(90)
    bob.end_fill()

def Finland():
    bob.penup()

    bob.goto(-200, 200)

    bob.pendown()

    for border in range(2):
        bob.fd(200)
        bob.rt(90)
        bob.fd(100)
        bob.rt(90)

    bob.fd(70)

    bob.pendown()
    bob.fillcolor("blue")
    bob.pencolor("blue")
    bob.begin_fill()
    for finlandkato in range(2):
        bob.rt(90)
        bob.fd(100)
        bob.rt(90)
        bob.fd(35)

    bob.end_fill()

    bob.penup()
    bob.fd(130)
    bob.rt(90)
    bob.fd(55)

    bob.pendown()
    bob.begin_fill()
    for finlandrizz in range(2):
        bob.rt(90)
        bob.fd(200)
        bob.rt(90)
        bob.fd(25)
    bob.end_fill()

def Poland():
    bob.penup()

    bob.goto(-200, 200)

    bob.pendown()
    bob.pencolor("white")

    for quegtr in range(2):
        bob.fd(100)
        bob.lt(90)
        bob.fd(50)
        bob.lt(90)


    bob.pendown()
    bob.pencolor("red")

    bob.fillcolor("red")
    bob.begin_fill()
    for demporo in range(2):
        bob.fd(120)
        bob.rt(90)
        bob.fd(35)
        bob.rt(90)
    bob.end_fill()

    bob.pencolor("black")

    bob.lt(90)
    bob.fd(30)
    bob.rt(90)
    bob.fd(120)
    bob.rt(90)
    bob.fd(65)
    bob.rt(90)
    bob.fd(120)
    bob.rt(90)
    bob.fd(35)

def UAE():
    bob.penup()

    bob.goto(-300, 100)

    bob.pendown()
    bob.pencolor("red")

    bob.fillcolor("red")
    bob.begin_fill()
    for green in range(2):
        bob.fd(50)
        bob.lt(90)
        bob.fd(105)
        bob.lt(90)
    bob.end_fill()

    bob.penup()

    bob.fd(50)
    bob.lt(90)
    bob.fd(105)
    bob.rt(90)

    bob.pendown()
    bob.pencolor("green")

    bob.fillcolor("green")
    bob.begin_fill()
    for black in range(2):
        bob.fd(120)
        bob.rt(90)
        bob.fd(35)
        bob.rt(90)
    bob.end_fill()

    bob.rt(90)
    bob.fd(35)
    bob.lt(90)
    bob.pendown()
    bob.pencolor("white")

    bob.fillcolor("white")
    bob.begin_fill()
    for red in range(2):
        bob.fd(120)
        bob.rt(90)
        bob.fd(35)
        bob.rt(90)
    bob.end_fill()

    bob.penup()

    bob.rt(90)
    bob.fd(35)
    bob.lt(90)

    bob.pendown()
    bob.pencolor("black")

    bob.fillcolor("black")
    bob.begin_fill()
    for yellow in range(2):
        bob.fd(120)
        bob.rt(90)
        bob.fd(35)
        bob.rt(90)
    bob.end_fill()





#lista ton flags
flags = [Italy,France,Germany,Finland,Poland,UAE]


while lives>0 and len(flags) > 0:
    bob.reset()
    bob.speed(200)
    flag = random.choice(flags)
    flag()
    answer = input("Guess the flag")

    if answer == flag.__name__ :
        print("CORRECT!!!")
        points = points + 100
        print("STATUS:")
        print("Points:",points)
        print("Lives:",lives)
        flags.remove(flag)

    else:
        print("WRONG AWNSER, U DON GOOFED UP")
        if points>0:
            points = points - 100
        else:
            points = 0
        lives = lives - 1
        print("STATUS:")
        print("Points:", points)
        print("Lives:", lives)
        flags.remove(flag)

if points > 399:
    print("POINTS:", points, "/400 MINIMUM")
    print("YOU WIN!!")
else:
    print("POINTS:", points, "/400 MINIMUM")
    print("NOT ENOUGH POINTS...")
    print("GAME OVER")
