import random

def play():
	user = input("r, p, or s\n")
	computer = random.choice(['r', 'p', 's'])	

	if user == computer:
			return 'tie'	

	if is_win(user, computer):
		return 'You Won'

	return 'You Lost'

def is_win(player, opponent):
	# return true if player wins
	if (player == 'r' and opponent == 's') \
	or (player == 's' and opponent == 'p') \
	or (player == 'p' and opponent == 's'):
		return True

print(play())
