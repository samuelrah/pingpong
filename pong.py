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
bollen.dx = 5
bollen.dy = 5

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

# Spelarkontroller
def spelfigur1_upp():
    y = spelfigur1.ycor()
    if y < 250:
        spelfigur1.sety(y + 20)

def spelfigur1_ned():
    y = spelfigur1.ycor()
    if y > -250:
        spelfigur1.sety(y - 20)

def spelfigur2_upp():
    y = spelfigur2.ycor()
    if y < 250:
        spelfigur2.sety(y + 20)

def spelfigur2_ned():
    y = spelfigur2.ycor()
    if y > -250:
        spelfigur2.sety(y - 20)

screen.listen()
screen.onkey(spelfigur1_upp, "w")
screen.onkey(spelfigur1_ned, "s")
screen.onkey(spelfigur2_upp, "Up")
screen.onkey(spelfigur2_ned, "Down")

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

    # Bollen passerar vänster sida
    if bollen.xcor() < -390:
        bollen.goto(0, 0)
        bollen.dx *= -1
        r_score += 1
        right_score.clear()
        right_score.write(r_score, align="center", font=("Courier", 80, "normal"))


# Vänta på klick för att avsluta
screen.exitonclick()

