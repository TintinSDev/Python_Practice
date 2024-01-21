# PYTHON_PRACTICE
number = random.randint(1,10)
mini_guess = 0
maxi_guess = 5
while mini_guess < maxi_guess:
    guess = int(input("Let's play a silly game. Guess a number between 1 and 10: "))
    mini_guess += 1
    if guess == number:
        print('YOU ARE LUCKY CHAP!!')
        break
    else:
        print("You's a sucker")

