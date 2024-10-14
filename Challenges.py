'''This module is responsible for the mechanics of all the challenges in the Game.'''

import Characters
import GameScript
import random

'''This function determines the outcome of the round'''
def diceRoll():
    global totalRoll
    # Rolling 2 six-sided dice.
    rollResult = random.randint(2, 12)  
    # Calculate the outcome of the dice roll considering the attribute of the hero.
    totalRoll = rollResult + heroAttribute
    # Ensure that total damage does not goes into negative
    totalRoll = max(0, totalRoll)
    GameScript.typingEffect(f"\n{Characters.heroColour}{Characters.heroName}\033[0m rolled {rollResult} (Modified by your {heroAttributeName} {heroAttribute} is {totalRoll}).", 0.03)

'''This function determines the damage dealt by the monster and Zarok'''
def monsterAttack():
    global monsterDamage

    # Function to determine the damage given by other monsters vs Zarok
    if GameScript.challengeNumber<=4:
        global monsterRoll
        monsterRoll = random.randint(2, 12)
    elif Characters.monsterTitle == "Zarok the Deathbringer" and Characters.monsterHealth <= 15 and Characters.monsterHealth > 0:
        monsterDamage = random.randint(4, 8)
    else:
        monsterRoll = 1

    # Checks if monster rolled more than the hero and monster is alive or not
    if monsterRoll > totalRoll and Characters.monsterHealth > 0:
        # Difference in rolls is the damage dealt to the hero
        monsterDamage = monsterRoll - totalRoll  
        Characters.heroHealth -= monsterDamage
        # Ensure hero's health does not go negative
        Characters.heroHealth = max(0, Characters.heroHealth)  
        GameScript.typingEffect(f"{Characters.colouredMonsterName}\033[0m strikes back and deals {monsterDamage} damage!", 0.04)
        Characters.eldaraDodgeAbility()
        GameScript.typingEffect(f"\n{Characters.heroColour}{Characters.heroName}\033[0m remaining health: {Characters.heroHealth}\n", 0.03)
        # Give health restore ability to Valerius
        Characters.valeriusHealthRestoreAbility()
        Characters.eldaraRespawnAbility()

    # If Zarok's health drops below 16 he uses his ability
    if Characters.monsterTitle == "Zarok the Deathbringer" and Characters.monsterHealth <= 15 and Characters.monsterHealth > 0:
        Characters.zarokDoubleDamageAbility()
    else:
        pass

'''This function checks if someone has won and display the messages accordingly'''
def checkWinner():

    # Oriana message whenever hero won
    if Characters.monsterHealth <= 0 and not GameScript.gameEnd:
        GameScript.typingEffect(f"{Characters.oriana}You have defeated {Characters.monsterColor}{Characters.monsterTitle}\033[0m Victory is yours!\n")
        GameScript.challengeNumber += 1
        Battlefield()

    # Ending message when hero finally defeate every monster
    elif Characters.monsterHealth <= 0 and GameScript.gameEnd: 
        GameScript.typingEffect(f"{Characters.colouredMonsterName}: \033[0mImpossible... How could I be defeated by a mere mortal?")
        GameScript.typingEffect("       This cannot be... but I feel my power slipping away...\n")
        GameScript.typingEffect("       I have been vanquished, hero. The darkness recedes... and I will never return.")
        GameScript.typingEffect("       Enjoy your victory... for even in my absence, shadows will always lurk in the hearts of men.\n")
        GameScript.typingEffect("       But as for me... my reign of terror is over.")

    # Message when monster won 
    elif Characters.heroHealth <= 0:
        GameScript.typingEffect(f"{Characters.heroColour}{Characters.heroName}\033[0m has been defeated. Game over.\n")

'''This function runs when the result of the dice is less than 10 / when critical damage is not delt'''
def normalAttack():
    global damage
    damage = totalRoll 
    # Ensure that total damage does not goes into negative
    damage = max(0, damage) 
    Characters.monsterHealth -= damage
    # Ensure health does not go negative
    Characters.monsterHealth = max(0, Characters.monsterHealth)  
    GameScript.typingEffect(f"\n{Characters.heroColour}{Characters.heroName}\033[0m hit {Characters.monsterColor}{Characters.colouredMonsterName}\033[0m for {damage} damage.", 0.03)
    GameScript.typingEffect(f"\n{Characters.colouredMonsterName}'s\033[0m remaining health: {Characters.monsterHealth}\n", 0.03)

