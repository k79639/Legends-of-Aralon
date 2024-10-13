'''This module is responsible for displaying the game content'''
import sys
import time
import Characters

'''This function creates a typing effect when printing a string of characters with some delay'''
def typingEffect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

'''Print game title, welcome message and a short overview of the game'''
def displayWelcome():
    #Prints the game title
    print("\n" + "\033[7m-" * 8 +" Legends of Aralon "+"-" * 8 +"\033[0m\n")

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
    typingEffect("- Special Ability: Can dodge a monster's attack once and respawn with 65% of health once.\n", 0.03)
    typingEffect("Type \033[92m'Valerius'\033[0m to embody strength and resilience,", 0.03)
    typingEffect("or \033[94m'Eldara'\033[0m to wield the power of wisdom and magic.", 0.03)

'''Oriana the storyteller's dialogues for challenge 1'''
def orianaChallenge1Intro():
    global challengeNumber, gameEnd
    typingEffect(f"\n{Characters.oriana}Greetings, hero. I am Oriana, keeper of forgotten tales and chronicler of Aralon.")
    typingEffect("        I am here to guide you on your journey and share the wisdom of the ancients.", 0.02)
    typingEffect("        A new challenge awaits you, hero. Prepare yourself for what lies ahead.\n", 0.03)
    typingEffect("        The first foe you must confront is known as \033[35mKragnar the Stoneborn\033[0m.", 0.06)
    typingEffect("        A towering beast of immense size and formidable strength.", 0.03)
    typingEffect("        Beware, hero; he can summon a shield of earth to deflect your critical attacks.", 0.03)
    typingEffect("        Choose your attacks wisely, for strategy will be key in overcoming this challenge.\n", 0.02)
    typingEffect("        \033[1mRemember, I will be here to offer guidance whenever you need it.\033[0m", 0.04)
    typingEffect("        Now, steel your resolve and prepare to face Kragnar the Stoneborn.\n", 0.03)
    challengeNumber = 1
    gameEnd = False

'''Initial dialogues before fight for challenge 1'''
def challenge1InitialDialogues():
    typingEffect("\033[35mKragnar: \033[0mSo, a hero dares to challenge me?", 0.04)
    typingEffect("         You must be brave or foolish to face the Stoneborn.\n", 0.03)
    typingEffect(f"{Characters.heroColour}{Characters.heroName}: \033[0mYou may be strong, but every stone can be shattered with enough will!")
    typingEffect("\n\033[35mKragnar: \033[0mEnough talk! Prepare to meet your end, hero!\n", 0.04)

'''Oriana the storyteller's dialogues for challenge 2'''
def orianaChallenge2Intro():
    typingEffect(f"        You've proven yourself worthy, hero. But the journey is far from over.\n")
    typingEffect("        Beyond these lands lies your next challenge: the dark forests where no light reaches.", 0.03)
    typingEffect("        It is said that a sinister force haunts these woods, a creature known only as \033[35mAzra\033[0m the Mirror Fiend.\n", 0.04)
    typingEffect("        \033[35mAzra\033[0m is not one of strength or might, but of cunning and deception.", 0.03)
    typingEffect("        \033[31mBeware,\033[0m for he can reflect your own attacks back at you, twisting your power to his advantage.\n")
    typingEffect("        Use your wits wisely, hero. The Mirror Fiend can be unpredictable.", 0.03)
    typingEffect("        But remember, every shadow has its weakness. Find it, and victory will be yours.\n", 0.04)
    typingEffect("        Prepare yourself, for what lies ahead will test not just your strength, but your mind.\n", 0.03)

'''Initial dialogues before fight for challenge 2'''
def challenge2InitialDialogues():
    typingEffect(f"{Characters.monsterName}: \033[0mAh, a brave soul ventures into my domain...")
    typingEffect("      But do you know what you face, hero?\n", 0.03)
    typingEffect(f"{Characters.heroColour}{Characters.heroName}: \033[0mI've faced worse, and I will overcome you as well!\n")
    typingEffect(f"{Characters.monsterName}: \033[0mHow amusing! But in these woods, strength matters little.")
    typingEffect(f"      The more you fight, the more you face yourself.", 0.04)
    typingEffect("      Let us see if you can handle the reflection of your own power!\n", 0.03)

'''Oriana the storyteller's dialogues for challenge 3'''
def orianaChallenge3Intro():
    typingEffect(f"        You have come far, hero, but the greatest challenge is still ahead of you.\n", 0.04)
    typingEffect("        Deep beneath the scorched lands lies a creature that feeds on life itself.", 0.03)
    typingEffect("        It is known as \033[35mMalakar, the Life Leech.\033[0m His hunger is endless, and he grows stronger with every soul he consumes.\n")
    typingEffect("        \033[35mMalakar\033[0m can drain your very essence, sapping your strength with each blow.", 0.04)
    typingEffect("        \033[31mBeware,\033[0m hero. Every strike he lands will make him more powerful, and you weaker.\n")
    typingEffect("        Only by keeping your wits and endurance can you outlast him.", 0.03)
    typingEffect("        Prepare yourself, for this battle will test your resolve like no other.\n")

