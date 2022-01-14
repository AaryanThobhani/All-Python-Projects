import turtle


turtle.speed(0)
circle_value = 1000
circle_value2 = 1000
circle_value3 = 1000
circle_value4 = 1000

turtle.pensize(2)
turtle.color("white")
turtle.bgcolor("black")

for i in range(50):
    turtle.circle(circle_value)
    circle_value -= 40
    
turtle.right(90)

for i in range(50):
    turtle.circle(circle_value2)
    circle_value2 -= 40

turtle.right(45)

for i in range(50):
    turtle.circle(circle_value3)
    circle_value3 -= 40

turtle.right(90)

for i in range(50):
    turtle.circle(circle_value4)
    circle_value4 -= 40
