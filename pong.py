import turtle
import time

# Skapa fönster
win = turtle.Screen()
win.title("Pong med Turtle")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Poäng
score_a = 0
score_b = 0
