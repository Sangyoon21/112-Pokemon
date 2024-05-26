from cmu_graphics import *
import p 

class SaliorGameWIn:
    # we are able to change the pokemon to Gyarados
    # also interacts with the NPC 
    goExit = False 
    def onAppStart(self):
        app.salior = "saliorNPC.png"
        # app.chrBackSal = "chrBack.png"
        app.charSalWinX = 350
        app.charSalWinY = 300
        app.saliorStep = 20
        app.chrFrontSal = "chrFront.png"
        app.chrLeftSal = "chrLeft.png"
        app.chrBackSal = "chrBack.png"
        app.chrRightSal = "chrRight.png"
        app.chrStatusSal = app.chrBackSal
        app.rockRoad = "rockRoad.png"
        # app.startTalkWin = False 
        app.winTalk = 0

    def redrawAll(self):
        drawImage("waterBackGround.png",0,0)
        drawImage("bridge.png",300,250,width = 250)
        drawImage(app.salior,350,200)
        drawImage(app.chrStatusSal,app.charSalWinX,app.charSalWinY,width = 100,height = 100)
        hpInnerBox = rgb(193,193,193)
        drawRect(100,600,600,180,fill = "gray",border = hpInnerBox,borderWidth = 5)
        if app.winTalk ==0:
            drawLabel("Oh you won the game!!! Good job!!",400,680,size = 17,align = "center")
            drawLabel("Press 0 to continue...",400,750,size = 17,align = "center",fill = "white")
        if app.winTalk ==1:
            drawLabel("You can choose if you want to change your Pokemon to Gyarados",400,680,size = 17,align = "center")
            drawLabel("Would you like to change or keep with your Pokemon now",400,720,size = 17,align = "center")
            drawLabel("Press 1 to continue...",400,750,size = 17,align = "center",fill = "white")
        if app.winTalk ==2:
            drawLabel("Think Enough!! You cannot change back",400,680,size = 17,align = "center")
            drawLabel("Press y to change or n to not change",400,750,size = 17,align = "center",fill = "white")

        if app.winTalk ==3:
            drawLabel("Okay player!!You might visit the next",400,680,size = 17,align = "center")
            drawLabel("stadium where you could fight with me!",400,720,size = 17,align = "center")
            drawLabel("Press e to exit",400,750,size = 17,align = "center", fill = "white")

        if app.winTalk ==4:
            drawLabel("Good Choice your Pokemon is now Gyarados!!",400,680,size = 17,align = "center")
            p.pokemonChosen = p.Gyarados
            # p.name = "Gyarados"
            drawLabel("Press space to continue",400,750,size = 17,align = "center",fill = "white")

    

    def onKeyPress(self,key):
       if key == "0" and app.winTalk ==0:
            app.winTalk = 1
            
       if key =="1" and app.winTalk ==1:
            app.winTalk =2 
            
       if key =="n" and app.winTalk ==2:
            app.winTalk = 3

       if key =="y" and app.winTalk ==2:
            app.winTalk = 4 

       if key =="e" and app.winTalk ==3:
            app.winTalk = 0
            self.goExit = True 
            #exit here in the class 

       if key =="space" and app.winTalk ==4:
            app.winTalk = 3



       