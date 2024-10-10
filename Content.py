'''This module is responsible for displaying the game content'''
import sys
import time
import Characters

#This function creates a typing effect when printing a string of characters with some delay
def typingEffect(text, delay=0):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


'''Print game title, welcome message and a short overview of the game'''
def displayWelcome():
    #Prints the game title
    print("\n" + "-" * 8 +" Legends of Aralon "+"-" * 8 +"\n")

    #Prints the background story
    typingEffect("The air crackles with anticipation...", 0.07)
    typingEffect("Ancient prophecies whisper of monstrous evils returning to the land of Aralon.", 0.04)
    typingEffect("The kingdom holds its breath, their fate hanging by a thread.", 0.03)

    #Introduce the characters
    typingEffect("Only two heroes stand between light and shadow:\n", 0.04)
    typingEffect("\033[92mValerius, the stalwart Guardian Knight,\033[0m and \033[94mEldara, the enigmatic Mystic Sage\033[0m.")
    typingEffect("\nThe prophecy foretold of their combined strength, yet destiny demands a different path.", 0.03)
    typingEffect("One hero must venture forth to confront the ancient evils", 0.04)
    typingEffect("while the other stands guard, protecting the heart of Aralon from the \033[091mencroaching darkness.\033[0m",0.03)
    typingEffect("Which path will you choose, hero?")


'''Prompt for hero selection and with abilities and attributes displayed of each character'''
def displayOptions():
    #Display the options
    typingEffect("\nWill you take up the mantle of", 0.04)
    typingEffect("\033[92mValerius, the Guardian Knight,\033[0m")
    typingEffect("or embrace the mystical path of", 0.04)
    typingEffect("\033[94mEldara, the Mystic Sage?")

    #Display characters attributes
    typingEffect("\n\033[92mValerius, the Guardian Knight,\033[0m", 0.04)
    typingEffect("- Stamina: +2\n- Strength: +2\n- wisdom: -3")
    typingEffect("- Special Abilities: Can break a monster's shield once and restore 40% of health twice.", 0.03)
    typingEffect("\n\033[94mEldara, the Mystic Sage:\033[0m", 0.04)
    typingEffect("- Stamina: -1\n- Strength: -2\n- Intelligence: +3", 0.04)
    typingEffect("- Special Ability: Can dodge a monster's attack once and regenerate 65% of health once.\n", 0.03)
    typingEffect("Type \033[92m'Valerius'\033[0m to embody strength and resilience,", 0.03)
    typingEffect("or \033[94m'Eldara'\033[0m to wield the power of wisdom and magic.", 0.03)



'''Oriana the storyteller's dialogues for challenge 1'''
def orianaChallengeIntro():
    typingEffect("\033[93mOriana:\033[0m Greetings, hero. I am Oriana, keeper of forgotten tales and chronicler of Aralon.")
    typingEffect("        I am here to guide you on your journey and share the wisdom of the ancients.", 0.02)
    typingEffect("        A new challenge awaits you, hero. Prepare yourself for what lies ahead.\n", 0.03)
    typingEffect("        The first foe you must confront is known as \033[35mKragnar the Stoneborn\033[0m.", 0.06)
    typingEffect("        A towering beast of immense size and formidable strength.", 0.03)
    typingEffect("        Beware, hero; he can summon a shield of earth to deflect your critical attacks.", 0.03)
    typingEffect("        Choose your attacks wisely, for strategy will be key in overcoming this challenge.\n", 0.02)
    typingEffect("        \033[1mRemember, I will be here to offer guidance whenever you need it.\033[0m")
    typingEffect("        Now, steel your resolve and prepare to face Kragnar the Stoneborn.\n")

