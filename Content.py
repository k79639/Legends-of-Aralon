'''This module is responsible for displaying the game content'''
import sys
import time

#This function creates a typing effect when printing a string of characters with some delay
def typingEffect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


'''Print game title, welcome message and a short overview of the game'''
def display_welcome():
    #Prints the game title
    print("\n" + "-" * 8 +" Legends of Aralon "+"-" * 8 +"\n")

    #Prints the background story
    typingEffect("The air crackles with anticipation...", 0.08)
    typingEffect("\033[093mAncient prophecies whisper of monstrous evils returning to the land of Aralon.\033[0m", 0.04)
    typingEffect("The kingdom holds its breath, their fate hanging by a thread.", 0.04)

    #Introduce the characters
    typingEffect("Only two heroes stand between light and shadow:\n")
    typingEffect("\033[92mValerius, the stalwart Guardian Knight,\033[0m and \033[94mEldara, the enigmatic Mystic Sage\033[0m.", 0.05)
    typingEffect("\nThe prophecy foretold of their combined strength, yet destiny demands a different path.", 0.03)
    typingEffect("One hero must venture forth to confront the ancient evils", 0.03)
    typingEffect("while the other stands guard, protecting the heart of Aralon from the \033[091mencroaching darkness.\033[0m")
    typingEffect("Which path will you choose, hero?")


'''Prompt for hero selection and with abilities and attributes displayed of each character'''
def display_options():
    #Display the options
    typingEffect("\nWill you take up the mantle of", 0.04)
    typingEffect("\033[92mValerius, the Guardian Knight,\033[0m")
    typingEffect("or embrace the mystical path of", 0.04)
    typingEffect("\033[94mEldara, the Mystic Sage?")

    #Display characters attributes
    typingEffect("\n\033[92mValerius, the Guardian Knight,\033[0m", 0.04)
    typingEffect("- Health: +2\n- Strength: +2\n- Intelligence: -3")
    typingEffect("- Special Abilities: Can break a monster's shield once and restore 40% of health twice.", 0.04)
    typingEffect("\n\033[94mEldara, the Mystic Sage:\033[0m", 0.04)
    typingEffect("- Health: -1\n- Strength: -2\n- Intelligence: +3", 0.04)
    typingEffect("- Special Ability: Can dodge a monster's attack once and regenerate 65% of health once.\n", 0.05)
    typingEffect("Type \033[92m'Valerius'\033[0m to embody strength and resilience,", 0.03)
    typingEffect("or \033[94m'Eldara'\033[0m to wield the power of wisdom and magic.", 0.03)


'''Acknowledge player choice and register their choice in a variable for future use'''
def select_character():
    while True:
        hero_choice = input("\nYour choice (\033[92mValerius\033[0m/\033[94mEldara\033[0m): ").strip().lower()
        if hero_choice == "valerius":
            typingEffect("\nYou have chosen \033[92mValerius, the Guardian Knight\033[0m. Prepare for battle!")
            return "Valerius"
        elif hero_choice == "eldara":
            typingEffect("\nYou have chosen \033[94mEldara, the Mystic Sage\033[0m. May wisdom guide your path!")
            return "Eldara"
        else:
            typingEffect("\n\033[91mInvalid choice. Please type \033[92m'Valerius'\033[0m or \033[94m'Eldara'\033[0m.", 0.03)
        return hero_choice