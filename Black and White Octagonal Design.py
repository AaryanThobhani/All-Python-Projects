# Program for Octagonal Design
# Color: Black and White

# Importing Libs
import turtle
import random

# Adjusting Turtle Speed
turtle.speed(0)

# Changing Background Color of Screen
turtle.Screen().bgcolor("black")

# Changing the color of the lines
turtle.color("white")

# Loop for making the illusion/design
for i in range(8):
	turtle.left(45)
	for i in range(8):
		turtle.forward(100)
		turtle.left(45)

# Hiding the arrow: Only Lines
turtle.hideturtle()

# End of Progrma
