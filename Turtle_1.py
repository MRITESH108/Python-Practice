from turtle import Turtle, Screen

tue = Turtle()
tue.shape("turtle")

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        tue.color(c)
        tue.forward(steps)
        tue.right(90)

screen = Screen()
screen.exitonclick()
