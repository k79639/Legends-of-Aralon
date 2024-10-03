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

#Print a welcome message and a short overview of the game
typing_effect("The air crackles with anticipation...", 0.1)
typing_effect("\033[093mAncient prophecies whisper of monstrous evils returning to the land of Aralon.\033[0m", 0.04)
typing_effect("The kingdom holds its breath, their fate hanging by a thread.", 0.04)
typing_effect("Only two heroes stand between light and shadow:\n")
typing_effect("\033[92mValerius, the stalwart Guardian Knight,\033[0m and \033[94mEldara, the enigmatic Mystic Sage.\033[0m", 0.05)
typing_effect("\nThe prophecy foretold of their combined strength, yet destiny demands a different path.", 0.03)
typing_effect("One hero must venture forth to confront the ancient evils",0.03)
typing_effect("while the other stands guard, protecting the heart of Aralon from the \033[091mencroaching darkness.\033[0m")
typing_effect("Which path will you choose, hero?")

