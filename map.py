from cmu_graphics import *
import p 



class Map:
    #Pvalues to track on when to go to the next phase 
    onOff = 1
    pokemonCenterColide = False 
    pokemonStadiumColide = False 
    fightStadiumColide = False 
    goLeft = False 
    goRight = False 
    def onAppStart(self):
        app.color = rgb(133,198,163)
        app.x =0
        app.y =0
        app.house = 'house.png'
        #app.ash = "ash.png"
        app.chrFront = "chrFront.png"
        app.chrLeft = "chrLeft.png"
        app.chrBack = "chrBack.png"
        app.chrRight = "chrRight.png"
        app.chrStatus = app.chrFront
        app.gridSize = 50
        app.pokemonCenter = "pokemonCenter.png"
        app.stadium = "brookHouse.png"
        app.fightStadium = "stadiumY.png"
        app.grass = "grass.png"
        app.road = "road.png"
        app.tree = "tree.png" 

    #drawing the road 
    def drawRoad(self):
        rowLength = app.width // app.gridSize
        roadColor = rgb(194,231,209)
        for row in range(rowLength):
            drawImage(app.road,4*app.gridSize,row * app.gridSize,width = 50, height = 50)

        colLength = app.height //app.gridSize
        for col in range(colLength):
            drawImage(app.road,col*app.gridSize,6*app.gridSize,width = 50, height = 50)


    #drawing the buldings 
    def drawHouse(self):
        drawRect(8*app.gridSize,0,app.gridSize*3,app.gridSize*2,fill= None)
        drawImage(app.pokemonCenter,8*app.gridSize,0,width=app.gridSize*3,height = app.gridSize*2)
        drawRect(0*app.gridSize,app.gridSize*8,app.gridSize*3,app.gridSize*3,fill = None)
        drawImage(app.stadium,0*app.gridSize,app.gridSize*8,width=app.gridSize*3,height = app.gridSize*3,rotateAngle = 270)
        drawRect(app.gridSize*8,app.gridSize*13,app.gridSize*5,app.gridSize*3,fill = None)
        drawImage(app.fightStadium,app.gridSize*8,app.gridSize*13,width = app.gridSize*5,height= app.gridSize*3, rotateAngle = 180)
        #if app.pokemonCenterColide:
            #drawRect(0,0,800,800)



    def drawMap(self):
        drawImage("backGroundGrass.png",0,0)


    
    def redrawAll(self):
        self.drawMap()
        self.drawRoad()
        self.drawHouse()
        drawImage(app.chrStatus,app.x,app.y,width=50,height = 50)
        drawImage(app.tree,0, app.gridSize * 12,width = app.gridSize * 4,height = app.gridSize * 6)


    #able to keep the characther move by pressing on not pressing 
    def onKeyHold(self,key):
        oldX, oldY = app.x, app.y
        if  "up" in key and app.y!=0:
            app.y -=app.gridSize
            if app.chrStatus == app.chrLeft or app.chrStatus == app.chrRight:
                app.chrStatus = app.chrBack

            if app.chrStatus ==app.chrFront:
                app.chrStatus = app.chrBack


        if "down" in key and app.y!=app.height-app.gridSize:
            app.y +=app.gridSize
            if app.chrStatus == app.chrLeft or app.chrStatus == app.chrRight:
                app.chrStatus = app.chrFront

            if app.chrStatus ==app.chrBack:
                app.chrStatus = app.chrFront

            
        if "right" in key:
        # and app.x!= app.width-app.gridSize:
            app.x +=app.gridSize
            if app.chrStatus == app.chrFront or app.chrStatus == app.chrBack:
                app.chrStatus = app.chrRight

            if app.chrStatus == app.chrLeft:
                app.chrStatus = app.chrRight
        if  "left" in key:  
        #and app.x!=0:
            app.x -=app.gridSize
            if app.chrStatus == app.chrFront or app.chrStatus == app.chrBack:
                app.chrStatus = app.chrLeft

            if app.chrStatus == app.chrRight:
                app.chrStatus = app.chrLeft

        #it goes to the next screen when we go over the board 
        if app.x < 0:
            self.goLeft = True 
        if app.x > app.width - app.gridSize:
            # app.x = app.width - app.gridSize
            self.goRight = True
  
        #checking if we had collide with the building 
        if self.isCollision(app.x, app.y, app.gridSize, app.gridSize,8*app.gridSize,0,app.gridSize*3,app.gridSize*2):
            app.x, app.y = oldX, oldY
            self.pokemonCenterColide =True
            print("[!!!] Colliding",self.pokemonCenterColide)
        if self.isCollision(app.x,app.y,app.gridSize,app.gridSize,0*app.gridSize,app.gridSize*8,app.gridSize*3,app.gridSize*3):
            app.x,app.y = oldX,oldY
            self.pokemonStadiumColide = True
        if self.isCollision(app.x,app.y,app.gridSize,app.gridSize,app.gridSize*8,app.gridSize*13,app.gridSize*5,app.gridSize*3) :
            app.x,app.y = oldX,oldY
            self.fightStadiumColide = True 


    
    def isCollision(self,x1, y1, w1, h1, x2, y2, w2, h2):
        return (x1 < x2 + w2) and (x1 + w1 > x2) and (y1 < y2 + h2) and (y1 + h1 > y2)



