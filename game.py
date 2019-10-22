# import the random package so that we can generate a 
from random import randint
# choices is an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices
computer = choices[randint(0, 2)]

player = input("choose rock, paper or scissors\n")

# set up the loop so we don't have to restart all the time
player = False

while player = False:
	#set player to True
player = input("choose rock or paper or scissors\n")

print ("computer chose ", computer, "\n")
print ("player chose ", player, "\n")

if player == "quit"
exit()

elif computer == player:
	print("tie!")
# need to check all of our conditions after checking for a tie
player = False
computer = choices [randint(0, 2)]