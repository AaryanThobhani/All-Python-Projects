def largerNumber(num1, num2):
  for i in num1, num2:
    if num1 < num2:
      return num2
    else:
      return num1

  return largerNumber()

print(largerNumber()(1, 2))
