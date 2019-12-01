#!/usr/bin/env python3

# imports
import random
# vars
player_choice = ''
# defs
def machine_move():
	# 1 being rock, 2 being paper, 3 being scissors
	random_move = random.randint(0, 2)
	
	if random_move == 1:
		print("The machine chooses rock!")
	elif random_move == 2:
		print("The machine chooses paper!")
	else:
		print("The machine chooses scissors!")
	return random_move
def check_winner(player_choice):
	random_move = machine_move()

	if player_choice == "rock" and random_move == 1:
		print("Draw!")
	elif player_choice == "scissors" and random_move == 1:
		print("Player lost!")
	elif player_choice == "rock" and random_move == 2:
		print("Player lost!")
	elif player_choice == "paper" and random_move == 3:
		print("Player lost!")
	else:
		print("Player won!")
def main():
	print('Rock, paper, scissors!')
	player_choice = input("Choose your move [rock/paper/scissors]: ")
	check_winner(player_choice)
# main
if __name__ == '__main__':
	while True:
		main()