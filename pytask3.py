# Modified Guessing game
import random
number = random.randint(1, 100)
easy_number = random.randint(1, 10)
medium_number = random.randint(1, 20)
hard_number = random.randint(1, 50)
guess_count = 0
print(number)
print('easy', easy_number)
print('medium', medium_number)
print('hard', hard_number)
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

    # a function that will be called by the different levels of the game avoiding repeatation of code
    def guessing(level_count, level_system_number, guess_count):
        for a in range(level_count):
            try:
                num1 = int(input('Make a guess: '))
                guess_count -= 1
                if num1 == level_system_number:
                    print("You are right!!!")
                    break
                else:
                    print("That was wrong")
                    print(f"You have {guess_count} guesses remaining")
            except ValueError:
                print('please enter a valid number')
                
    if user_guess_number1 == 'easy':
        guessing(6, easy_number, 6)
    elif user_guess_number1 == 'medium':
        guessing(4, medium_number, 4)
    elif user_guess_number1 == 'hard':
        guessing(3, hard_number, 3)
    
            
