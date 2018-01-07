##Variables##
import time #imported the time function enables to pause, or sleep the program
import random #imported the random function in order to enable random selections to be made
import sys #imported the sys function to enable exiting the program
hasGreen = False
hasBlue = False
hasSilver = False #Variables declared as false as the start of the program
hasGold = False
hasMagical = False
##Lists##
paths = ['left', 'ahead ','right'] #a list that will be used for randomised selection of the correct path
##Functions##
def startIntro (): ## Intro
    print ('As you wake up, you are startled as the surroundings are not that of your bedroom but that of a magically sparkling cave.')
    print ('A scenery you have never witnessed nor believed to have existed within your world. The cave appeared to be empty, as no sounds were to be heard.')
    print ('As the sleep drowsiness wore off you decided to explore this magical cave. As you look around, you notice three crystals laying on a large rock.')
    print ('You are shocked at the fact that you did not see them the first time you looked around, as they shined as brightly as a torchlight.')
    print ('Upon approaching the crystals, you decide that you are going to be taking one of them with you, as to have proof that you were in this magical cave.')
def CrystalChoices():
    choice = input("Before you are a Red, Green, and Blue crystals, which do you choose to take? : ") # Input box
    if choice == 'green': #if the user inputs green the hasGreen variable will turn true and the print will appear
        global hasGreen
        hasGreen = True
        print("You have collected the green Crystal!")
    elif choice == 'blue':#if the user inputs blue the hasBlue variable will turn true and the print will appear
        global hasBlue
        hasBlue = True
        print ("You have collected the blue Crystal!")
    elif choice == 'red':#if the user inputs red the player will lose the game and be prompted to either try again or exit the game.
        print ("As you collect the red crystal you are engufled by flame! GAME OVER")
        RestartCrystal()
    else: #a verification check, to ensure that the program does not break upon an incorrect entry, if an incorrect entry is made it will loop the function
        print ("That is not a Crystal!")
        CrystalChoices()
def IntroAct2(): #Intro
    print ('Upon picking up the crystal the rest vanish before your eyes, it startles you, but does not surprise as you have seen plenty weird things occur within this cave.')
    print ('Seeing as the cave is extremely dark you decide that the crystal would be a good lighting device and thus start scouting the caves walls, finding three different paths.')
    print ('Each path seems equally as eerie, which path do you wish to take?')
def IntroAct3 (): #Intro
    print ('Soon you were right in front of the objects that were emitting the light, and as you looked closer you saw three objects.')
    print ('One of the sparkling objects appeared to be gold, the next item seemed to be silver,')
    print ('although the third item you could not identify, it sparkled in multiple colours and was brighter than both gold and silver.')  
def PathChoices(): #while neither of the options are entered by the user
    choice = ""
    while choice != "left" and choice != "ahead" and choice !="right":
        choice = input("Before you are three paths, input the number of the one you choose to follow? : left, ahead or right? : ")
    return choice
def checkChoice (PathChoices): # when a correct option is entered it will move on to this function and randomly pick from the list 'paths' which path is correct 
    correctPath = random.choice(paths) #states that the correctPath is a random choice from 'paths' lsit
    if PathChoices == correctPath: #states that if the input is the same as the random choice then the user may move onto the next stage.
        print("As you walk down the path you are drawn towards a sparkling light coming from deep down, as you come closer, it gets brighter and brighter.")
    else: # if the ranomly selected correct path is not what the player selected they will have to restart this section.
        print("As I walk down the path to my left, I do not realise that the path does not exist and fall to my death.")
        RestartPath()
def ItemChoices(): # a function that check which item the user selects
    choice = input("Before you are three objects, Silver, Gold and a Magical Entity : ") #searches for user input
    if choice == 'silver': #if the input is 'silver' the variable hasSiler will turn from false to true
        global hasSilver
        hasSilver = True
        print("You have collected the silver object!")
    elif choice == 'gold':#if the input is 'gold' the variable hasGold will turn from false to true
        global hasGold
        hasGold = True
        print ("You have collected the golden object!")
    elif choice == 'magical entity':#if the input is 'magical entity' the variable hasMagical will turn from false to true
        global hasMagical
        hasMagical = True
        print ("You have collected the magical entity!")
    else: #a verification statement that will ensure that only one of the given options is selected
        print ("That is not one of the objects!")
        ItemChoices()
def RestartCrystal(): #restart function that enables the player to choose whether they wish to replay or exit the program
     choice = input("Do you wish to play again? yes/no : ")
     if choice == 'yes':
        startIntro()
        time.sleep(2)
        CrystalChoices()
        time.sleep(2)
     elif choice == 'no':
         sys.exit(0) #exit function (requires sys to be imported)
     else:
        print ("that is not one of the options!")
        RestartCrystal()
def RestartPath():
     choice = input("Do you wish to play again? Y/N") #same function as the previous restart, but used for a different segment of the game.
     if choice == 'Y':
        IntroAct2()
        time.sleep(2)
        choice = PathChoices()
        checkChoice(choice)
        time.sleep(2)
     elif choice == 'N':
         sys.exit(0)
     else:
        print ("that is not one of the options!")
        RestartCrystal()
def FinalIntro ():#intro
    print ("As you carry on walking down the same path you found the sparkling objects, you hear a loud ‘Roar’ up ahead.")
    print ("You are shaken, but contempt with walking forward, curious as to what else you may see in this mysterious cave.")
    print ("And right there and then you come across a large Minotaur looking creature, the creature is 10x the size of you, and has an extremely menacing look to it.")
    print ("As it notices you, it starts walking towards you.")
    print ("Frozen in place, you contemplate on what you may do with the items you have on you.")
def Final(): #final outcome, checks which variables are true and decides the fate of the player
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
        RestartCrystal()
    
            ##Act1##
startIntro()
time.sleep(5)
CrystalChoices()
time.sleep(2)
            ##Act2##
IntroAct2()
time.sleep(5)
choice = PathChoices() #set variable that will save the choice that the user has made
checkChoice(choice) #the variable will then be used to check whether the choice matches the randomly selected one.
time.sleep(2)
            ##Act3##
IntroAct3()
time.sleep(5)
ItemChoices()
time.sleep(2)
           ##ActFinal##
FinalIntro()
time.sleep(10)
Final()