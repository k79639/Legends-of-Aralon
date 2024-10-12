''' This is the Main module of the game which will handel the program flow and main game script. '''
import GameScript
import Characters
import Challenges


#Welcome the user to the game 
# GameScript.displayWelcome()

#Display the characters and their attribute
# GameScript.displayOptions()

#Prompt user to select a character
Characters.selectCharacter()

#Introduce storyteller and first challenge
Characters.storyTeller()
# GameScript.orianaChallenge1Intro()

#Start the first challenge
Challenges.firstChallenge()
