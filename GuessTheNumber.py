import random

def guess(x):
	random_number = random.randint(1, x)
	guess = 0
	
	while guess !=  random_number:
		
		while True:
			guess = input(f"Guess a number between 1 and {x}: ")

			try:
				guess = int(guess)
				break

			except ValueError:
				print("Pick a whole number dumbass")

		if guess < random_number:
			print("Try a higher number!")
	
		elif guess > random_number:
			print("Try a lower number!")

	print(f"you got it, the number is {random_number}!")

guess(10)


