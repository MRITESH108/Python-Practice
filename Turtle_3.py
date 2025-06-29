import colorgram
import turtle
import random

from Turtle_1 import screen

tue = turtle.Turtle()




colors=colorgram.extract('hirstpaint.jpg', 50)
# print(colors)



# rgb_color=[]
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_color.append((r,g,b))
#
# print(rgb_color)
# # print(len(rgb_color))

# color_list=[(238, 237, 233), (237, 234, 238), (233, 235, 240), (215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56), (11, 87, 108), (177, 190, 213), (111, 124, 153), (81, 142, 169), (73, 63, 53)]

rgb_color=[(color.rgb.r,color.rgb.g,color.rgb.b)for color in colors]

tue.forward(20)

screen.exitonclick()




