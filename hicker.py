from cmu_graphics import *
import p

class HickerNPC:
    # this is HICker NPC where we ask to play a game 
    # to earn a new Pokemon 
    exitHick = False 
    def onAppStart(self):
        app.cave = "cave.png"
        app.squareSize = 80
        app.hickerNPC = "hickerNPC.png"
        app.ashBackC = "chrBack.png"
        app.caveTalk = 0

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
        if app.caveTalk ==0:
            drawLabel("Hello, young trainer!Welcome to Rock and Cave City!!",400,680,size = 17,align = "center")
            drawLabel("Press q to continue...",400,750,size = 17,align = "center",fill = "white")
        if app.caveTalk ==1:
            drawLabel("You could earn Onix if you solve this puzzle about 15-112 ",400,680,size = 17,align = "center")
            drawLabel("Press w to continue...",400,750,size = 17,align = "center",fill = "white")

        if app.caveTalk ==2:
            drawLabel("Do you want to play this game?",400,680,size = 17,align = "center")
            drawLabel("Press y to play the game and press n to not",400,700,size = 17,align = "center")

        if app.caveTalk ==3:
            drawLabel("Oh okay good bye",400,680,size = 17,align = "center")
            drawLabel("Press e to exit",400,700,size = 17,align = "center")

        if app.caveTalk ==4:
            drawLabel("Alright!! Let's play now",400,680,size = 17,align = "center")
            # drawLabel("Press on the right number digit for the answer",400,700,size = 17,align = "center")
            drawLabel("Press r  to continue",400,750,size = 17,align = "center",fill = "white")

        if app.caveTalk ==5:
            drawLabel("What is the room number for 15-112?",400,680,size = 17,align = "center")
            drawLabel("1.2042  2. 2023  3.2152  4.1002",400,710,size = 17,align = "center")
            drawLabel("Press on the right number digit for the answer",400,750,size = 17,align = "center",fill = "white")
            # drawLabel("Press r  to continue",400,750,size = 17,align = "center",fill = "white")

        if app.caveTalk ==5.1:
            drawLabel("It is wrong try it again",400,680,size = 17,align = "center")
            drawLabel("1.2042  2. 2023  3.2152  4.1002",400,710,size = 17,align = "center")
            drawLabel("Press on the right number digit for the answer",400,750,size = 17,align = "center",fill = "white")

        if app.caveTalk == 6:
            drawLabel("What is the term prokect out of whole point 100%?",400,680,size = 17,align = "center")
            drawLabel("1.10  2. 20  3.30  4.15",400,710,size = 17,align = "center")
            drawLabel("Press on the right number digit for the answer",400,750,size = 17,align = "center",fill = "white")

        if app.caveTalk ==6.1:
            drawLabel("It is wrong try it again",400,680,size = 17,align = "center")
            drawLabel("1.10  2. 20  3.30  4.15",400,710,size = 17,align = "center")
            drawLabel("Press on the right number digit for the answer",400,750,size = 17,align = "center",fill = "white")


        if app.caveTalk ==7:
            drawLabel("Who is the best Mentor",400,680,size = 17,align = "center")
            drawLabel("1.Sunaya  2. No one else  3.Nobody  4.Hmmm",400,710,size = 17,align = "center")
            drawLabel("Press on the right number digit for the answer",400,750,size = 17,align = "center",fill = "white")

        if app.caveTalk ==8:
            drawLabel("Alright you solved all of the problems!! ",400,680,size = 17,align = "center")
            drawLabel("Would you like to change your pokemon into Onix?",400,710,size = 17,align = "center")
            drawLabel("Press y for Yes and press n for N0",400,750,size = 17,align = "center",fill = "white")

        if app.caveTalk ==9:
            drawLabel("Good luck with Onix ",400,680,size = 17,align = "center")
            drawLabel("Press a to continue",400,750,size = 17,align = "center",fill = "white")









            




    def onKeyPress(self,key):
        if key =="q" and app.caveTalk ==0:
            app.caveTalk =1 

        if key =="w" and app.caveTalk ==1:
            app.caveTalk =2

        if key == "e" and app.caveTalk ==3:
            self.exitHick = True
            app.caveTalk = 0

        if key =="n" and app.caveTalk ==2:
            app.caveTalk = 3

        if key =="y" and app.caveTalk==2:
            app.caveTalk = 4

        if key =="r" and app.caveTalk ==4:
            app.caveTalk =5

        if key =="3" and app.caveTalk ==5:
            app.caveTalk = 6

        if key =="4" and app.caveTalk ==6:
            app.caveTalk = 7

        if (key =="1") and app.caveTalk ==7:
            app.caveTalk = 8

        if key =="y" and app.caveTalk ==8:
            app.caveTalk = 9
            p.pokemonChosen = p.Onix
            # p.name = "Onix"

        if key =="n" and app.caveTalk ==8:
            app.caveTalk = 3

        if key =="a" and app.caveTalk ==9:
            app.caveTalk =3


        
