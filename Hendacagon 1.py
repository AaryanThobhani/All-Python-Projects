import turtle

def hendacagon():
    turtle.fillcolor("#5695f5")
    turtle.begin_fill()
    turtle.left(16.365)
    turtle.forward(100)

    for i in range(10):
        turtle.left(32.73)
        turtle.forward(100)
    turtle.end_fill()
hendacagon()
