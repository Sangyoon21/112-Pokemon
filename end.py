from cmu_graphics import *

class End:
    #the ending screen
    def onAppStart(self):
        app.theEnd = "theEnd.png"

    def redrawAll(self):
        drawRect(0,0,800,800, fill = "white")
        drawImage("logo.png",0,200,opacity = 50)
        drawLabel("Game Ended!!",400,500,size = 20)
        drawLabel("Wish you a good luck for you and your future young player!",400,550,size = 20)
        drawImage("theEnd.png",100,100)