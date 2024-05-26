from cmu_graphics import *
import p 
#this is paeg where the professor NPC comes out
class TitlePage: 
    #checker for exiting the oage 
    goToStart = False 
    def onAppStart(self):
        app.page = 0
        app.startPage = "startGamePage.png"
        app.professor = "Professor_Oak_XY.png"
        app.profTalk = 0



    def redrawAll(self):
        #changing the things i print depend on the talk phase we are in 
        if app.page ==0:
            color = rgb(197,206,165)
            drawRect(0,0,app.width,app.height,fill = color)
            drawImage(app.startPage,80,100) 
            drawLabel("Press p to play the game!!",400,650,fill = "gray",size = 30)

        if app.page ==1:
            drawRect(0,0,app.width,app.height,fill ="skyBlue")
            drawImage(app.professor,250,100,width = 200,height = 400)
            hpInnerBox = rgb(193,193,193)
            drawRect(100,600,600,180,fill = "gray",border = hpInnerBox,borderWidth = 5)
            #drawLabel("Press space to continue...",400,750,size = 17,align = "center",fill = "white")
            if app.profTalk ==0:
                drawLabel("Hello, young trainer! This is Professor Oak's laboratory in Palette Town.",400,680,size = 17,align = "center")
                drawLabel("Press 1 to continue...",400,750,size = 17,align = "center",fill = "white")
            if app.profTalk ==1:
                drawLabel("You have just turned to 10 years old!!",400,680,size = 17,align = "center")
                drawLabel("It is about to take your first steps as a Pokemon trainer.",400,700,size  = 17 ,align = "center")
                drawLabel("Press 2 to continue...",400,750,size = 17,align = "center",fill = "white")
            if app.profTalk ==2:
                drawLabel("Are you ready!!!",400,680,size = 17,align = "center")
                drawLabel("Press 0 to continue...",400,750,size = 17,align = "center",fill = "white")



        #change the phase by clicking on the keys 
    def onKeyPress(self,key):
        if key =="p" and app.page ==0:
            app.page  =1 

        if key =="1" and app.page ==1 and app.profTalk ==0:
            app.profTalk =1 
            
        if key =="2" and app.page ==1 and app.profTalk ==1:
            app.profTalk =2

        if key =="0" and app.page ==1 and app.profTalk ==2:
            self.goToStart = True