'''This function runs when the result of the dice more than 10'''
def criticalAttack():
    if Characters.monsterHealth> 0 :
        Characters.monsterHealth -= damage
        # Ensure that the health does not go into negative
        Characters.monsterHealth = max(0, Characters.monsterHealth)  
        GameScript.typingEffect(f"\n{Characters.heroColour}{Characters.heroName}\033[0m rolled a critical hit! {Characters.colouredMonsterName}\033[0m takes {damage} damage.\n", 0.04)
        GameScript.typingEffect(f"{Characters.colouredMonsterName}'s\033[0m remaining health: {Characters.monsterHealth}\n", 0.03)

'''This function handles all the challenges and loop the battle until someone won'''
def Battlefield():
    # Challenge 1
    if GameScript.challengeNumber == 1:
        global totalRoll, heroAttribute, heroAttributeName, damage

        # Attribute used for this challenge
        heroAttribute = Characters.heroStrength
        heroAttributeName = "Strength"

        # Wakes up the monster for the round
        Characters.kragnar()
        # Display initial dialogues
        GameScript.challenge1InitialDialogues()
    
    # Challenge 2
    elif GameScript.challengeNumber == 2:

        # Attribute used for this challenge
        heroAttribute = Characters.heroIntelligence
        heroAttributeName = "Intelligence"

        # Wakes up the monster for the round
        Characters.azra()
        # Display initial dialogues
        GameScript.orianaChallenge2Intro()
        GameScript.challenge2InitialDialogues()

    # Challenge 3
    elif GameScript.challengeNumber == 3:

        # Attribute used for this challenge
        heroAttribute = Characters.heroStamina
        heroAttributeName = "Stamina"

        # Wakes up the monster for the round
        Characters.malakar()
        # Display initial dialogues
        GameScript.orianaChallenge3Intro()
        GameScript.challenge3InitialDialogues()

    # Challenge 4
    elif GameScript.challengeNumber == 4:

        # Attribute used for this challenge
        heroAttribute = Characters.heroStrength
        heroAttributeName = "Strength"

        # Wakes up the monster for the round
        Characters.Ignarok()
        # Display initial dialogues
        GameScript.orianaChallenge4Intro()
        GameScript.challenge4InitialDialogues()

    # Challenge 5
    elif GameScript.challengeNumber == 5:

        # Attribute used for this challenge
        heroAttribute = Characters.heroStamina
        heroAttributeName = "Stamina"

        # Wakes up the monster for the round
        Characters.zarok()
        # Display initial dialogues
        GameScript.orianaChallenge5Intro()
        GameScript.challenge5InitialDialogues()

    # Battle loop until one character wins
    while Characters.monsterHealth > 0 and Characters.heroHealth > 0:

        input("\n\033[4mPress Enter/Return to roll dices:\033[0m ")

        # Roll the dice to determine the outcome of this round
        diceRoll()
        
        # Determine what happens when Critical hit by hero and give azar ability to attack when his health drops below 16
        if totalRoll >= 8 or Characters.monsterTitle == "Azra the Mirror Fiend": 
            damage = totalRoll
            if GameScript.challengeNumber == 1:
                Characters.kragnarShieldAbility()
            elif GameScript.challengeNumber == 2:
                Characters.azraAttackReverseAbility()
            elif GameScript.challengeNumber == 3:
                Characters.malakarAbsorbAttackAbility()
            elif GameScript.challengeNumber == 4:
                normalAttack()
            elif GameScript.challengeNumber == 5:
                normalAttack()

        # Normal Attack if the dice roll is less than 8
        elif totalRoll <= 7:
            normalAttack()
        else:
            pass

        if GameScript.challengeNumber == 4 and Characters.monsterHealth <= 0:
            Characters.ignarokExplosionAbility()
        else:
            pass

        # Now it's monster's turn to attack
        monsterAttack()

        # Check if someone won
        checkWinner()


