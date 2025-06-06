from turtle import Screen, Turtle
import time

# Skapa skärmen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Slå av automatisk uppdatering

# Skapa spelare 1 (vänster)
spelfigur1 = Turtle()
spelfigur1.shape("square")
spelfigur1.shapesize(stretch_wid=5, stretch_len=1)
spelfigur1.color("white")
spelfigur1.penup()
spelfigur1.goto(-380, 0)

# Skapa spelare 2 (höger)
spelfigur2 = Turtle()
spelfigur2.shape("square")
spelfigur2.shapesize(stretch_wid=5, stretch_len=1)
spelfigur2.color("white")
spelfigur2.penup()
spelfigur2.goto(380, 0)

# Skapa bollen
bollen = Turtle()
bollen.shape("circle")
bollen.color("white")
bollen.penup()
bollen.goto(0, 0)
bollen.dx = 7
bollen.dy = 7

# Poängsystem
l_score = 0
r_score = 0

left_score = Turtle()
left_score.color("white")
left_score.penup()
left_score.hideturtle()
left_score.goto(-100, 200)
left_score.write(l_score, align="center", font=("Courier", 80, "normal"))

right_score = Turtle()
right_score.color("white")
right_score.penup()
right_score.hideturtle()
right_score.goto(100, 200)
right_score.write(r_score, align="center", font=("Courier", 80, "normal"))

# Kontrollflaggor för rörelse
spelfigur1_up_pressed = False
spelfigur1_down_pressed = False
spelfigur2_up_pressed = False
spelfigur2_down_pressed = False

def spelfigur1_upp_press():
    global spelfigur1_up_pressed
    spelfigur1_up_pressed = True

def spelfigur1_upp_release():
    global spelfigur1_up_pressed
    spelfigur1_up_pressed = False

def spelfigur1_ned_press():
    global spelfigur1_down_pressed
    spelfigur1_down_pressed = True

def spelfigur1_ned_release():
    global spelfigur1_down_pressed
    spelfigur1_down_pressed = False

def spelfigur2_upp_press():
    global spelfigur2_up_pressed
    spelfigur2_up_pressed = True

def spelfigur2_upp_release():
    global spelfigur2_up_pressed
    spelfigur2_up_pressed = False

def spelfigur2_ned_press():
    global spelfigur2_down_pressed
    spelfigur2_down_pressed = True

def spelfigur2_ned_release():
    global spelfigur2_down_pressed
    spelfigur2_down_pressed = False

def move_paddles():
    if spelfigur1_up_pressed:
        y = spelfigur1.ycor()
        if y < 250:
            spelfigur1.sety(y + 20)
    if spelfigur1_down_pressed:
        y = spelfigur1.ycor()
        if y > -250:
            spelfigur1.sety(y - 20)
    if spelfigur2_up_pressed:
        y = spelfigur2.ycor()
        if y < 250:
            spelfigur2.sety(y + 20)
    if spelfigur2_down_pressed:
        y = spelfigur2.ycor()
        if y > -250:
            spelfigur2.sety(y - 20)
    screen.ontimer(move_paddles, 30)

screen.listen()
screen.onkeypress(spelfigur1_upp_press, "w")
screen.onkeyrelease(spelfigur1_upp_release, "w")
screen.onkeypress(spelfigur1_ned_press, "s")
screen.onkeyrelease(spelfigur1_ned_release, "s")
screen.onkeypress(spelfigur2_upp_press, "Up")
screen.onkeyrelease(spelfigur2_upp_release, "Up")
screen.onkeypress(spelfigur2_ned_press, "Down")
screen.onkeyrelease(spelfigur2_ned_release, "Down")

move_paddles()

# Spelloop
game_is_on = True

while game_is_on:
    time.sleep(0.03)
    screen.update()

    # Flytta bollen
    bollen.setx(bollen.xcor() + bollen.dx)
    bollen.sety(bollen.ycor() + bollen.dy)

    # Kollision med väggar
    if bollen.ycor() > 290 or bollen.ycor() < -290:
        bollen.dy *= -1

    # Bollen passerar höger sida
    if bollen.xcor() > 390:
        bollen.goto(0, 0)
        bollen.dx *= -1
        l_score += 1
        left_score.clear()
        left_score.write(l_score, align="center", font=("Courier", 80, "normal"))
        if l_score == 10:
            winner = Turtle()
            winner.hideturtle()
            winner.color("yellow")
            winner.penup()
            winner.goto(0, 0)
            winner.write("Vänster spelare vinner!", align="center", font=("Courier", 36, "bold"))
            game_is_on = False

    # Bollen passerar vänster sida
    if bollen.xcor() < -390:
        bollen.goto(0, 0)
        bollen.dx *= -1
        r_score += 1
        right_score.clear()
        right_score.write(r_score, align="center", font=("Courier", 80, "normal"))
        if r_score == 10:
            winner = Turtle()
            winner.hideturtle()
            winner.color("yellow")
            winner.penup()
            winner.goto(0, 0)
            winner.write("Höger spelare vinner!", align="center", font=("Courier", 36, "bold"))
            game_is_on = False

    # Kollision med spelare 2
    if bollen.distance(spelfigur2) < 50 and bollen.xcor() > 360:
        bollen.dx *= -1

    # Kollision med spelare 1
    if bollen.distance(spelfigur1) < 50 and bollen.xcor() < -360:
        bollen.dx *= -1

# Vänta på klick för att avsluta
screen.exitonclick()