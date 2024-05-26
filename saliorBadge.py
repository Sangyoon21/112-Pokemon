from cmu_graphics import *
import p 

class SaliorBadge:
    goExitSB = False 
    def onAppStart(self):
        # we are getiing the salior's badge after we win the battle and also interact with the NPC 
        app.saliorSB = "saliorNPC.png"
        # app.chrBackSal = "chrBack.png"
        app.charSalWinXSB = 350
        app.charSalWinYSB = 300
        app.saliorSBStep = 20
        app.chrFrontSalSB = "chrFront.png"
        app.chrLeftSalSB = "chrLeft.png"
        app.chrBackSalSB = "chrBack.png"
        app.chrRightSalSB = "chrRight.png"
        app.chrStatusSalSB = app.chrBackSal
        app.rockRoadSB = "rockRoad.png"
        app.saliorBadge = "badgeSalior.png"
        # app.startTalkWin = False 
        app.winTalkSB = 0
        app.angleSB = 0
        app.moveRightSB = True
        app.moveLeftSB = False 
        app.stepSB = 0

    def redrawAll(self):
        drawImage("waterBackGround.png",0,0)
        drawImage("bridge.png",300,250,width = 250)
        drawImage(app.saliorSB,350,200)
        drawImage(app.chrStatusSal,app.charSalWinXSB,app.charSalWinYSB,width = 100,height = 100)
        hpInnerBox = rgb(193,193,193)
        drawRect(100,600,600,180,fill = "gray",border = hpInnerBox,borderWidth = 5)
        if app.winTalkSB ==0:
            drawLabel("Oh you won the batttle with me goodJob!!",400,680,size = 17,align = "center")
            drawLabel("Press 0 to continue...",400,750,size = 17,align = "center",fill = "white")
        if app.winTalkSB ==1:
            drawLabel("Congrulats you earn this badge",400,680,size = 17,align = "center")
            drawLabel("Press 1 to continue...",400,750,size = 17,align = "center",fill = "white")
        if app.winTalkSB ==2:
            drawRect(0,0,800,800,fill= "skyBlue")
            drawImage(app.saliorBadge,250,200,width = 300, height = 300,rotateAngle = app.angleSB)
            drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
            drawLabel("Look at the Badge!",400,680,size = 17,align = "center")
            drawLabel("Press 2 to continue..",400,750,size = 17,align = "center",fill = "white")

        if app.winTalkSB ==3:
            drawLabel("Player wish you a good luck",400,680,size = 17,align = "center")
            drawLabel("See you next time",400,720,size = 17,align = "center")
            drawLabel("Press e to exit",400,750,size = 17,align = "center", fill = "white")


    

    def onKeyPress(self,key):
       if key == "0" and app.winTalkSB ==0:
            app.winTalkSB = 1
            
       if key =="1" and app.winTalkSB ==1:
            app.winTalkSB =2 
            
       if key =="2" and app.winTalkSB ==2:
            app.winTalkSB = 3

       if key =="e" and app.winTalkSB ==3:
            app.winTalkSB = 0
            p.badgeCollect.add("Salior")
            print(p.badgeCollect)
            self.goExitSB = True 


    def moveMent(self):
        if app.winTalkSB ==2:
            if app.moveRightSB:
                app.angleSB +=20
            else:
                app.angleSB  -= 20


    def onStep(self):
        if app.winTalkSB ==2:
            app.stepSB +=1 
            if app.stepSB %15 ==0: 
                if app.moveRightSB == True:
                    app.moveRightSB = False 
                    app.moveLeftSB  = True
                    self.moveMent()
                else:
                    app.moveRightSB = True 
                    app.moveLeftSB  = False 
                    self.moveMent()
        




