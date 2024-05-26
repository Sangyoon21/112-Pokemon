#import the different files into the main file
from cmu_graphics import *
from npcStarter import TitlePage
from startPage import Starter
from map import Map
from pokemonCenter import PokemonCenter
from pokemonStadium import PokemonStadium
from fightStadium import FightStadium 
from fightingScene import FightingScence
from mapRight import MapR
from saliorNPC import SaliorNPC
from saliorGame import SaliorGame
from saliorGameWin import SaliorGameWIn
from saliorStadium import SaliorStadium
from brockBadge import BrockBadge
from saliorBadge import SaliorBadge
from mapLeft import MapLeft 
from hicker import HickerNPC
from hickerFight import HigherFight
from hickerBadge import HickerBadge
from end import End
import p
import json


myTitlePage = TitlePage()
myStartPage = Starter()
myMap = Map()
myPokemonCenter = PokemonCenter()
myPokemonStadium = PokemonStadium()
myFightStadium = FightStadium()
myFightingScence = FightingScence()
myMapR = MapR ()
mySaliorNPC = SaliorNPC()
mySaliorGame = SaliorGame()
mySaliorGameWin = SaliorGameWIn()
mySaliorStadium = SaliorStadium()
myBrockBadge = BrockBadge()
mySaliorBadge = SaliorBadge()
myMapLeft = MapLeft()
myHickerNPC = HickerNPC()
myHickerFight = HigherFight()
myHickerBadge = HickerBadge()
myEnd = End()
#p.control is the thing that controls the phase 
p.control = -1


def onAppStart(app):
    #calling all of the onAppstart 
    # l = [p.control,p.name,p.health]


    # p.loadtedData()
    myTitlePage.onAppStart()
    myStartPage.onAppStart()
    myMap.onAppStart()
    myPokemonCenter.onAppStart()
    myPokemonStadium.onAppStart()
    myFightStadium.onAppStart()
    myFightingScence.onAppStart()
    myMapR.onAppStart()
    mySaliorNPC.onAppStart()
    mySaliorGame.onAppStart()
    mySaliorGameWin.onAppStart()
    mySaliorStadium.onAppStart()
    myBrockBadge.onAppStart()
    mySaliorBadge.onAppStart()
    myMapLeft.onAppStart()
    myHickerNPC.onAppStart()
    myHickerFight.onAppStart()
    myHickerBadge.onAppStart()
    myTitlePage.onAppStart()

# p = -1: titlePage, p = 0:starterPage, p =1:map , p = 1.1: mapR, p = 2: pkcenter ,p=3: stadium 
# p=4: fightStadium, p=5: fightingscence, p=1.2: mySlionarNPc, p=1.3: subGame, p = 1.4: chose pk - water 
#p = 1.5: rightStadium enter,  p =1.5: brockBadge page, p=1.6: saliorPage page, p= 7: leftMap
#p=7.1: hickerPage, p =7.2: hicker Fighting scence, p = 7.3: hicker badge , p= 42: The End!!
def redrawAll(app):
    # global p.control
    # drawing the features depending what is the p value 
    if p.control == -1:
        myTitlePage.redrawAll()
        # print("this is printingg for mttitlepage")
    if p.control == 0:
        myStartPage.redrawAll()
        # p.loadtedData() 
    if p.control == 1:
        myMap.redrawAll()
    if p.control ==1.1:
        myMapR.redrawAll()
    if p.control ==2:
        myPokemonCenter.redrawAll()
    if p.control ==3:
        myPokemonStadium.redrawAll()
    if p.control ==4:
        myFightStadium.redrawAll()
    if p.control ==5:
        myFightingScence.redrawAll()
    if p.control ==1.2:
        mySaliorNPC.redrawAll()
    if p.control ==1.3:
        mySaliorGame.redrawAll()
    if p.control ==1.4:
        mySaliorGameWin.redrawAll()
    if p.control ==1.5:
        mySaliorStadium.redrawAll()
    if p.control ==1.6:
        myBrockBadge.redrawAll()
    if p.control ==1.7:
        mySaliorBadge.redrawAll()
    if p.control ==7:
        myMapLeft.redrawAll()
    if p.control ==7.1:
        myHickerNPC.redrawAll()
    if p.control ==7.2:
        myHickerFight.redrawAll()
    if p.control ==7.3:
        myHickerBadge.redrawAll()
    if p.control ==42:
        myEnd.redrawAll()






