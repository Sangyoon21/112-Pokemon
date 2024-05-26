from cmu_graphics import *

class SaliorNPC:
    #when we met a salior NPC it asks to play a game and when we win the game we 
    #we are able to change the pokeom
    exit = False 
    goLeft = False 
    goGame = False 
    def onAppStart(self):
        app.salior = "saliorNPC.png"
        # app.chrBackSal = "chrBack.png"
        app.charSalX = 300
        app.charSalY = 690
        app.saliorStep = 20
        app.chrFrontSal = "chrFront.png"
        app.chrLeftSal = "chrLeft.png"
        app.chrBackSal = "chrBack.png"
        app.chrRightSal = "chrRight.png"
        app.chrStatusSal = app.chrBackSal
        app.rockRoad = "rockRoad.png"
        app.startTalkSal = False 
        app.salTalk = 0

    def redrawAll(self):
        drawImage("waterBackGround.png",0,0)
        drawImage("bridge.png",300,250,width = 250)
        drawImage(app.salior,350,200)
        drawImage(app.chrStatusSal,app.charSalX,app.charSalY,width = 100,height = 100)

        if app.startTalkSal == True:
            #NPC conversations 
            hpInnerBox = rgb(193,193,193)
            drawRect(100,600,600,180,fill = "gray",border = hpInnerBox,borderWidth = 5)
            if app.salTalk ==0:
                drawLabel("Hello, young trainer!Welcome to Water City!!",400,680,size = 17,align = "center")
                drawLabel("Press 0 to continue...",400,750,size = 17,align = "center",fill = "white")

            if app.salTalk ==1:
                drawLabel("You could earn a new Pokemon when you win this game!!",400,680,size = 17,align = "center")
                drawLabel("Press 1 to continue...",400,750,size = 17,align = "center",fill = "white")

            if app.salTalk ==2:
                drawLabel("Do you want to play this game?",400,680,size = 17,align = "center")
                drawLabel("Press y to play the game and press n to not",400,700,size = 17,align = "center")

            if app.salTalk ==3:
                drawLabel("Oh okay! Then good bye",400,680,size = 17,align = "center")
                drawLabel("Press e  to exit",400,750,size = 17,align = "center",fill = "white")

            if app.salTalk ==4:
                drawLabel("Alright!! Let's play then",400,680,size = 17,align = "center")
                drawLabel("Press p  to start the game",400,750,size = 17,align = "center",fill = "white")


    def onKeyHold(self,key):
        oldX, oldY = app.charSalX, app.charSalY
        if  "up" in key and app.charSalY!=0:
            app.charSalY -=app.saliorStep
            if app.chrStatusSal == app.chrLeftSal or app.chrStatusSal == app.chrRightSal:
                app.chrStatusSal = app.chrBackSal

            if app.chrStatusSal ==app.chrFrontSal:
                app.chrStatusSal = app.chrBackSal


        if "down" in key and app.charSalY!=app.height-app.saliorStep :
            app.charSalY +=app.saliorStep
            if app.chrStatusSal == app.chrLeftSal or app.chrStatusSal == app.chrRightSal:
                app.chrStatusSal = app.chrFrontSal

            if app.chrStatusSal ==app.chrBackSal:
                app.chrStatusSal = app.chrFrontSal

            
        if "right" in key and app.charSalX!= app.width-app.saliorStep:
            app.charSalX +=app.saliorStep
            if app.chrStatusSal == app.chrFrontSal or app.chrStatusSal == app.chrBackSal:
                app.chrStatusSal = app.chrRightSal

            if app.chrStatusSal == app.chrLeftSal:
                app.chrStatusSal = app.chrRightSal
        if  "left" in key  and app.charSalX!=0 :
            app.charSalX -=app.saliorStep
            if app.chrStatusSal == app.chrFrontSal or app.chrStatusSal == app.chrBackSal:
                app.chrStatusSal = app.chrLeftSal

            if app.chrStatusSal == app.chrRightSal:
                app.chrStatusSal = app.chrLeftSal

      #check so its doesn't go over the bridge
        if self.isOnBridgeY(app.charSalY):
            app.charSalY = oldY

        if self.isOnBridgeX(app.charSalX):
            app.charSalX = oldX

        if self.isCollision(app.charSalX,app.charSalY,100,100,350,200,138,106):
            app.charSalX = oldX
            app.charSalY = oldY
            app.startTalkSal = True





    def onKeyPress(self,key):
        if key =="0" and app.salTalk ==0:
            app.salTalk =1 

        if key =="1" and app.salTalk ==1:
            app.salTalk =2 

        if key == "n" and app.salTalk==2:
            app.salTalk = 3

        if key =="y" and app.salTalk ==2:
            app.salTalk = 4

        if key =="p" and app.salTalk ==4:
            self.goGame = True
            app.charSalX = 300
            app.charSalY = 690
            app.saliorStep = 20
            # app.chrFrontSal = "chrFront.png"
            # app.chrLeftSal = "chrLeft.png"
            # app.chrBackSal = "chrBack.png"
            # app.chrRightSal = "chrRight.png"
            app.chrStatusSal = app.chrBackSal
            # app.rockRoad = "rockRoad.png"
            app.startTalkSal = False 
            app.salTalk = 0 

        if key =="e" and app.salTalk ==3:
            self.exit = True
            app.charSalX = 300
            app.charSalY = 690
            app.saliorStep = 20
            # app.chrFrontSal = "chrFront.png"
            # app.chrLeftSal = "chrLeft.png"
            # app.chrBackSal = "chrBack.png"
            # app.chrRightSal = "chrRight.png"
            app.chrStatusSal = app.chrBackSal
            # app.rockRoad = "rockRoad.png"
            app.startTalkSal = False 
            app.salTalk = 0

    



    

    def isOnBridgeY(self,y):
        # Assuming the bridge is in a specific range, modify as neede
        return  y <250 or y >720
    def isOnBridgeX(self,x):
        return 300 > x or x> 400

    def isCollision(self,x1, y1, w1, h1, x2, y2, w2, h2):
            return (x1 < x2 + w2) and (x1 + w1 > x2) and (y1 < y2 + h2) and (y1 + h1 > y2)
        






