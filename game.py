''' This is the Main module of the game which will handel the program flow and main game script. '''
import time
import sys

#This function creates a typing effect when printing a string of characters with some delay
def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

#Print game title, welcome message and a short overview of the game
def display_welcome(typing_effect):
    print("\n" + "-" *5 +"Legends of Aralon"+"-" *5 +"\n")
    typing_effect("The air crackles with anticipation...", 0.1)
    typing_effect("\033[093mAncient prophecies whisper of monstrous evils returning to the land of Aralon.\033[0m", 0.04)
    typing_effect("The kingdom holds its breath, their fate hanging by a thread.", 0.04)
    typing_effect("Only two heroes stand between light and shadow:\n")
    typing_effect("\033[92mValerius, the stalwart Guardian Knight,\033[0m and \033[94mEldara, the enigmatic Mystic Sage.\033[0m", 0.05)
    typing_effect("\nThe prophecy foretold of their combined strength, yet destiny demands a different path.", 0.03)
    typing_effect("One hero must venture forth to confront the ancient evils", 0.03)
    typing_effect("while the other stands guard, protecting the heart of Aralon from the \033[091mencroaching darkness.\033[0m")
    typing_effect("Which path will you choose, hero?")

display_welcome(typing_effect)

#Prompt for hero selection and with abilities and attributes displayed of each character
def display_options(typing_effect):
    typing_effect("\nWill you take up the mantle of", 0.04)
    typing_effect("\033[92mValerius, the Guardian Knight,\033[0m")
    typing_effect("or embrace the mystical path of", 0.04)
    typing_effect("\033[94mEldara, the Mystic Sage?")

    typing_effect("\n\033[92mValerius, the Guardian Knight,\033[0m", 0.04)
    typing_effect("- Health: +2\n- Strength: +2\n- Wisdom: -3")
    typing_effect("- Special Abilities: Can break a monster's shield once and restore 40% of health twice.", 0.04)

    typing_effect("\n\033[94mEldara, the Mystic Sage:\033[0m", 0.04)
    typing_effect("- Health: -1\n- Strength: -2\n- Wisdom: +2", 0.04)
    typing_effect("- Special Ability: Can dodge a monster's attack once and regenerate 65% of health once.\n", 0.05)

    typing_effect("Type \033[92m'Valerius'\033[0m to embody strength and resilience,", 0.03)
    typing_effect("or \033[94m'Eldara'\033[0m to wield the power of wisdom and magic.", 0.03)

display_options(typing_effect)

#Acknowledge player choice and register their choice in a variable for future use
def select_hero():
    while True:
        hero_choice = input("\nYour choice (\033[92mValerius\033[0m/\033[94mEldara\033[0m): ").strip().lower()
        if hero_choice == "valerius":
            typing_effect("\nYou have chosen \033[92mValerius, the Guardian Knight\033[0m. Prepare for battle!")
            return "Valerius"
        elif hero_choice == "eldara":
            typing_effect("\nYou have chosen \033[94mEldara, the Mystic Sage\033[0m. May wisdom guide your path!")
            return "Eldara"
        else:
            typing_effect("\n\033[91mInvalid choice. Please type \033[92m'Valerius'\033[0m or \033[94m'Eldara'\033[0m.", 0.03)
           
selected_hero = select_hero()