def onMouseDrag(app, mouseX, mouseY):
    # global p.control
    if p.control == 0:
        myStartPage.onMouseDrag(mouseX, mouseY)

def onMouseRelease(app, mouseX, mouseY):
    # global p.control
    if p.control == 0:
        myStartPage.onMouseRelease(mouseX, mouseY)

    # if myStartPage.pokemonChosen == "Bulbasaur":
    #     p.pokemonChosen = p.Bulbasaur
    


def onStep(app):

    #control onstep funciton 
    if p.control == 0:
        myStartPage.onStep()

        #Check if myStartPage has finished, and transition to the map page
        if myStartPage.finish:
            p.control = 1
    if myMap.pokemonCenterColide == True:
        p.control = 2
        myMap.pokemonCenterColide = False 
    # if p.control ==2:
    #     myPokemonCenter.onStep()
    if p.control ==3:
        myPokemonStadium.onStep()
    if p.control ==5:
        #print("this is printing in main line 92")
        myFightingScence.onStep()

    if p.control ==1.3:
        mySaliorGame.onStep()

    if p.control ==1.5:
        mySaliorStadium.onStep()
    #control when we go to the next page or go back to the map
    if myTitlePage.goToStart ==True:
        p.control = 0 
        myTitlePage.goToStart = False 

    #controlling te value of p by chaking if we enter the vulding or we are out 
    if myPokemonCenter.end ==True:
        p.control = 1
        myPokemonCenter.end = False

    if myMap.pokemonStadiumColide == True:
        p.control = 3
        myMap.pokemonStadiumColide = False 

    if myMapR.pokemonCenterColide == True:
        p.control = 2
        myMapR.pokemonCenterColide= False 

    if myPokemonStadium.pageEnd == True:
        p.control = 1
        myPokemonStadium.pageEnd = False

    if myMap.fightStadiumColide == True and p.health >0:
        p.control = 4
        myMap.fightStadiumColide = False 

    if myFightStadium.fightStadiumEnd == True:
        p.control = 1
        myFightStadium.fightStadiumEnd = False 

    if myFightStadium.goFight == True:
        p.control =5
        myFightStadium.goFight = False 

    if myFightingScence.endWin == True:
        p.control = 1.6
        myFightingScence.endWin = False
    if myFightingScence.endLost == True:
        p.control = 1
        myFightingScence.endLost = False 

    if myMapR.saliorCenterColide == True:
        p.control = 1.2
        myMapR.saliorCenterColide = False 

    if mySaliorNPC.exit ==True:
        p.control =1.1 
        mySaliorNPC.exit = False 

    if mySaliorNPC.goGame ==True:
        p.control = 1.3 
        mySaliorNPC.goGame = False 

    if mySaliorGame.lose == True:
        p.control = 1.1
        mySaliorGame.lose = False 

    if mySaliorGame.win ==True:
        p.control = 1.4 
        mySaliorGame.win = False 

    if mySaliorGameWin.goExit == True:
        p.control = 1.1
        mySaliorGameWin.goExit = False 

    if myMapR.saliorStadiumColide ==True  and p.health >0:
        p.control = 1.5
        myMapR.saliorStadiumColide = False 

    if mySaliorStadium.battleEndLose == True:
        p.control =1.1
        mySaliorStadium.battleEndLose = False 

    if mySaliorStadium.battleEndWin == True:
        p.control = 1.7
        mySaliorStadium.battleEndWin = False 
    if mySaliorBadge.goExitSB ==True:
        p.control = 1.1
        mySaliorBadge.goExitSB = False 

    if myBrockBadge.exitBB == True:
        p.control =1
        myBrockBadge.exitBB = False 

    if myMapLeft.pokemonCenter2ColideL == True:
        p.control = 2
        myMapLeft.pokemonCenter2ColideL = False 

    if myMapLeft.hickerHouseColideL == True:
        p.control = 7.1
        myMapLeft.hickerHouseColideL = False 

    if myHickerNPC.exitHick ==True:
        p.control = 7
        myHickerNPC.exitHick = False 

    if myMapLeft.stadiumYColideL ==True and  p.health >0:
        p.control = 7.2
        myMapLeft.stadiumYColideL  = False 

    if p.control ==7.2:
        myHickerFight.onStep()

    if myHickerFight.battleEndLoseH == True:
        p.control = 7
        myHickerFight.battleEndLoseH = False 

    if myHickerFight.battleEndWinH == True:
        p.control = 7.3
        myHickerFight.battleEndWinH = False 

    if myHickerBadge.goExitHB == True:
        p.control = 7
        myHickerBadge.goExitHB = False 

    if p.control ==7.3:
        myHickerBadge.onStep()

    if p.control ==1.6:
        myBrockBadge.onStep()

    if p.control ==1.7:
        mySaliorBadge.onStep()

    if p.badgeCollect =={'Hicker', 'Brock', 'Salior'}:
        p.control = 42

    

    





