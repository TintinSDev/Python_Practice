# importing functions from the main .py file
# import funcs
# from funcs import emoji_converter
# from ecommerce.shipping import calc_shipping
from pathlib import Path
import random
# path = Path()
# for file in path.glob('*'):
#     print(file)


people = ['rander', 'Heather', 'Gator']
leader = random.choice(people)
print(leader)

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

# lucky_number = 7
# maxi_guess = 3
# mini_guess = 0
#
# while mini_guess < maxi_guess:
#     guess = int(input("Lucky guess: "))
#     mini_guess += 1
#     if guess == lucky_number:
#         print("Oh you lucky bustard!!")
#         break
#     else:
#         print("Try again next time")

# calc_shipping()
# print(funcs.square())
# funcs.greet_user()
# emoji_converter()
