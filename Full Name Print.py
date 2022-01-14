import turtle
name_input_font = ('Times New Roman', 45, 'bold')
name_input = input("What is your name?: ")



turtle.write("Nice to meet you {}.".format(str(name_input)),font = name_input_font, align = 'center')
