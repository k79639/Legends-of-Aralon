'''This module is responsible for the mechanics of all the challenges.'''

import Characters
import Content
import random

'''This function handles the first challenge'''
def firstChallenge():
    global totalRoll, heroAttribute, heroAttributeName

    # Attribute used for this challenge
    heroAttribute = Characters.heroStrength
    heroAttributeName = "Strength"
    
    # Wakes up Kragnar
    Characters.kragnar()

    # Display initial dialogues
    Content.typingEffect("\033[35mKragnar: \033[0mSo, a hero dares to challenge me?")
    Content.typingEffect("         You must be brave or foolish to face the Stoneborn.\n")
    Content.typingEffect(f"{Characters.heroColour}{Characters.heroName}: \033[0mYou may be strong, but every stone can be shattered with enough will!")
    Content.typingEffect("\n\033[35mKragnar: \033[0mEnough talk! Prepare to meet your end, hero!\n")

    # Battle loop until one character wins
    
    while Characters.monsterHealth > 0 and Characters.heroHealth > 0:
        Content.typingEffect(input("Press Enter/Return to roll dice: "))

        diceRoll()  # Roll the dice to determine the outcome of this round

        # Critical hit
        if totalRoll >= 10: 
            damage = totalRoll

            # 50% chance for Kragnar to create a shield if he has shields left
            if Characters.kragnarTotalShields > 0 and not Characters.kragnarHasShield and random.randint(0, 1) < 0.5:
                Characters.kragnarHasShield = True
                Characters.kragnarTotalShields -= 1
                Content.typingEffect("\033[35mKragnar\033[0m summons a shield of stone to protect himself!\n")
                
                
                # Prompt to remove the shield but only once
                if Characters.heroCanRemoveShield:
                    while True:
                        removeShield = input("Do you want to use your ability to break Kragnar's shield? (yes/no): ").strip().lower()
                        if removeShield == "yes":
                            Characters.kragnarHasShield = False
                            # Apply damage after shield is broken
                            Characters.monsterHealth -= damage  
                            Content.typingEffect(f"\n{Characters.heroName} shatters {Characters.monsterName}'s\033[0m shield and deals {damage} damage!\n")
                            Content.typingEffect(f"{Characters.monsterName} has {Characters.kragnarTotalShields} shields remaining.\n")
                            Characters.monsterHealth = max(0, Characters.monsterHealth)  
                            Content.typingEffect(f"{Characters.monsterName}'s\033[0m remaining health: {Characters.monsterHealth}\n")
                            Characters.heroCanRemoveShield = False
                            break
                        
                        # If player decided not to destroy monster's shield
                        elif removeShield == "no":
                            Content.typingEffect(f"\n{Characters.heroName} decides to save their ability for now.\n")
                            Content.typingEffect(f"{Characters.monsterName}'s\033[0m shield absorbs your attack!\n")
                            Content.typingEffect(f"{Characters.monsterName} has {Characters.kragnarTotalShields} shields remaining.\n")
                            Characters.kragnarHasShield = False
                            break

                        else:
                            Content.typingEffect("\033[91mInvalid choice.\033[0m Please type 'Yes' or 'No'.\n")
                
                # If monster have a shield but hero cannot remove it.
                if not Characters.heroCanRemoveShield and Characters.kragnarHasShield:
                    Content.typingEffect("You have already used your ability to break a shield, so you cannot remove it again.\n")
                    Content.typingEffect(f"{Characters.monsterName}'s\033[0m shield absorbs your attack!\n")
                    Content.typingEffect(f"{Characters.monsterName} has {Characters.kragnarTotalShields} shields remaining.\n")
                    Characters.kragnarHasShield = False

            else:
                Characters.monsterHealth -= damage
                checkWinner()
                # Ensure that the health does not go into negative
                Characters.monsterHealth = max(0, Characters.monsterHealth)  
                Content.typingEffect(f"\nYou rolled a critical hit! {Characters.monsterName} takes {damage} damage.")
                Content.typingEffect(f"{Characters.monsterName}'s\033[0m remaining health: {Characters.monsterHealth}\n")
        
        # Normal Attack if the dice roll is less than 10
        elif totalRoll < 10:
            normalAttack()
        
        # Now it's Kragnar's turn to attack
        monsterAttack()
        
        # Check if someone won
        checkWinner()

'''This function determines the damage dealt by the hero'''
def diceRoll():
    global totalRoll
    rollResult = random.randint(0, 0)  # Rolling 2 six-sided dice
    totalRoll = rollResult + Characters.heroStrength
    Content.typingEffect(f"{Characters.heroName}\033[0m rolled a {rollResult} (Modified by your {heroAttributeName} {heroAttribute} is {totalRoll}).\n")

'''This function determines the damage dealt by the monster'''
def monsterAttack():
    monsterRoll = random.randint(8, 12)
    if monsterRoll > totalRoll:
        # Difference in rolls is the damage dealt to the hero
        monsterDamage = monsterRoll - totalRoll  
        Characters.heroHealth -= monsterDamage
        # Ensure hero's health does not go negative
        Characters.heroHealth = max(0, Characters.heroHealth)  
        Content.typingEffect(f"\n{Characters.monsterName}\033[0m strikes back and deals {monsterDamage} damage!")
        Content.typingEffect(f"\n{Characters.heroColour}{Characters.heroName}\033[0m remaining health: {Characters.heroHealth}\n")
        # Give health restore ability to Valerius
        healthRestoreAbility()

'''This function checks if someone has won'''
def checkWinner():
    if Characters.monsterHealth <= 0:
        Content.typingEffect(f"You have defeated {Characters.monsterColor}{Characters.monsterTitle}\033[0m Victory is yours!\n")
    elif Characters.heroHealth <= 0:
        Content.typingEffect(f"{Characters.heroColour}{Characters.heroName}\033[0m has been defeated. Game over.\n")

'''This function runs when the result of the dice is less than 10 / when critical damage is not delt'''
def normalAttack():
    damage = totalRoll  
    Characters.monsterHealth -= damage
    checkWinner()
    # Ensure health does not go negative
    Characters.monsterHealth = max(0, Characters.monsterHealth)  
    Content.typingEffect(f"\nYou hit {Characters.monsterColor}{Characters.monsterName}\033[0m for {damage} damage.")
    Content.typingEffect(f"\n{Characters.monsterName}'s\033[0m remaining health: {Characters.monsterHealth}\n")

'''This function gives valerius ability to restore 40% of his health twice'''
def healthRestoreAbility():
    while True:
        if Characters.selectedHero == "valerius" and Characters.healthRestore > 0 and Characters.heroHealth < 25:
            healthRestore = input("\nWould you like to use your health restoration ability now? (yes/no): ").strip().lower()
            if healthRestore == 'yes':
                Characters.heroHealth = Characters.heroHealth + 20
                Characters.healthRestore = Characters.healthRestore - 1
                Content.typingEffect(f"\n{Characters.heroColour}{Characters.heroName}\033[0m health restored to: {Characters.heroHealth}\n")
                Content.typingEffect(f"You have {Characters.healthRestore} health restoration use(s) left.\n")
                break
            elif healthRestore == 'no':
                Content.typingEffect("\nYou chose not to use your health restoration ability. The battle continues!\n")
                break
            else:
                Content.typingEffect("\n\033[91mInvalid choice.\033[0m Please type 'Yes' or 'No'.")
        else:
            break
