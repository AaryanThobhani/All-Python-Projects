import turtle

turtle.speed(5)
def square(pixels):
    turtle.forward(pixels)
    turtle.right(90)
    turtle.forward(pixels)
    turtle.right(90)
    turtle.forward(pixels)
    turtle.right(90)
    turtle.forward(pixels)

# square(Call the number of "pixels")

def triangle(pixels, turns):
    turtle.forward(pixels)
    turtle.right(turns)
    turtle.forward(pixels)
    turtle.right(turns)
    turtle.forward(pixels)
triangle(200, 120)
