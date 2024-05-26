from cmu_graphics import *
import p 


class PokemonCenter:
    #this is the code when we enter the pokemon center and interact with the NpC
    end = False
    finished = False 
    def onAppStart(self):
        app.backgroundColor = rgb(243, 238, 209)
        # app.background = backgroundColor
        app.squareSize = 80
        app.desk = "centerDesk.png"
        app.ashBack = "ashBack.png"
        app.isMousePressed = False 
        app.talkStep = 0
        app.talk1Selection = None
        app.step =0
        app.ashX = 300
        app.ashY = 150


    def redrawAll(self):
        #draw the tiles of the background 
        drawRect(0,0,800,800,fill = app.backgroundColor)
        for i in range(app.width // app.squareSize):
            for j in range(app.height // app.squareSize):
                x = i * app.squareSize
                y = j * app.squareSize
                if (i + j) % 2 == 0:
                    drawRect(x, y, app.squareSize, app.squareSize, fill=app.background)
                else:
                    drawRect(x, y, app.squareSize, app.squareSize, fill="white")

        drawRect(app.squareSize*1,app.squareSize*0,app.squareSize*7,app.squareSize*4,fill = None)
        drawImage(app.desk,app.squareSize*1,app.squareSize*0,width= app.squareSize*8,height =app.squareSize*4)
        drawImage(app.ashBack,app.ashX,app.ashY,width=240,height = 240)
        hpInnerBox = rgb(193,193,193)
        drawRect(100,600,600,180,fill = "gray",border = hpInnerBox,borderWidth = 5)
        #different NPC talks depending on the different pahse we are in 
        if app.isMousePressed ==False:
            drawLabel("Press the Nurse to Interact with the Nusrse!!",400,670,size = 20,align = "center")
        if app.isMousePressed:
            if app.talkStep ==-2:
                drawLabel("It is my pleasure to see younger Player",400,670,size = 20,align = "center")
                drawLabel("Did you heard about this place?",400,700,size = 20,align = "center")
                drawLabel("Press q to continue",400,740,size = 20,fill = "white",align = "center")
            if app.talkStep ==-1:
                drawLabel("If you know about me and this center press:  y",400,670,size = 20,align = "center")
                drawLabel("If you don't know about me and this center press:  n",400,700,size = 20,align = "center")
                
            if app.talkStep ==0:
                drawLabel("So player than what could we help you??",400,670,size = 20,align = "center")
                drawLabel("Press on the space to continue",400,720,size = 20,align = "center", fill = "white")
            if app.talkStep ==1:
                drawLabel("Press on the option you want",400,670,size = 20,align = "center")
                drawRect(550,500,150,50,fill = "gray",border = hpInnerBox,borderWidth = 5)
                drawLabel("1. Heal the Pokemon",630,525,size = 13)
                drawRect(550,550,150,50,fill = "gray",border = hpInnerBox,borderWidth = 5)
                drawLabel("2. No I am Okay",630,575,size = 13)
            if app.talkStep ==2:
                if app.talk1Selection ==1:
                    drawLabel("Here is our Pokemon all Healed!!",400,670,size = 20,align = "center")
                    drawLabel("Press space to continue",400,740,size = 20,fill = "white",align = "center")

                elif app.talk1Selection ==2:
                    drawLabel("Oh Okay! Wish you good luck!!",400,670,size = 20,align = "center")
                    drawLabel("Press space to continue",400,740,size = 20,fill = "white",align = "center")

            if app.talkStep ==3:
                drawLabel("Good bye young player",400,670,size = 20,align = "center")
                drawLabel("Press e to exit",400,740,size = 20,fill = "white",align = "center")


            if app.talkStep ==4:
                drawLabel("Hello my name is Nuse Joy!! ",400,670,size = 20,align = "center")
                drawLabel("Nice to meet you",400,700,size = 20,align = "center")
                drawLabel("Press w to continue",400,740,size = 20,fill = "white",align = "center")

            if app.talkStep ==5:
                drawLabel("This place is called Pokemon Center!! ",400,670,size = 20,align = "center")
                drawLabel("You could heal your pokemon's HP here!!",400,700,size = 20,align = "center")
                drawLabel("Press r to continue",400,740,size = 20,fill = "white",align = "center")
    #click on the right box
    def pointInRect(self,x, y, rectX, rectY, rectWidth, rectHeight):
        return rectX <= x <= rectX + rectWidth and rectY <= y <= rectY + rectHeight


    def onMousePress(self,x,y):
    # app.namePK1 = p.pokemonChosen.name
    # app.hpPK1 = p.pokemonChosen
        app.ashX = 300
        app.ashY = 150
        if self.pointInRect(x, y, app.squareSize*1,app.squareSize*0,app.squareSize*7,app.squareSize*4):
            app.isMousePressed = True
            app.talkStep =-2



        if app.talkStep ==1:
            if self.pointInRect(x, y, 550,500,150,50):
                app.talk1Selection = 1
                p.health = 100
                # print(app.namePK1,app.hpPK1)
                app.talkStep =2
            if self.pointInRect(x, y, 550,550,150,50):
                    app.talk1Selection = 2
                    print("it is selected 2")
                    # print(app.namePK1,app.hpPK1)
                    app.talkStep =2 
    #control the phase by pressing on the key
    def onKeyPress(self,key):
        if key == "q" and app.talkStep ==-2:
            app.talkStep = -1

        if key == "y" and app.talkStep ==-1:
            app.talkStep = 0 

        if key == "n" and app.talkStep == -1:
            app.talkStep = 4 

        if key =="space" and app.talkStep == 0:
            app.talkStep = 1

        if key =="w" and app.talkStep == 4:
            app.talkStep = 5 

        if key == "r" and app.talkStep ==5:
            app.talkStep = 0

        if key == "space" and app.talkStep == 2:
            app.talkStep =3

        if key == "e" and app.talkStep ==3:
            self.end = True 
            app.talkStep = -2
                











