'''
This module is responsible for the interaction of the user and characters and contains all the information about 
the different characters of the game
'''
import GameScript
import Challenges
import random

'''Acknowledge player choice and register their choice in a variable for future use and give attributes to the selected hero'''
def selectCharacter():
    while True:
        global selectedHero
        selectedHero = input("\nYour choice (\033[92mValerius\033[0m/\033[94mEldara\033[0m): ").strip().lower()
        if selectedHero == "valerius":
            GameScript.typingEffect("\nYou have chosen \033[92mValerius, the Guardian Knight\033[0m. Prepare for battle!\n")
            valerius()
            return "Valerius"
        elif selectedHero == "eldara":
            GameScript.typingEffect("\nYou have chosen \033[94mEldara, the Mystic Sage\033[0m. May wisdom guide your path!")
            eldara()
            return "Eldara"
        else:
            GameScript.typingEffect("\n\033[91mInvalid choice.\033[92m Please type 'Valerius'\033[0m or \033[94m'Eldara'\033[0m.", 0.03)

'''This function defines the attributes of the first hero Valerius'''
def valerius():
    global heroName, heroColour, heroHealth, heroIntelligence, heroStrength, heroStamina,\
    heroCanRemoveShield, heroCanRespawn, heroCanDodgeAttack, heroCanRestoreHealth, shieldUsed
    heroName = "Valerius"
    heroColour = "\033[92m"
    heroStamina = +2
    heroStrength = +2
    heroIntelligence = -3
    heroHealth = 50
    heroCanRemoveShield = True
    heroCanRestoreHealth = 2
    heroCanDodgeAttack = False
    heroCanRespawn = False
    shieldUsed = False

'''This function gives valerius ability to restore 40% of his health twice'''
def valeriusHealthRestoreAbility():
    global heroCanRestoreHealth, heroHealth
    while True:
        if selectedHero == "valerius" and heroCanRestoreHealth > 0 and heroHealth < 25:
            heroCanRestoreHealth = input("\nWould you like to use your health restoration ability now? (yes/no): ").strip().lower()
            if heroCanRestoreHealth == 'yes':
                heroHealth = heroHealth + 20
                heroCanRestoreHealth = heroCanRestoreHealth - 1
                GameScript.typingEffect(f"\n{heroColour}{heroName}\033[0m health restored to: {heroHealth}\n", 0.03)
                GameScript.typingEffect(f"{heroColour}{heroName}\033[0m have {heroCanRestoreHealth} health restoration use(s) left.\n", 0.03)
                break
            elif heroCanRestoreHealth == 'no':
                GameScript.typingEffect(f"\nYou chose not to use {heroColour}{heroName}\033[0m health restoration ability. The battle continues!\n", 0.02)
                break
            else:
                GameScript.typingEffect("\n\033[91mInvalid choice.\033[0m Please type 'Yes' or 'No'.", 0.03)
        else:
            break

'''This function gives valerius ability to destroy monster's shield once'''
def valeriusDestroyShieldAbility():
    global heroCanRemoveShield, shieldUsed, monsterHealth, kragnarHasShield
    # Prompt to remove the shield but only once
    if heroCanRemoveShield:
        while True:
            removeShield = input(f"Do you want to use {heroColour}{heroName}\033[0m ability to break Kragnar's shield? (yes/no): ").strip().lower()
            if removeShield == "yes":
                kragnarHasShield = False
                # Apply damage after shield is broken
                monsterHealth -= Challenges.damage
                GameScript.typingEffect(f"\n{heroColour}{heroName}\033[0m shatters {monsterName}'s\033[0m shield and deals {Challenges.damage} damage!\n", 0.03)
                GameScript.typingEffect(f"{monsterName}\033[0m has {kragnarTotalShields} shields remaining.\n", 0.03)
                monsterHealth = max(0, monsterHealth)  
                GameScript.typingEffect(f"{monsterName}'s\033[0m remaining health: {monsterHealth}\n", 0.03)
                heroCanRemoveShield = False
                break
            
            # If player decided not to destroy monster's shield
            elif removeShield == "no":
                GameScript.typingEffect(f"\n{heroName} decides to save their ability for now.\n", 0.03)
                GameScript.typingEffect(f"{monsterName}'s\033[0m shield absorbs your attack!\n", 0.03)
                GameScript.typingEffect(f"{monsterName}\033[0m has {kragnarTotalShields} shields remaining.\n", 0.03)
                kragnarHasShield = False
                break

            # If monster have a shield but hero cannot remove it and aleart the player that the shield is already used.
            elif not heroCanRemoveShield and kragnarHasShield and not shieldUsed:
                GameScript.typingEffect(f"{heroColour}{heroName}\033[0m have already used your ability to break a shield, so you cannot remove it again.\n", 0.03)
                GameScript.typingEffect(f"{monsterName}'s\033[0m shield absorbs your attack!\n", 0.03)
                GameScript.typingEffect(f"{monsterName}\033[0m has {kragnarTotalShields} shields remaining.\n", 0.03)
                kragnarHasShield = False
                shieldUsed = True
            else:
                GameScript.typingEffect("\n\033[91mInvalid choice.\033[0m Please type 'Yes' or 'No'.\n", 0.03)
    else:
        GameScript.typingEffect(f"{heroColour}{heroName}\033[0m does not have the ability to destroy Monster's Shield\n")
        GameScript.typingEffect(f"{monsterName}'s\033[0m shield absorbs your attack!\n", 0.03)
        GameScript.typingEffect(f"{monsterName}\033[0m has {kragnarTotalShields} shields remaining.\n", 0.03)
        kragnarHasShield = False

