from cmu_graphics import *
from control import Control

class Starter:
    onOff = 1
    finish = False  # New attribute to indicate when the start page is finished
    transitionCondition = False
    def onAppStart(self):
        print("printingawsderewrwerewr")
        app.urlPokemonBall = 'Pokebola-pokeball-png-0.png'
        app.urlPokemon = 'Starters.png'
        app.ballX = 400
        app.ballY = 600 
        app.count = 0
        app.rotate = 0 
        app.step = 0
        app.isPressedBulbasaur = False
        app.isNextScreen = False 
        app.chosenPokemon = None 
        app.pokemon_ball_blinkin = "ball_blink.gif"
        app.moveRight = True 
        app.moveLeft = False 
        app.secondBallX = app.width//2
        app.secondBallY = app.height//2+200
        app.secondBallRotation = 0
        app.myStartPageFinish = False 
        app.isNextPage = False 
        print("printingawsderewrwerewr")


    def redrawAll(self):
        if Starter.onOff ==1:
            self.drawStartPage()
            if app.isNextScreen:
                self.nextScreen()
                if app.isNextPage:
                    Starter.onOff =0
                    if Starter.finish:
                        Starter.transitionCondition = True


    def drawStartPage(self): 
        if Starter.onOff ==1:   
            drawRect(0,0,app.width,app.height,fill="white")
            imageWidth, imageHeight = getImageSize(app.urlPokemon)
            drawImage(app.urlPokemon, 400, 400, align='center', 
                    width=imageWidth//2, height=imageHeight//2)
            drawImage(app.urlPokemonBall,app.ballX,app.ballY,align = 'center',
                    width=50, height=50,rotateAngle=app.rotate)
            drawLabel("Drag the ball to the Pokemon you would like to play?? 1.Bulbasaur, 2.Charmander,3.Squirtle ",app.width//2,300)


    def nextScreen(self):
        if Starter.onOff ==1:
            drawRect(0,0,app.width,app.height,fill="white")
            chosen_text = f"The pokemon you have chosen is {app.chosenPokemon}"
            drawLabel(chosen_text,app.width//2,app.height//2,fill="black")
            drawImage(app.pokemon_ball_blinkin,app.secondBallX,app.secondBallY,align = "center",rotateAngle = app.secondBallRotation ) 

    def onMouseDrag(self,mouseX, mouseY):
        if Starter.onOff ==1:
            # This is called when the user moves the mouse
            # while it IS pressed:
            app.ballX = mouseX
            app.ballY = mouseY
            distance = (abs(200-mouseX) + abs(300-mouseY))**0.5
            app.rotate = distance *60

    def onMouseRelease(self,mouseX, mouseY):
        if Starter.onOff ==1:
            if app.ballX >=240 and app.ballX <= 340 and app.ballY >= 347 and app.ballY <= 453:
                app.isNextScreen = True
                app.chosenPokemon = "Bulbasaur"
            elif app.ballX >=341 and app.ballX <=440 and app.ballY >= 347 and app.ballY <= 453:
                app.isNextScreen = True
                app.chosenPokemon = "Charmander"
            elif app.ballX >=441 and app.ballX <=560 and app.ballY >= 347 and app.ballY <= 453:
                app.isNextScreen = True
                app.chosenPokemon = "Squirtle"

    def moveMent(self):
        if Starter.onOff ==1:
            if app.moveRight:
                app.secondBallRotation +=10
            else:
                app.secondBallRotation  -= 10


    def onStep(self):
        if Starter.onOff ==1:
            app.step +=1 
            if app.step %15 ==0: 
                if app.moveRight == True:
                    app.moveRight = False 
                    app.moveLeft  = True
                    self.moveMent()
                else:
                    app.moveRight = True 
                    app.moveLeft  = False 
                    self.moveMent()

    def onKeyPress(self,key):
        if key != None :
            Starter.onOff = 0

