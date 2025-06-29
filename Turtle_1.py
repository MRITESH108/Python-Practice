import random
from turtle import Turtle, Screen,colormode

colormode(255)
tue = Turtle()
tue.shape("turtle")
tue.pensize(3)
tue.speed()

# for i in range(100):
#     steps = random.randint(5,13)
#     angle = random.choice([0, 90, 180, 270])
#     tue.forward(steps)
#     tue.setheading(angle)
#     tue.color(random.choice(["SlateGray","SeaGreen","wheat"]))


                        # Random colour
# tue.colormode(255)
def color():

    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
    # random_color=(r,g,b)
    # return(random_color)


for _ in range(1000):
    tue.color(color())
    tue.forward(13)
    tue.setheading(random.choice([0,90,180,270]))


screen = Screen()
screen.exitonclick()

