from cmu_graphics import *
class MapLeft:
    # it is map when we move to left from the left side of main map
    goRightL = False 
    hickerHouseColideL = False 
    pokemonCenter2ColideL = False 
    stadiumYColideL = False 
    def onAppStart(self):
        app.backGround = "rockPK.png"
        app.xL =0
        app.yL =0
        #app.ash = "ash.png"
        app.chrFrontL = "chrFront.png"
        app.chrLeftL = "chrLeft.png"
        app.chrBackL = "chrBack.png"
        app.chrRightL = "chrRight.png"
        app.chrStatusL = app.chrFrontL
        app.gridSizeL = 50

    def drawBuildingL(self):
        # drawRect(8*app.gridSizeL,app.gridSizeL *3,app.gridSizeL*4,app.gridSizeL*3,fill= None)
        drawImage("hickerHouse.png",9*app.gridSizeL,app.gridSizeL * 12,width = app.gridSizeL *6,height = app.gridSizeL * 4,rotateAngle = 180)
        drawImage("pokemonCenter2.png",10*app.gridSizeL,app.gridSizeL * 3,width = app.gridSizeL *5,height = app.gridSizeL * 4)
        drawImage("stadiumY.png",0,450,width=app.gridSizeL*5,height = app.gridSizeL*4,rotateAngle = 180)

    def redrawAll(self):
        drawImage(app.backGround,0,0)
        drawImage(app.chrStatusL,app.xL,app.yL,width=50,height = 50)
        self.drawBuildingL()

    def onKeyHold(self,key):
        oldX, oldY = app.xL, app.yL
        if  "up" in key and app.yL!=0:
            app.yL -=app.gridSizeL
            if app.chrStatusL == app.chrLeftL or app.chrStatusL == app.chrRightL:
                app.chrStatusL = app.chrBackL

            if app.chrStatusL ==app.chrFrontL:
                app.chrStatusL = app.chrBackL


        if "down" in key and app.yL!=app.height-app.gridSizeL:
            app.yL +=app.gridSizeL
            if app.chrStatusL == app.chrLeftL or app.chrStatusL == app.chrRightL:
                app.chrStatusL = app.chrFrontL

            if app.chrStatusL ==app.chrBackL:
                app.chrStatusL = app.chrFrontL

            
        if "right" in key and app.xL!= app.width-app.gridSizeL:
            app.xL +=app.gridSizeL
            if app.chrStatusL == app.chrFrontL or app.chrStatusL == app.chrBackL:
                app.chrStatusL = app.chrRightL

            if app.chrStatusL == app.chrLeftL:
                app.chrStatusL = app.chrRightL
        if  "left" in key  and app.xL!=0:
            app.xL -=app.gridSizeL
            if app.chrStatusL == app.chrFrontL or app.chrStatusL == app.chrBackL:
                app.chrStatusL = app.chrLeftL
            if app.chrStatusL == app.chrRightL:
                app.chrStatusL = app.chrLeftL


        if self.isCollision(app.xL, app.yL, app.gridSizeL, app.gridSizeL,9*app.gridSizeL,app.gridSizeL * 12,app.gridSizeL *6,app.gridSizeL * 4):
            app.xL, app.yL = oldX, oldY
            self.hickerHouseColideL = True 

        if self.isCollision(app.xL, app.yL, app.gridSizeL, app.gridSizeL,10*app.gridSizeL,app.gridSizeL * 3,app.gridSizeL *5,app.gridSizeL * 4):
            app.xL, app.yL = oldX, oldY
            self.pokemonCenter2ColideL = True 


        if self.isCollision(app.xL, app.yL,  app.gridSizeL, app.gridSizeL, 0,450,app.gridSizeL*5,app.gridSizeL*4):
            app.xL, app.yL = oldX, oldY
            self.stadiumYColideL = True

        if app.xL >= app.width - app.gridSizeL:
            # app.x = app.width - app.gridSize
            self.goRightL = True
            print(self.goRightL)


    def isCollision(self,x1, y1, w1, h1, x2, y2, w2, h2):
        return (x1 < x2 + w2) and (x1 + w1 > x2) and (y1 < y2 + h2) and (y1 + h1 > y2)
