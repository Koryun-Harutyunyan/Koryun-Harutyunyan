from random import choice
gallows = (
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
	 |     / \
	 |
	-------
	"""
	)
max_wrong = len(gallows)
words = ("fruit", "game", "programing")
word = choice(words)
so_far = "_" * len(word)
wrong = 0
guess = input("enter the letter")
if guess in word:
	print("\nYour answer is true")
	new = ""
	for i in range(len(word)):
		if guess == word[i]:
			new += guess
		else:
			new += so_far[i]
			print(gallows[0])
	so_far = new
else:
	print("\nYour answer is wrong")
	wrong += 1


if wrong == max_wrong:
	print(gallows[wrong])
	print("you lose")
else:
	print("you win")


	