def onKeyPress(app, key):
    #control onkeypress with control here 
    #check the my___ to see what phase we are in 
    if p.control == -1:
        myTitlePage.onKeyPress(key)
    # global p.control
    if p.control == 0:
        myStartPage.onKeyPress(key)
        # Check if a condition is met to transition to the map page
        if myStartPage.transitionCondition:
            p.control = 1

    if p.control ==2:
        myPokemonCenter.onKeyPress(key)

    if p.control ==3:
        myPokemonStadium.onKeyPress(key)

    if p.control ==4:
        myFightStadium.onKeyPress(key)

    if p.control ==5:
        myFightingScence.onKeyPress(key)

    if p.control ==1.2:
        mySaliorNPC.onKeyPress(key)

    if p.control ==1.3:
        mySaliorGame.onKeyPress(key)
    if p.control ==1.4:
        mySaliorGameWin.onKeyPress(key)
    if p.control ==1.5:
        mySaliorStadium.onKeyPress(key)
    
    if p.control ==1.6:
        myBrockBadge.onKeyPress(key)

    if p.control ==1.7:
        mySaliorBadge.onKeyPress(key)

    if p.control ==7.1:
        myHickerNPC.onKeyPress(key)

    if  p.control ==7.2:
        myHickerFight.onKeyPress(key)

    if p.control == 7.3:
        myHickerBadge.onKeyPress(key)

    # if key =="s":
    #         l = [p.control,p.health]
    #         p.saveData(l,p.name)
    #         p.loadtedData()
    
    

def onKeyHold(app,key):
     #control onKeyHold with control here 
    #check the my___ to see what phase we are in 
    if p.control ==1:
        myMap.onKeyHold(key)

        if myMap.goRight == True:
            myMap.goRight = False 
            p.control = 1.1

        if myMap.goLeft == True:
            myMap.goLeft = False 
            p.control = 7

    if p.control ==1.1:
        myMapR.onKeyHold(key)

        if myMapR.goLeft == True:
            myMapR.goLeft = False 
            p.control = 1

    if p.control ==7:
        myMapLeft.onKeyHold(key)
        if myMapLeft.goRightL == True:
            myMapLeft.goRightL = False 
            p.control = 1





    if p.control ==1.2:
        mySaliorNPC.onKeyHold(key)


 





def isCollision(app, x1, y1, w1, h1, x2, y2, w2, h2):
    #check if we had some collision
    if p.control ==1:
        myMap.isCollision(x1, y1, w1, h1, x2, y2, w2, h2)
    if p.control ==3:
        myPokemonStadium.isCollision(x1, y1, w1, h1, x2, y2, w2, h2)


def onMousePress(app,x,y):
    #call the mouse presses depending on the different p values and the phases 
    if p.control ==2:
        myPokemonCenter.onMousePress(x,y)

    if p.control ==5:
        myFightingScence.onMousePress(x,y)

    if p.control ==1.3:
        mySaliorGame.onMousePress(x,y)

    if p.control ==1.5:
        mySaliorStadium.onMousePress(x,y)

    if p.control ==7.2:
        myHickerFight.onMousePress(x,y)


        



runApp(800, 800)