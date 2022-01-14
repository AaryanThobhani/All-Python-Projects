import turtle

x = 20
turn_right_Triangle = 120

turtle.speed(0)
turtle.bgcolor("black")
turtle.color("white")
turtle.pensize(3)

for i in range(200):
    turtle.forward(x)
    turtle.right(turn_right_Triangle)
    turtle.forward(x)
    turtle.right(turn_right_Triangle)
    turtle.forward(x)

    turtle.right(100)

    x += 5
