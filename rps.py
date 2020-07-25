import sys
from random import randint as rand

results = {1: 'rock', 2: 'paper', 3: 'scissors'}

def play(choice):
    cpu_choice = rand(1, 3)
    win_text = '\nYOU WIN! You chose {} and the computer chose {}.'.format(
        results[choice], results[cpu_choice])
    lose_text = '\nYOU LOSE! You chose {} and the computer chose {}.'.format(
        results[choice], results[cpu_choice])
    draw_text = '\nDRAW! You both chose {}.'.format(results[choice])
    if choice == cpu_choice:
        return draw_text
    elif cpu_choice == 1:
        return [lose_text, win_text][choice == 2]
    elif cpu_choice == 2:
        return [lose_text, win_text][choice == 3]
    elif cpu_choice == 3:
        return [lose_text, win_text][choice == 1]

def choose():
    error_text = '\nPlease follow instructions. Your must enter either 1, 2, or 3 to play or 4 to quit.'
    try:
        choice = int(input(
            '\nEnter 1, 2, or 3 to choose rock, paper, or scissors. Enter 4 to quit: '))
    except ValueError:
        print(error_text)
    else:
        if choice in range(1, 5):
            if choice == 4:
                print('\nThank you for playing Rock, Paper, Scissors.')
                sys.exit(0)
            else:
                print(play(choice))
        else:
            print(error_text)


while True:
    choose()
