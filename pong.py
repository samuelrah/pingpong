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

# Vänta på klick för att avsluta
screen.exitonclick()

