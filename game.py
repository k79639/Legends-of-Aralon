''' This is the first version of the game to kind of test some ideas '''
import time
import sys

#This function creates a typing effect when printing a string of characters with some delay
def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

typing_effect("Hello")