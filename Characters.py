'''
This module is responsible for the interaction of the user and characters and contains all the information about 
the different characters of the game
'''
import Content

'''Acknowledge player choice and register their choice in a variable for future use and give attributes to the selected hero'''
def selectCharacter():
    while True:
        global selectedHero, heroName, heroColour, heroHealth, heroIntelligence, heroStrength, heroStamina, healthRestore
        selectedHero = input("\nYour choice (\033[92mValerius\033[0m/\033[94mEldara\033[0m): ").strip().lower()
        if selectedHero == "valerius":
            Content.typingEffect("\nYou have chosen \033[92mValerius, the Guardian Knight\033[0m. Prepare for battle!\n")
            heroName = "Valerius"
            heroColour = "\033[92m"
            heroStamina = +2
            heroStrength = +2
            heroIntelligence = -3
            heroHealth = 50
            healthRestore = 2

            return "Valerius"
        elif selectedHero == "eldara":
            Content.typingEffect("\nYou have chosen \033[94mEldara, the Mystic Sage\033[0m. May wisdom guide your path!")
            heroName = "Eldara"
            heroColour = "\033[94m"
            heroStamina = -1
            heroStrength = -2
            heroIntelligence = +3
            heroHealth = 50
            return "Eldara"
        else:
            Content.typingEffect("\n\033[91mInvalid choice.\033[92m Please type 'Valerius'\033[0m or \033[94m'Eldara'\033[0m.", 0.03)

'''Storyteller Character'''
def storyTeller():
    global oriana
    oriana = "\033[93mOriana:\033[0m "


'''First monster's attributes'''
def kragnar():
    global monsterHealth, kragnarHasShield, kragnarTotalShields, heroCanRemoveShield, monsterColor, monsterName, monsterTitle
    monsterName = "\033[35mKragnar"
    monsterTitle = "Kragnar the Stoneborn!"
    monsterColor = "\033[35m"
    monsterHealth = 25
    kragnarTotalShields = 3  
    kragnarHasShield = False
    heroCanRemoveShield = True