'''Initial dialogues before fight for challenge 3'''
def challenge3InitialDialogues():
    typingEffect(f"{Characters.monsterName}: \033[0mAh... another soul to feast upon. How delightful.")
    typingEffect("         You will not survive this, hero. The more you fight, the more I feed.\n", 0.03)
    typingEffect(f"{Characters.heroColour}{Characters.heroName}: \033[0mI've overcome worse than you, Malakar. You won't defeat me!\n")
    typingEffect(f"{Characters.monsterName}: \033[0mFoolish mortal. ")
    typingEffect("         Your strength will wither as I grow stronger. Let us begin.\n", 0.03)

'''Oriana the storyteller's dialogues for challenge 4'''
def orianaChallenge4Intro():
    typingEffect(f"        You have overcome {Characters.monsterColor}Malakar\033[0m, but the challenges are far from over, hero.\n")
    typingEffect(f"        Your next foe awaits in the fiery depths of the mountain: {Characters.monsterColor}{Characters.monsterTitle}\033[0m.")
    typingEffect("        This creature breathes fire hotter than the sun, and its flames can turn the bravest heroes to ash.\n", 0.03)
    typingEffect("        \033[31mBe warned:\033[0m when \033[35mIgnarok\033[0m falls, it erupts in a fiery explosion, dealing damage to all nearby.", 0.04)
    typingEffect("        You must stay vigilant, as Ignarok's flames are not only fierce but unpredictable.\n", 0.03)
    typingEffect("        Only by keeping your wits and endurance can you outlast him.", 0.04)
    typingEffect("        Use your wisdom and strategy wisely, for only then can you extinguish the flames of this mighty beast.\n", 0.03)

'''Initial dialogues before fight for challenge 4'''
def challenge4InitialDialogues():
    typingEffect(f"{Characters.monsterName}: \033[0mWho dares disturb my slumber?")
    typingEffect("         Another fool seeking glory? You shall be nothing but ashes!\n", 0.03)
    typingEffect(f"{Characters.heroColour}{Characters.heroName}: \033[0mI've faced worse than you, {Characters.monsterName}!\033[0m I will not back down!\n")
    typingEffect(f"{Characters.monsterName}: \033[0mYour bravado is amusing. Prepare to feel the heat of my flames!", 0.03)

'''Oriana the storyteller's dialogues for challenge 5'''
def orianaChallenge5Intro():
    typingEffect(f"        This is it, hero. The final battle stands before you.\n")
    typingEffect(f"        Deep within the ancient ruins, the source of all darkness awaits: \033[35m{Characters.monsterTitle}\033[0m", 0.04)
    typingEffect(f"        {Characters.monsterName}\033[0m has the power to drain the life from all living things, leaving nothing but death in his wake.\n")
    typingEffect("        He is unlike any foe you've faced before, for he wields the power of the shadows themselves.", 0.03)
    typingEffect(f"        \033[31mBe warned:\033[0m {Characters.monsterName}\033[0m will double his power when his health drops below 16.\n")
    typingEffect("        This is your final test, hero. Defeat Zarok, and the kingdom of Aralon will be free from the darkness.", 0.03)
    typingEffect("        But fail... and the light will fade forever.\n")

'''Initial dialogues before fight for challenge 5'''
def challenge5InitialDialogues():
    global gameEnd 
    typingEffect(f"{Characters.monsterName}: \033[0mSo, you are the one who has been causing me trouble.", 0.04)
    typingEffect("       You think you can stop me? You are but a fleeting breath in the winds of time.\n", 0.03)
    typingEffect(f"{Characters.heroColour}{Characters.heroName}: \033[0mI won't let you destroy this kingdom, Zarok!\n")
    typingEffect(f"{Characters.monsterName}: \033[0mFoolish hero. I am death incarnate. The more you fight, the closer you come to your end.", 0.03)
    typingEffect("       I will extinguish your light, as I have done with countless others before you.", 0.03)
    gameEnd = True

'''Oriana the storyteller's final dialogues after hero'''
def orianaFinalDialogues():
    typingEffect(f"\n{Characters.oriana}You did it, hero! Zarok is defeated, and the kingdom is safe.")
    typingEffect("        Your bravery has brought light back to Aralon.\n", 0.03)
    typingEffect("        \033[1mRest now, champion. Your legend will be told for generations.\033[0m")

'''A little thank you message for the player'''
def finalMessage():
    typingEffect("\n\033[7mThank you for playing Legends of Aralon. Your journey may be over for now, but your legend will live on!\033[7m\n", 0.04)
    