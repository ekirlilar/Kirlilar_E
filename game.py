# import the random package so that we can generate a 
from random import randint
# choices is an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices
computer = choices[randint(0, 2)]

player = input("choose rock, paper or scissors\n\n")

# set up the loop so we don't have to restart all the time
player = False

while player is False:	
	
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
		else:
			print("You WIN!", player, "smashes", computer, "\n")

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
		else:
			print("You WIN!", player, "covers", computer, "\n")

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
		else:
			print("You WIN!", player, "cuts", computer, "\n")

	else:
		print("That's not a valid choice, try again")



	# need to check all of our conditions after checking for a tie
	player = False
	computer = choices [randint(0, 2)]
