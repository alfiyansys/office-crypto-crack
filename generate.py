import itertools

#characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`,./?;:'[]\|~!@#$%^&*()-_=+ "
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

#length = 2
#done = False

def pw_guess(i):
	res = itertools.permutations(characters, i)
	for guess in res:
		yield guess

#Make generator object
for i in range(1,4):
	guess_generator = pw_guess(i)
	for guess in guess_generator:
		str_guess = ''.join(guess)
		print(str_guess)
		if guess == ('A', 'B', 'C'):
			print()
			print("Password acquired: " + str(guess))
			break
