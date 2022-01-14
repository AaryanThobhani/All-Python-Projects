import turtle

turtle.speed(0)
x = 100
angle_right = 40

def hexagon():
     for i in range(6):
        turtle.forward(x)
        turtle.right(angle_right)

for i in range(100):
    turtle.right(10)
    hexagon()
    turtle.right(10)
    hexagon()
