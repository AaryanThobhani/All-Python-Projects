def biggest_guy(num1, num2, num3):
    if num1 > num2:
        bigger_guy = num1

    else:
        bigger_guy = num2

    if bigger_guy > num3:
        biggest_guy = bigger_guy

    else:
        biggest_guy = num3

    return biggest_guy

print(biggest_guy(1, 2, 6))
