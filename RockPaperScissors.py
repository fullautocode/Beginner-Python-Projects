import random

def play():

	turns = 1
	user_score = 0
	computer_score = 0

	while turns != 4:
		user = input(f"(Round {turns} of 3) Type 'Rock', 'Paper', or 'Scissors':  ").lower()
		computer = random.choice(['rock', 'paper', 'scissors']).lower()

		if user == 'rock' and computer == 'paper':
			print("Computer picks paper, computer gets a point!")
			turns = turns + 1
			computer_score = computer_score + 1
			print(f"Your Points: {user_score}")
			print(f"Computer's Points: {computer_score}")

		if user == 'rock' and computer == 'scissors':
			print("Computer picks scissors, you get a point!")
			turns = turns + 1
			user_score = user_score + 1
			print(f"Your Points: {user_score}")
			print(f"Computer's Points: {computer_score}")

		if user == 'paper' and computer == 'rock':
			print("Computer picks rock, you get a point!")
			turns = turns + 1
			user_score = user_score + 1
			print(f"Your Points: {user_score}")
			print(f"Computer's Points: {computer_score}")

		if user == 'paper' and computer == 'scissors':
			print("Computer picks scissors, computer gets a point!")
			turns = turns + 1
			computer_score = computer_score + 1
			print(f"Your Points: {user_score}")
			print(f"Computer's Points: {computer_score}")

		if user == 'scissors' and computer == 'paper':
			print ("Computer picks paper, you get a point!")
			turns = turns + 1
			user_score = user_score + 1
			print(f"Your Points: {user_score}")
			print(f"Computer's Points: {computer_score}")

		if user == 'scissors' and computer == 'rock':
			print("Computer picks Rock, computer gets a point")
			turns = turns + 1
			computer_score = computer_score + 1
			print(f"Your Points: {user_score}")
			print(f"Computer's Points: {computer_score}")

		if user == computer:
			print(f"Computer also picked {user}, no one gets a point and the turn doesn't count!")
			print(f"Your Points: {user_score}")
			print(f"Computer's Points: {computer_score}")

	if user_score > computer_score:
		print("You win")
	
	if computer_score > user_score:
		print("You lose")


play()