'''This function defines the attributes of the second hero eldara'''
def eldara():
    global heroName, heroColour, heroHealth, heroIntelligence, heroStrength, heroStamina,\
    heroCanRemoveShield, heroCanRespawn, heroCanDodgeAttack, heroCanRestoreHealth
    heroName = "Eldara"
    heroColour = "\033[94m"
    heroStamina = -1
    heroStrength = -2
    heroIntelligence = +3
    heroHealth = 50
    heroCanRespawn = True
    heroCanDodgeAttack = 2
    heroCanRemoveShield = False
    heroCanRestoreHealth = False

'''This function gives Eldara ability to respawn once but with only 65% of total original health.'''
def eldaraRespawnAbility():
    global heroCanRespawn, heroHealth
    while True:
        if selectedHero == "eldara" and heroCanRespawn and heroHealth == 0:
            heroCanRespawn = input(f"\nWould you like to use {heroColour}{heroName}'s\033[0m respawn ability and continue the battle (yes/no): ").strip().lower()
            if heroCanRespawn == 'yes':
                heroHealth = heroHealth + 33
                heroCanRespawn = False
                GameScript.typingEffect(f"\n{heroColour}{heroName}\033[0m health restored to: {heroHealth}\n", 0.03)
                GameScript.typingEffect(f"{heroColour}{heroName}\033[0m can not use this ability again", 0.03)
                break
            elif heroCanRespawn == 'no':
                GameScript.typingEffect(f"\nYou chose not to use {heroColour}{heroName}'s\033[0m respawn ability.\n", 0.02)
                break
            else:
                GameScript.typingEffect("\n\033[91mInvalid choice.\033[0m Please type 'Yes' or 'No'.", 0.03)
        else:
            break

'''This function gives Eldara ability to dodge a monster's critical attack twice'''
def eldaraDodgeAbility():
    global heroCanDodgeAttack
    while True:
        if heroCanDodgeAttack > 0 and Challenges.monsterDamage >= 5:
            heroCanDodgeAttack = input(f"\nWould you like to use {heroColour}{heroName}\033[0m ability to dodge this attack?: ").strip().lower()
            if heroCanDodgeAttack == 'yes':
                heroHealth = heroHealth + Challenges.monsterDamage
                heroCanDodgeAttack = heroCanDodgeAttack - 1
                GameScript.typingEffect(f"\n{heroColour}{heroName}\033[0m succesfully dodged the monster attack.\n", 0.03)
                GameScript.typingEffect(f"{heroColour}{heroName}\033[0m have {heroCanDodgeAttack} dodge left.", 0.03)
                break
            elif heroCanDodgeAttack == 'no':
                GameScript.typingEffect(f"\nYou chose not to use {heroColour}{heroName}'s\033[0m dodge ability.The battle continues!\n", 0.02)
                break
            else:
                GameScript.typingEffect("\n\033[91mInvalid choice.\033[0m Please type 'Yes' or 'No'.", 0.03)
        else:
            break

'''This function defines the Storyteller Character'''
def storyTeller():
    global oriana
    oriana = "\033[93mOriana:\033[0m "

'''This function defines the First monster's attributes'''
def kragnar():
    global monsterHealth, kragnarHasShield, kragnarTotalShields, monsterColor, monsterName, monsterTitle
    monsterName = "\033[35mKragnar"
    monsterTitle = "Kragnar the Stoneborn!"
    monsterColor = "\033[35m"
    monsterHealth = 200
    kragnarTotalShields = 3  
    kragnarHasShield = False

'''This function gives kragnar ability to create a shield to protect himself if critically attacked by the hero'''
def kragnarShieldAbility():
    global kragnarTotalShields, kragnarHasShield, monsterHealth
    # 50% chance for Kragnar to create a shield if he has shields left
    if random.randint(0, 0) == 0:
        monsterDecidedToUseAbility = True
    else:
        monsterDecidedToUseAbility = False
    if kragnarTotalShields > 0 and monsterDecidedToUseAbility and not kragnarHasShield:
        kragnarHasShield = True
        kragnarTotalShields -= 1
        GameScript.typingEffect("\n\033[35mKragnar\033[0m summons a shield of stone to protect himself!\n")
        valeriusDestroyShieldAbility()
    elif monsterDecidedToUseAbility == False:
        monsterHealth -= Challenges.damage
        # Ensure that the health does not go into negative
        monsterHealth = max(0, monsterHealth)  
        GameScript.typingEffect(f"\n{heroColour}{heroName}\033[0m rolled a critical hit! {monsterName}\033[0m takes {Challenges.damage} damage.\n", 0.04)
        GameScript.typingEffect(f"{monsterName}'s\033[0m remaining health: {monsterHealth}\n", 0.03)
    else:
        monsterHealth -= Challenges.damage
        # Ensure that the health does not go into negative
        monsterHealth = max(0, monsterHealth)  
        GameScript.typingEffect(f"\n{heroColour}{heroName}\033[0m rolled a critical hit! {monsterName}\033[0m takes {Challenges.damage} damage.\n", 0.04)
        GameScript.typingEffect(f"{monsterName}'s\033[0m remaining health: {monsterHealth}\n", 0.03)



