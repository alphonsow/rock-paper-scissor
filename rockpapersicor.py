import random
import time
def run():
	print("Rock ")
	time.sleep(1)
	print("Paper ")
	time.sleep(1) 
	print("Scissor")
	time.sleep(1)
	mychoice = input("Shot: ")
	moves = ["Rock","Paper","Scissor"]
	computerchoice=random.choice(moves)
	print(mychoice, "Vs" ,computerchoice)
	if mychoice ==  computerchoice:
		print("draw")
	else:
		if mychoice == 'Rock':
			if computerchoice == 'Paper':
				print("F in the chat.")
			if computerchoice == 'Scissor':
				print("I very best!")
		if mychoice == 'Paper':
			if computerchoice == 'Scissor':
				print("F in the chat.")
			if computerchoice == 'Rock':
				print("I very best!")
		if mychoice == 'Scissor':
			if computerchoice == 'Rock':
				print("F in the chat.")
			if computerchoice == 'Paper':
				print("I very best!")