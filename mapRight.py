from cmu_graphics import *
# from control import Control
# from pokemonCenter import PokemonCenter



class MapR:
    # it is left sife othe main map
    goLeft = False 
    pokemonCenterColide = False 
    saliorCenterColide = False 
    saliorStadiumColide = False 
    def onAppStart(self):
        app.xR =0
        app.yR =0
        #app.ash = "ash.png"
        app.chrFrontR = "chrFront.png"
        app.chrLeftR = "chrLeft.png"
        app.chrBackR = "chrBack.png"
        app.chrRightR = "chrRight.png"
        app.chrStatusR = app.chrFrontR
        app.rockRoad = "rockRoad.png"
        app.gridSizeR = 50

  


    def drawMap(self):
        drawImage("backGroundGrass.png",0,0)

    def drawRoad(self):
        drawImage("rockRoad.png",6*app.gridSizeR,0,width = app.gridSizeR * 2)
        drawImage(app.rockRoad,5*app.gridSizeR,0*app.gridSizeR- 100,width = app.gridSizeR *2 ,rotateAngle = 90 )

    def drawBuilding(self):
        drawRect(8*app.gridSizeR,app.gridSizeR *3,app.gridSizeR*4,app.gridSizeR*3,fill= None)
        drawImage("blueBuilding.png",8*app.gridSizeR,app.gridSizeR*3,width=app.gridSizeR*4,height = app.gridSizeR*3)
        drawImage("pokemonCenter2.png",9*app.gridSizeR,app.gridSizeR * 12,width = app.gridSizeR *6,height = app.gridSizeR * 4,rotateAngle = 180)
        drawImage("stadiumY.png",0*app.gridSizeR,app.gridSizeR * 5,width = app.gridSizeR *5,height = app.gridSizeR * 3)

    def redrawAll(self):
        self.drawMap()
        self.drawRoad()
        self.drawBuilding()
        drawImage(app.chrStatusR,app.xR,app.yR,width=50,height = 50)


    def onKeyHold(self,key):
        oldX, oldY = app.xR, app.yR
        if  "up" in key and app.yR!=0:
            app.yR -=app.gridSizeR
            if app.chrStatusR == app.chrLeftR or app.chrStatusR == app.chrRightR:
                app.chrStatusR = app.chrBackR

            if app.chrStatusR ==app.chrFrontR:
                app.chrStatusR = app.chrBackR


        if "down" in key and app.yR!=app.height-app.gridSizeR:
            app.yR +=app.gridSizeR
            if app.chrStatusR == app.chrLeftR or app.chrStatusR == app.chrRightR:
                app.chrStatusR = app.chrFrontR

            if app.chrStatusR ==app.chrBackR:
                app.chrStatusR = app.chrFrontR

            
        if "right" in key and app.xR!= app.width-app.gridSizeR:
            app.xR +=app.gridSizeR
            if app.chrStatusR == app.chrFrontR or app.chrStatusR == app.chrBackR:
                app.chrStatusR = app.chrRightR

            if app.chrStatusR == app.chrLeftR:
                app.chrStatusR = app.chrRightR
        if  "left" in key  and app.xR!=0:
            app.xR -=app.gridSizeR
            if app.chrStatusR == app.chrFrontR or app.chrStatusR == app.chrBackR:
                app.chrStatusR = app.chrLeftR

            if app.chrStatusR == app.chrRightR:
                app.chrStatusR = app.chrLeftR

        if self.isCollision(app.xR, app.yR, app.gridSizeR, app.gridSizeR,8*app.gridSizeR,app.gridSizeR *3,app.gridSizeR*4,app.gridSizeR*3):
            app.xR, app.yR = oldX, oldY
            self.saliorCenterColide = True 


        if self.isCollision(app.xR, app.yR, app.gridSizeR, app.gridSizeR,9*app.gridSizeR,app.gridSizeR * 12,app.gridSizeR *6,app.gridSizeR * 4):
            app.xR, app.yR = oldX, oldY
            self.pokemonCenterColide =True

        if self.isCollision(app.xR, app.yR, app.gridSizeR, app.gridSizeR,0*app.gridSizeR,app.gridSizeR * 5,app.gridSizeR *5,app.gridSizeR * 3):
            app.xR, app.yR = oldX, oldY
            self.saliorStadiumColide = True

        if app.xR  - app.gridSizeR <0:
            self.goLeft = True
            print(self.goLeft) 


        



    def isCollision(self,x1, y1, w1, h1, x2, y2, w2, h2):
        return (x1 < x2 + w2) and (x1 + w1 > x2) and (y1 < y2 + h2) and (y1 + h1 > y2)



