def bigger_guy(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

    return bigger_guy
    
def biggest_guy(num1, num2, num3):
    return bigger_guy(bigger_guy(num1, num2), num3)

print(biggest_guy(1, 2, 6))
