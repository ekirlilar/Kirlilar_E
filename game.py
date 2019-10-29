# import the random package so that we can generate a 
from random import randint

#set up some variables for player and AI lives
player_lives = 5
computer_lives = 5

# choices is an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices
computer = choices[randint(0, 2)]

player = input("choose rock, paper or scissors\n\n")

# set up the loop so we don't have to restart all the time
player = False

while player is False:
	#set payer to True	
	print("******************************\n")
	print("Computer lives:", computer_lives, "\5")
	print("Player lives:", player_lives, "\5")
	print ("****************************\n\n")
	print ("Chose your wepon!\n\n")
	print ("****************************\n\n")

	player = input("choose rock or paper or scissors\n\n")


	print ("computer chose ", computer, "\n")
	print ("player chose ", player, "\n")

	if player.lower() == "quit":
		exit()

	elif computer == player:
		print("Tie!")

	elif player.lower() == "rock":
		if computer == "paper":
			print("You Lose!", computer, "covers", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You WIN!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You WIN!", player, "covers", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You WIN!", player, "cuts", computer, "\n")
			computer_lives = computer_lives - 1

	else:
		print("That's not a valid choice, try again")


	if player_lives is 0:
		print("Out of Lives! Would you like to give ita try again?\n")
		choice = input("Y / N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("You chose to quit.")
			exit()

		elif (choice is "Y") or (choice is "y"):
			player_lives = 5
			computer_lives =5
			player = False
			computer = choice[randint(0, 2)]

	elif computer_lives is 0:
		print("You WIN!! Would you like to give it a try again?\n")
		choice = input("Y / N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("You chose to quit.")
			exit()

		elif (choice is "Y") or (choice is "y"):
			player_lives = 5
			computer_lives =5
			player = False
			computer = choice[randint(0, 2)]


	else:
		# need to check all of our conditions after checking for a tie
		player = False
		computer = choices[randint(0, 2)]
