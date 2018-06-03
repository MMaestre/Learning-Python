# Same import as in PHP, at the top
import random

print('---------------------------------------')
print('      GUESS THAT NUMBER GAME')
print('---------------------------------------')
print()

number = random.randint(0, 100)
guess_text = input('Adivina en que número estoy pensando (es del 0 al 100) : ')

guess = int(guess_text)

# This check the variable type
# print(guess_text, type(guess_text))
# print(guess, type(guess))
