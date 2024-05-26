from cmu_graphics import *
import random


def onAppStart(app):
    backgroundColor = rgb(90, 90, 113)
    app.background = backgroundColor
    app.loadingImage = "loading.png"
    app.loadImageX = 250
    app.loadImageY = 200
    app.stepInfo = 0


def redrawAll(app):
    drawImage(app.loadingImage,app.loadImageX,app.loadImageY )
    drawLabel("Did You Know the first Pokemon Game in already 27??", 400 ,400, font = "monospace", size = 25,fill = "white")
    drawLabel("There are over 1000 species of Pokémon!", 400,440,font = "monospace", size = 25,fill = "white")
    drawLabel("Pokémon means 'Pocket Monsters'",400,480,font = "monospace", size = 25,fill = "white")
    drawLabel("If you didn't chosee the poemon at the choosing phase'",400,530,font = "monospace", size = 23,fill = "white")
    drawLabel("You would have a pokemon as your Pokemon!!(Hidden piece)",400,570,font = "monospace", size = 23,fill = "white")
    drawLabel("Press any button to continue",400,660,font = "monospace", size = 23,fill = "white")

    
    
    

def onStep(app):
    app.stepInfo +=1
    if app.stepInfo %30==0:
        app.loadImageY +=5
    if app.stepInfo % 50 ==0:
        app.loadImageY -=5


        


runApp(800,800)