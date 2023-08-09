from colorama import init
from termcolor import colored

BLANK = "_"

def printb(stats):
    correct = stats[0]
    in_word = stats[1]
    output = []

    for i in range(0, len(correct)):
        if correct[i] != BLANK:
            output.append(colored(correct[i], 'green'))
        elif in_word[i] != BLANK:
            output.append(colored(in_word[i], 'yellow'))
        else:
            output.append(BLANK)
    print(' '.join(output))
