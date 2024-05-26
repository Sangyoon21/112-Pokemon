from cmu_graphics import *
import p 

class BrockBadge:
    # it is when we are able to get the badge from Brock
    exitBB = False 
    def onAppStart(self):
        backgroundColor = rgb(90, 90, 113)
        app.background = backgroundColor
        app.tileColor = rgb(97, 97, 115)
        app.squareSizeBB = 80
        app.ashBackBB = "ashBack2.png"
        app.ashXBB = app.squareSizeBB * 4
        app.ashYBB = app.squareSizeBB * 5
        app.doorBB = "door.png"
        app.hpInnerBox = rgb(193, 193, 193)
        app.brockBB = "brock.png"
        app.talkBB = 0
        app.angleBB = 0
        app.moveRightBB = True
        app.moveLeftBB = False 
        app.stepBB = 0


    def redrawAll(self):
        for i in range(app.width // app.squareSizeBB):
            for j in range(app.height // app.squareSizeBB):
                x = i * app.squareSizeBB
                y = j * app.squareSizeBB
                if (i + j) % 2 == 0:
                    drawRect(x, y, app.squareSizeBB, app.squareSizeBB, fill=app.background)
                else:
                    drawRect(x, y, app.squareSizeBB, app.squareSizeBB, fill=app.tileColor)

        drawImage(app.ashBackBB, app.ashXBB, app.ashYBB, width=app.squareSizeBB, height=app.squareSizeBB)
        drawRect(app.squareSizeBB * 4, app.squareSizeBB * 5, app.squareSizeBB, app.squareSizeBB, fill=None)
        drawImage(app.brockBB, app.squareSizeBB * 4, app.squareSizeBB * 4, width=app.squareSizeBB, height=app.squareSizeBB)
        drawRect(app.squareSizeBB * 4, app.squareSizeBB * 0, app.squareSizeBB, app.squareSizeBB, fill=None)
        drawImage(app.doorBB, app.squareSizeBB * 4, app.squareSizeBB * 0, width=app.squareSizeBB, height=app.squareSizeBB)
        drawRect(app.squareSizeBB * 1, app.squareSizeBB * 0, app.squareSizeBB, app.squareSizeBB, fill=None)
        drawImage(app.doorBB, app.squareSizeBB * 1, app.squareSizeBB * 0, width=app.squareSizeBB, height=app.squareSizeBB)
        drawRect(app.squareSizeBB * 7, app.squareSizeBB * 0, app.squareSizeBB, app.squareSizeBB, fill=None)
        drawImage(app.doorBB, app.squareSizeBB * 7, app.squareSizeBB * 0, width=app.squareSizeBB, height=app.squareSizeBB)
        if app.talkBB==0:
            drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
            drawLabel("Great Job you have win me!!", 400, 670, size=20, align="center")
            drawLabel("Here is the badge that proves that you won me", 400, 700, size=20, align="center")
            drawLabel("Press 1 to continue", 400, 730, size=20, align="center", fill = "white")

        if app.talkBB ==1:
            drawRect(0,0,800,800,fill= "gray")
            drawImage("badgeBrook.png",250,200,width = 300, height = 300,rotateAngle = app.angleBB)
            drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
            drawLabel("Look at the Badge!", 400, 670, size=20, align="center")
            drawLabel("Might go the Salior's stadium next!", 400, 700, size=20, align="center")
            drawLabel("Press 2 to continue", 400, 730, size=20, align="center", fill = "white")
        if app.talkBB ==2:
            drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
            drawLabel("God luck on your future!! ", 400, 670, size=20, align="center")
            drawLabel("See you next time!!", 400, 700, size=20, align="center")
            drawLabel("Press space to continue", 400, 730, size=20, align="center", fill = "white")
        


    def onKeyPress(self,key):
        if app.talkBB ==0 and key =="1":
            app.talkBB= 1
        if app.talkBB ==1 and key =="2":
            app.talkBB = 2
        if app.talkBB ==2 and key=="space":
            app.talkBB = 0
            p.badgeCollect.add("Brock")
            print(p.badgeCollect)
            self.exitBB = True 


    def moveMent(self):
        if app.talkBB ==1:
            if app.moveRightBB:
                app.angleBB +=20
            else:
                app.angleBB  -= 20


    def onStep(self):
        if app.talkBB ==1:
            app.stepBB +=1 
            if app.stepBB %15 ==0: 
                if app.moveRightBB == True:
                    app.moveRightBB = False 
                    app.moveLeftBB  = True
                    self.moveMent()
                else:
                    app.moveRightBB = True 
                    app.moveLeftBB  = False 
                    self.moveMent()