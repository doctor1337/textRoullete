# Roullete
print("[-----------------------------------------------------------------------]")
print("                            Hello!                                       ")
print("        Welcome to Roullete, theese are the commands: bet, balance       ")
print("[-----------------------------------------------------------------------]")
print("\n")

def setBalance():
	global balance
	while True:
		balance = input("How much would you like to have as a balance? ")
		try:
			balance = int(balance)
			if balance == 0:
				print("You can't start with 0 credits as a balance")
				setBalance()
			else:
				main()
				
		except ValueError:
			print("That's not valid")
		

	
def checkBalance():
	print("\nYou have a balance of: ", balance)
	main()
	
def bet():
	print("\nHow much would you like to bet? ")
	global betAmount
	while True:
		betAmount = input("Input the amount you want to bet: ")
		try:
			betAmount = int(betAmount)
			break
		except ValueError:
			print("That's not valid")	
	if betAmount > balance:
		print("You don't have that much")
		bet()
	elif betAmount == 0:
		print("You can't bet 0 credits.")
		bet()
	global betColor
	betColor = input("Input wich color you want to bet (Red/Black/Green)\n> ")
	betColor = betColor.lower()
	if betColor == "red":
		print("You have placed a bet on red")
		roullete()
	elif betColor == "black":
		print("You have placed a bet on black")
		roullete()
	elif betColor == "green":
		print("You have placed a bet on green")
		roullete()
	else:
		print("That's not a valid color")
		bet()

		
	
def red():
		global balance
		if betColor == "red":
			print("You won a total amount of ", betAmount * 2)
			balance = balance + betAmount
			main()
		else:
			print("You lost an amount of ", betAmount)
			balance = balance - betAmount
			main()
			
def black():
		global balance
		if betColor == "black":
			print("You won a total amount of ", betAmount * 2)
			balance = balance + betAmount
			main()
		else:
			print("You lost an amount of ", betAmount)
			balance = balance - betAmount
			main()
			
def green():
		global balance
		if betColor == "green":
			print("You won an amount of ", betAmount * 14)
			balance = balance + (betAmount - betAmount * 14)
			main()
		else:
			print("You lost an amount of ", betAmount)
			balance = balance - betAmount
			main()
						
def roullete():
	import random
	roulleteNo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
	chance = (random.choice(roulleteNo))
	if chance == 0:
		land = "green"
		print("\nIt landed on green")
		green()
	elif chance == 1:
		land = "black"
		print("\nIt landed on black")
		black()
	elif chance == 2:
		land = "black"
		print("\nIt landed on black")
		black()
	elif chance == 3:
		land = "black"
		print("\nIt landed on black")
		black()
	elif chance == 4:
		land = "black"
		print("\nIt landed on black")
		black()
	elif chance == 5:
		land = "black"
		print("\nIt landed on black")
		black()
	elif chance == 6:
		land = "black"
		print("\nIt landed on black")
		black()
	elif chance == 7:
		land = "black"
		print("\nIt landed on black")
		black()
	else:
		land  = "red"
		print("\nIt landed on red!")
		red()

def tryAgain():	
		tryagain = input("Would you like to try again? (y/n)\n> ")
		tryagain.lower()
		if tryagain == "y":
			setBalance()
		elif tryagain == "n":
			print("Ok, bye..")
			exit()
		else:
			print("That's not valid")
			tryAgain()
		
	
def main():
	if balance > 0:
		print("\n")
		while True:
			command = str(input("What would you like to do now?\n> "))
			try:
				command = str(command)
				command = command.lower()
				if command == "bet":
					bet()
				elif command == "balance":
					checkBalance()
				else:
					print("That's not a command")
					main()
			except NameError:
				print("That's not valid!")
				main()
	elif balance == 0:
		print("\n________________________________________________")
		print("\n         You have no more money")
		print("________________________________________________")
		print("\nThanks for playing!")
		tryAgain()
		
		
setBalance()		
main()
