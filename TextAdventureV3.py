##Variables##
import time
import random
hasGreen = False
hasBlue = False
hasSilver = False
hasGold = False
hasMagical = False
##Functions##
def startIntro ():
    print ('As you wake up, you are startled as the surroundings are not that of your bedroom but that of a magically sparkling cave.')
    print ('A scenery you have never witnessed nor believed to have existed within your world. The cave appeared to be empty, as no sounds were to be heard.')
    print ('As the sleep drowsiness wore off you decided to explore this magical cave. As you look around, you notice three crystals laying on a large rock.')
    print ('You are shocked at the fact that you did not see them the first time you looked around, as they shined as brightly as a torchlight.')
    print ('Upon approaching the crystals, you decide that you are going to be taking one of them with you, as to have proof that you were in this magical cave.')
def CrystalChoices():
    choice = input("Before you are a Red, Green, and Blue crystals, which do you choose to take? : ")
    if choice == 'Green':
        global hasGreen
        hasGreen = True
        print("You have collected the green Crystal!")
    elif choice == 'Blue':
        global hasBlue
        hasBlue = True
        print ("You have collected the blue Crystal!")
    elif choice == 'Red':
        print ("As you collect the red crystal you are engufled by flame! GAME OVER")
        RestartRed()
    else:
        print ("That is not a Crystal!")
        CrystalChoices()
def IntroAct2():
    print ('Upon picking up the crystal the rest vanish before your eyes, it startles you, but does not surprise as you have seen plenty weird things occur within this cave.')
    print ('Seeing as the cave is extremely dark you decide that the crystal would be a good lighting device and thus start scouting the caves walls, finding three different paths.')
    print ('Each path seems equally as eerie, which path do you wish to take?')
def IntroAct3 ():
    print ('Soon you were right in front of the objects that were emitting the light, and as you looked closer you saw three objects.')
    print ('One of the sparkling objects appeared to be gold, the next item seemed to be silver,')
    print ('although the third item you could not identify, it sparkled in multiple colours and was brighter than both gold and silver.')  
def PathChoices():
    choice = input("Before you are three paths, Which do you choose to follow? : Left, Ahead or Right?")
    if choice == 'Left':
        print("As I walk down the path to my left, I do not realise that the path does not exist and fall to my death.")
        RestartRed()
    if choice == 'Y':
        startIntro()
    elif choice == 'N':
        quit
    elif choice == 'Ahead':
        print ("As you walk down the path you are drawn towards a sparkling light coming from deep down, as you come closer, it gets brighter and brighter.")
    elif choice == 'Right':
        print ("As you walk down the path you are drawn towards a sparkling light coming from deep down, as you come closer, it gets brighter and brighter.")
    else:
        print ("That is not one of the paths!")
        PathChoices()
def ItemChoices():
    choice = input("Before you are three objects, Silver, Gold and a Magical Entity : ")
    if choice == 'Silver':
        global hasSilver
        hasSilver = True
        print("You have collected the silver object!")
    elif choice == 'Gold':
        global hasGold
        hasGold = True
        print ("You have collected the golden object!")
    elif choice == 'Magical entity':
        global hasMagical
        hasMagical = True
        print ("As have collected the magical entity!")
    else:
        print ("That is not one of the objects!")
        ItemChoices()
def RestartRed():
     choice = input("Do you wish to play again? Y/N")
     if choice == 'Y':
         startIntro()
         CrystalChoices()
     elif choice == 'N':
         quit
     else:
        print ("that is not one of the options!")
        RestartRed()
def FinalIntro ():
    print ("As you carry on walking down the same path you found the sparkling objects, you hear a loud ‘Roar’ up ahead.")
    print ("You are shaken, but contempt with walking forward, curious as to what else you may see in this mysterious cave.")
    print ("And right there and then you come across a large Minotaur looking creature, the creature is 10x the size of you, and has an extremely menacing look to it.")
    print ("As it notices you, it starts walking towards you.")
    print ("Frozen in place, you contemplate on what you may do with the items you have on you.")
def Final():
    if hasGreen == True and hasMagical == True:
        print("You place the 2 mystical items you have found, and a green light shoots out from where u stand, a magical fairy appears and grants you the power of nature.")
        print("With this newly acquired power you use it to collapse the cave onto the minotaur, thus defeating him.")
        print("Upon defeat of the minotaur you are brought back to your own world, in the familiar surrounding of your own bedroom, in your own bed. The End")
    elif hasBlue == True and hasMagical == True:
        print ("You place the 2 mystical items you have found, and a blue light shoots out from where u stand, a magical fairy appears and grants you the power of water.")
        print (". With this newly acquired power you use it to trap the minotaur within a gigantic water bubble where he gasps for air and drowns.")
        print ("Upon defeat of the minotaur you are brought back to your own world, in the familiar surroundings of your own bedroom, in your own bed. The end")
    else:
        print ("You place the 2 mystical items you have found, but nothing appears to happen.")
        print ("The minotaur makes a loud noise, which sounds as if he’s laughing at you.")
        print ("And a voice appears inside your head which says “Gold/Silver is what you took, now suffer for your greed you crook”.")
        print ("As the minotaur approaches you he gobbles you up whole and you are forever gone. The end")
        RestartRed()
    
            ##Act1##
startIntro()
time.sleep(2)
CrystalChoices()
time.sleep(2)
            ##Act2##
IntroAct2()
time.sleep(2)
PathChoices()
time.sleep(2)
            ##Act3##
IntroAct3()
time.sleep(2)
ItemChoices()
time.sleep(2)
           ##ActFinal##
FinalIntro()
time.sleep(2)
Final()