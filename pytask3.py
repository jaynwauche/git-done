# Modified Guessing game
import random
number = random.randint(1, 100)
easy_number = random.randint(1, 10)
medium_number = random.randint(1, 20)
hard_number = random.randint(1, 50)
guess_count = 0
print(number)
print('easy', easy_number)
try:
    while True:
        user_guess_number = int(input('Guess a number: '))
        if user_guess_number == number:
            print('You won!!!')
            break
        else:
            print('Wrong answer')
except ValueError:
    user_guess_number1 = (input('There are three levels: easy, medium, and hard, choose: '))
if user_guess_number1 == 'easy':
    for a in range(6):
        num1 = int(input('Make a guess: '))
        guess_count += 1
        if num1 == easy_number:
            print("You are right")
            break
        else:
            print("That was wrong")
    else:
        print("Game over")
if user_guess_number1 == 'medium':
    for x in range(4):
        num2 = int(input('Make a guess: '))
        guess_count += 1
        if num2 == medium_number:
            print("You are right")
            break
        else:
            print("That was wrong")
    else:
        print('Game over')
elif user_guess_number1 == 'hard':
    for b in range(3):
        num1 = int(input('Make a guess: '))
        guess_count += 1
        if num1 == hard_number:
            print("You are right")
            break
        else:
            print("That was wrong")
    else:
        print('Game over')
            
