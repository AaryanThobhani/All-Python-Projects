def square_number(number):
	return number ** 2

def test_number():	
	assert square_number(2) == 4
	assert square_number(9) == 81
	assert square_number(11) == 121
	print("I am a Programmer.")

test_number() 

def even_number(number):
	if number % 2 == 0:
		return True
	else:
		return False

assert even_number(13) == False
assert even_number(14) == True
assert even_number(33) == False
assert even_number(36 / 3) == True
print(even_number(18))

print("Yay, the code is right")

