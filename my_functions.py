import sys
sys.path.append("/Users/ktsionis/Library/Python/3.10/lib/python/site-packages")
import random
import time
import gesturesASCII as ASCII
from termcolor import colored, cprint

def print_object_info(obj):
    cprint('getting dictionary info...', 'green')
    cprint(obj)

def play_rock_paper_scissors():

    playing_game = True

    cprint('getting some rock paper and a pair of scissors..','green')
    score = [0,0]

    while playing_game:
        colors = ['red', 'cyan', 'magenta']
        rock_expressions = ['rock','Rock','R','r',1]
        paper_expressions = ['paper','Paper','P','p',2]
        scissors_expressions = ['scissors','Scissors','S','s',3]
        won_game = 0

        responses = {'rock':rock_expressions, 'paper':paper_expressions, 'scissors':scissors_expressions }

        acceptable_responses = rock_expressions + paper_expressions + scissors_expressions
        correct_input = False

        while not correct_input:
            player_choice = input(colored('What will you choose? ', 'green'))

            if player_choice in acceptable_responses:
                correct_input = True
            else:
                cprint('... \n Not a valid option please try again', 'yellow')

        if not correct_input:
            return 'end of game'

        cpu_choice = random.randint(0,2)
        cprint('choices locked in', 'green')
        time.sleep(0.5)
        cprint('game starting...', 'green')
        time.sleep(2)

        if player_choice in responses['rock']:
            cprint(ASCII.text[0], colors[0])
            cprint(ASCII.gestures[0], colors[0])
            if cpu_choice == 2:
                won_game = 1
                score[0] += 1
            if cpu_choice == 1:
                won_game = -1
                score[1] += 1

        if player_choice in responses['paper']:
            cprint(ASCII.text[1], colors[1])
            cprint(ASCII.gestures[1], colors[1])
            if cpu_choice == 0:
                won_game = 1
                score[0] += 1
            if cpu_choice == 2:
                won_game = -1
                score[1] += 1

        if player_choice in responses['scissors']:
            cprint(ASCII.text[2], colors[2])
            cprint(ASCII.gestures[2], colors[2])
            if cpu_choice == 1:
                won_game = 1
                score[0] += 1
            if cpu_choice == 0:
                won_game = -1
                score[1] += 1

        time.sleep(1)
        cprint(ASCII.versus, 'yellow')
        time.sleep(1)
        cprint(ASCII.text[cpu_choice], colors[cpu_choice])
        cprint(ASCII.gestures[cpu_choice], colors[cpu_choice])
        time.sleep(2)
        if won_game == 1:
            cprint(ASCII.win[0], 'green')
        elif won_game == -1:
            cprint(ASCII.lose[0], 'red')
        else:
            cprint(ASCII.draw[0], 'yellow')

        time.sleep(2)
        cprint('Player: ' + str(score[0]) + ' - CPU: ' + str(score[1]), 'green')

        keep_playing = input(colored('Play again? (Y) ', 'yellow'))
        if keep_playing != 'Y':
            playing_game = False
            time.sleep(0.5)
            cprint('Thanks for playing :)', 'green')
            time.sleep(1)