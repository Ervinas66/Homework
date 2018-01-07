								#### Library ####
#### Variables ####

import random
import time
#### Lists #### []
CrystalsCorrect = ['Green Crystal','green','Green','green crystal', 'Blue Crystal','blue','Blue','blue crystal']
CrystalsIncorrect = ['Red Crystal', 'red', 'Red', 'red crystal']
#### Tuples #### ()
Pathscorrect_tpl = ('Left', 'Centre', 'Right')
#### Dictionary #### {}

#### Functions ####
def crystalChoice ():
    crystalChoice = str(input("Before you are a Red, Green, and Blue crystals, Which one do you wish to take?  : "))
    if crystalChoice in CrystalsCorrect:
        print ("You have collected the green crystal!")
    else:
        print ("That is not a Crystal!")
        return crystalChoice
def startIntro ():
    print ('As you wake up, you are startled as the surroundings are not that of your bedroom but that of a magically sparkling cave.')
    print ('A scenery you have never witnessed nor believed to have existed within your world. The cave appeared to be empty, as no sounds were to be heard.')
    print ('As the sleep drowsiness wore off you decided to explore this magical cave. As you look around, you notice three crystals laying on a large rock.')
    print ('You are shocked at the fact that you did not see them the first time you looked around, as they shined as brightly as a torchlight.')
    print ('Upon approaching the crystals, you decide that you are going to be taking one of them with you, as to have proof that you were in this magical cave.')
def Intro ():
    print ('Upon picking up the crystal the rest vanish before your eyes, it startles you, but does not surprise as you have seen plenty weird things occur within this cave.')
    print ('Seeing as the cave is extremely dark you decide that the crystal would be a good lighting device and thus start scouting the caves walls, finding three different paths.')
    print ('Each path seems equally as eerie, which path do you wish to take?')
def Act2_intro ():
      print ('Soon you were right in front of the objects that were emitting the light, and as you looked closer you saw three objects.')
      print ('One of the sparkling objects appeared to be gold, the next item seemed to be silver,')
      print ('although the third item you could not identify, it sparkled in multiple colours and was brighter than both gold and silver.')   
    #### Act 1 ####
startIntro ()
time.sleep(2)

crystalChoice()

time.sleep(2)
Intro()
PathChoice = str(input("The three paths are to your Left, in front of you (Centre) and to your Right: "))
if PathChoice in Pathscorrect_tpl:
    correctpath = random.choice(Pathscorrect_tpl) ## Randomly selects the correct path, each playthrough will have different correct option
    if PathChoice == correctpath:
        print ('As you walk down the path you are drawn towards a sparkling light coming from deep down, as you come closer, it gets brighter and brighter.')
    else:
        print ('As I walk down the path, I do not realise that the path does not exist and fall to my death.')
								#### Act 2 ####
Act2_intro()
time.sleep(2)

								#### Act 3 (Finale) ####
