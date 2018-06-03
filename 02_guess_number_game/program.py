# Same import as in PHP, at the top
import random

print('---------------------------------------')
print('      GUESS THAT NUMBER GAME')
print('---------------------------------------')
print()

number = random.randint(0, 100)
guess = -1
name = input('¿Cómo te llamas?')

# This check the variable type
# print(guess_text, type(guess_text))
# print(guess, type(guess))

while guess != number:
    guess_text = input('Adivina en que número estoy pensando (es del 0 al 100) : ')
    guess = int(guess_text)
    winning_text = '¡Has ganado {1}! Era el {0}'.format(guess, name)

    if guess < number:
        print('Más, {1}. {0} es muy BAJO'.format(guess, name))
    elif guess > number:
        # In the same order, you don't need numbers inside the brackets
        print('Menos, {}. {} es muy ALTO'.format(name, guess))
    else:

        print(winning_text)

print ('Listo')
