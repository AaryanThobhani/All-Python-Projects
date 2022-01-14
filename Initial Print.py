import turtle

user_input_font = ('Times New Roman', 50, 'bold')
user_input = input("What is your first and last initial?: ")


turtle.write('Hey {}'. format(user_input), font = user_input_font, align = 'center')

