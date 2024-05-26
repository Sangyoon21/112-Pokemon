from cmu_graphics import *
import p 

class HickerBadge:
    goExitHB = False 
    # when we get a new badge from the hicker is in thei phase 
    def onAppStart(self):
        app.cave = "cave.png"
        app.squareSize = 80
        app.hickerNPC = "hickerNPC.png"
        app.ashBackC = "chrBack.png"
        app.caveTalkHB = 0
        app.hickerBadge = "hickerBadge.png"
        app.angleHB = 0
        app.moveRight = True
        app.moveLeft = False 
        app.stepHB = 0

    def redrawAll(self):
        bkColor = rgb(139,112,91)
        drawRect(0,0,800,800,fill = bkColor)
        drawRect(app.squareSize * 1.5, app.squareSize * 0, app.squareSize, app.squareSize, fill=None)
        drawImage(app.cave, app.squareSize * 1.5, app.squareSize * 0, width=app.squareSize, height=app.squareSize)
        drawRect(app.squareSize * 3.5, app.squareSize * 0, app.squareSize, app.squareSize, fill=None)
        drawImage(app.cave, app.squareSize * 3.5, app.squareSize * 0, width=app.squareSize, height=app.squareSize)
        drawRect(app.squareSize * 5.5, app.squareSize * 0, app.squareSize, app.squareSize, fill=None)
        drawImage(app.cave, app.squareSize * 5.5, app.squareSize * 0, width=app.squareSize, height=app.squareSize)
        drawRect(app.squareSize * 7.5, app.squareSize * 0, app.squareSize, app.squareSize, fill=None)
        drawImage(app.cave, app.squareSize * 7.5, app.squareSize * 0, width=app.squareSize, height=app.squareSize)
        drawImage(app.hickerNPC,350,300,width=app.squareSize, height=app.squareSize)
        drawImage(app.ashBackC,350,400,width=app.squareSize, height=app.squareSize)
        hpInnerBox = rgb(193,193,193)
        drawRect(100,600,600,180,fill = "gray",border = hpInnerBox,borderWidth = 5)
        if app.caveTalkHB == 0:
            drawLabel("Good job it was a tough fight!!",400,680,size = 17,align = "center")
            drawLabel("Press q to continue...",400,750,size = 17,align = "center",fill = "white")
        if app.caveTalkHB ==1:
            drawLabel("Here is the badge!!! Good Job!",400,680,size = 17,align = "center")
            drawLabel("Press w to continue...",400,750,size = 17,align = "center",fill = "white")

        if app.caveTalkHB ==2:
            drawRect(0,0,800,800,fill = bkColor)
            drawImage(app.hickerBadge,220,200,width = 300, height = 300,rotateAngle = app.angleHB)
            drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
            drawLabel("You deserve this Badge player",400,680,size = 17,align = "center")
            drawLabel("Press a to continue..",400,750,size = 17,align = "center",fill = "white")

        if app.caveTalkHB ==3:
            drawLabel("Player wish you a good luck",400,680,size = 17,align = "center")
            drawLabel("See you next time",400,720,size = 17,align = "center")
            drawLabel("Press e to exit",400,750,size = 17,align = "center", fill = "white")

        
            

    def onKeyPress(self,key):
        if key =="q" and app.caveTalkHB ==0:
            app.caveTalkHB = 1
        if key =="w" and app.caveTalkHB ==1:
            app.caveTalkHB = 2

        if key =="a" and app.caveTalkHB ==2:
            app.caveTalkHB = 3

        if key =="e" and app.caveTalkHB ==3:
            app.winTalkHB = 0
            p.badgeCollect.add("Hicker")
            print(p.badgeCollect)
            self.goExitHB = True 

    def moveMent(self):
        if app.caveTalkHB ==2:
            if app.moveRight:
                app.angleHB +=20
            else:
                app.angleHB  -= 20


    def onStep(self):
        if app.caveTalkHB ==2:
            app.stepHB +=1 
            if app.stepHB %15 ==0: 
                if app.moveRight == True:
                    app.moveRight = False 
                    app.moveLeft  = True
                    self.moveMent()
                else:
                    app.moveRight = True 
                    app.moveLeft  = False 
                    self.moveMent()

        