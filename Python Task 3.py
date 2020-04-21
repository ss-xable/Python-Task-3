from random import randint
import string
print('''Welcome to the Guessing Game!''')

start = True
while start:
    difficulty_level = str(input('Select Difficulty Level by choosing [E for Easy, M for Medium, H for hard]: ')).upper()
    
    start = False
    if difficulty_level == 'E':
        secret_number = randint(1,10)
        for number_of_guesses in range(6):
            guess = eval(input('pick guess[1-10]? '))
            while guess != secret_number:
                print('That answer was wrong!', 5-number_of_guesses,'guesses left')
                break
                
            else:
                print('You got it right')
                break
        else:
            print('Sorry, Gameover!')
            start = False
            
    if difficulty_level == 'M':
        secret_number = randint(1,20)
        for number_of_guesses in range(4):
            guess = eval(input('pick guess[1-20]? '))
            while guess != secret_number:
                print('That was wrong!', 3-number_of_guesses,'guesses left')
                break
                
            else:
                print('You got it right')
                break
        else:
            print('Sorry, Gameover!')
            start = False
            
    if difficulty_level == 'H':
        secret_number = randint(1,50)
        for number_of_guesses in range(3):
            guess = eval(input('pick guess[1-50]? '))
            while guess != secret_number:
                print('That was wrong!', 2-number_of_guesses,'guesses left')
                break

            else:
                print('You got it right')
                break
        else:
            print ('Sorry, Gameover!!!')
            start = False
            
    to_continue = str(input('Do you wish to continue game [Y/N]? '))
    if to_continue == 'N':
        start = False
    else:
        start = True