from random import choice
gallows = [
	"""
	  ______
	 | /    |
	 |/     | 
	 |      |
	 |      0 
	 |
	 |
	 |
	 |
	-------
	""",
	"""
	  ______
	 | /    |
	 |/     | 
	 |      |  
	 |      0
	 |     /|\\
	 |
	 |
	-------
	""",
	"""
	  ______
	 | /    |
	 |/     | 
	 |      |  
	 |      0
	 |     /|\\
	 |     / \\
	 |
	-------
	"""
]
words = ["eagle", "game", "programing"]
word = choice(words)
so_far = "_" * len(word)
print(so_far)
wrong = 0
count = 0
a = len(word)

while count < len(word):
	guess = input("enter the letter\n")
	

		
	if guess in word:
		print("\nYour answer is true")
		count += 1		
	else:
		print("\nYour answer is wrong")
		wrong += 1
		print(gallows[wrong - 1])
	
	if count == len(word) and wrong != 3:
		print("you win")
		break
	elif wrong == 3:
		print("you lose")
		break





	

	
	


	

