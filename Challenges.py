'''This module is responsible for the mechanics of all the challenges in the.'''

import Characters
import GameScript
import random

'''This function determines the outcome of the round'''
def diceRoll():
    global totalRoll
    # Rolling 2 six-sided dice.
    rollResult = random.randint(13, 14)  
    # Calculate the outcome of the dice roll considering the attribute of the hero.
    totalRoll = rollResult + Characters.heroStrength
    GameScript.typingEffect(f"{Characters.heroColour}{Characters.heroName}\033[0m rolled a {rollResult} (Modified by your {heroAttributeName} {heroAttribute} is {totalRoll}).", 0.03)


'''This function determines the damage dealt by the monster'''
def monsterAttack():
    global monsterDamage
    monsterRoll = random.randint(10, 12)
    # Checks if monster rolled more than the hero and monster is alive or not
    if monsterRoll > totalRoll and Characters.monsterHealth > 0:
        # Difference in rolls is the damage dealt to the hero
        monsterDamage = monsterRoll - totalRoll  
        Characters.heroHealth -= monsterDamage
        # Ensure hero's health does not go negative
        Characters.heroHealth = max(0, Characters.heroHealth)  
        GameScript.typingEffect(f"{Characters.monsterName}\033[0m strikes back and deals {monsterDamage} damage!", 0.04)
        Characters.eldaraDodgeAbility()
        GameScript.typingEffect(f"\n{Characters.heroColour}{Characters.heroName}\033[0m remaining health: {Characters.heroHealth}\n", 0.03)
        # Give health restore ability to Valerius
        Characters.valeriusHealthRestoreAbility()
        Characters.eldaraRespawnAbility()


'''This function checks if someone has won'''
def checkWinner():
    if Characters.monsterHealth <= 0:
        GameScript.typingEffect(f"{Characters.oriana}You have defeated {Characters.monsterColor}{Characters.monsterTitle}\033[0m Victory is yours!\n")
    elif Characters.heroHealth <= 0:
        GameScript.typingEffect(f"{Characters.heroColour}{Characters.heroName}\033[0m has been defeated. Game over.\n")


'''This function runs when the result of the dice is less than 10 / when critical damage is not delt'''
def normalAttack():
    global damage
    damage = totalRoll  
    Characters.monsterHealth -= damage
    # Ensure health does not go negative
    Characters.monsterHealth = max(0, Characters.monsterHealth)  
    GameScript.typingEffect(f"\n{Characters.heroColour}{Characters.heroName}\033[0m hit {Characters.monsterColor}{Characters.monsterName}\033[0m for {damage} damage.", 0.03)
    GameScript.typingEffect(f"\n{Characters.monsterName}'s\033[0m remaining health: {Characters.monsterHealth}\n", 0.03)


'''This function handles the first challenge'''
def firstChallenge():
    global totalRoll, heroAttribute, heroAttributeName, damage

    # Attribute used for this challenge
    heroAttribute = Characters.heroStrength
    heroAttributeName = "Strength"
    
    # Wakes up the monster for the round
    Characters.kragnar()

    # Display initial dialogues
    GameScript.typingEffect("\033[35mKragnar: \033[0mSo, a hero dares to challenge me?", 0.04)
    GameScript.typingEffect("         You must be brave or foolish to face the Stoneborn.\n", 0.03)
    GameScript.typingEffect(f"{Characters.heroColour}{Characters.heroName}: \033[0mYou may be strong, but every stone can be shattered with enough will!")
    GameScript.typingEffect("\n\033[35mKragnar: \033[0mEnough talk! Prepare to meet your end, hero!\n")

    # Battle loop until one character wins
    while Characters.monsterHealth > 0 and Characters.heroHealth > 0:
        GameScript.typingEffect(input("\nPress Enter/Return to roll dice: "))

        diceRoll()  # Roll the dice to determine the outcome of this round

        # Critical hit
        if totalRoll >= 10: 
            damage = totalRoll
            Characters.kragnarShieldAbility()

        # Normal Attack if the dice roll is less than 10
        elif totalRoll < 10:
            normalAttack()

        # Now it's monster's turn to attack
        monsterAttack()

        # Check if someone won
        checkWinner()


