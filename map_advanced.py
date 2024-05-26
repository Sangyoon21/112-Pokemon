from cmu_graphics import *
from control import Control
from pokemonCenter import PokemonCenter


class Map:
    onOff = 1
    def onAppStart(self):
        print("map is printing")
        #app.map = "map.jpeg"
        app.color = rgb(133,198,163)
        app.x =0
        app.y =0
        app.house = 'house.png'
        app.ash = "ash.png"
        app.gridSize = 40
        app.pokemonCenter = "pokemon_center.png"
        app.pokemonCenterColide = False 
        print("map is printing")


    def drawRoad(self):
        rowLength = app.width // app.gridSize
        roadColor = rgb(194,231,209)
        for row in range(rowLength):
            drawRect(5*app.gridSize,row * app.gridSize,app.gridSize,app.gridSize,fill =roadColor)

        colLength = app.height //app.gridSize
        for col in range(colLength):
            drawRect(col*app.gridSize,7*app.gridSize,app.gridSize,app.gridSize,fill =roadColor)



    def drawHouse(self):
        drawRect(9*app.gridSize,0,app.gridSize*3,app.gridSize*2,fill= None)
        drawImage(app.pokemonCenter,9*app.gridSize,0,width=app.gridSize*3,height = app.gridSize*2)
        drawRect(0*app.gridSize,app.gridSize*12,app.gridSize*3,app.gridSize*4)
        drawRect(app.gridSize*16,app.gridSize*17,app.gridSize*3,app.gridSize*3)
        if app.pokemonCenterColide:
            drawRect(0,0,800,800)



    def drawMap(self):
        rowLength = app.width // app.gridSize
        colLength = app.height //app.gridSize
        for row in range(rowLength):
            for col in range(colLength):
                self.drawCell(row,col,app.color)

    def drawCell(cell,row,col,color):
        x0 = col * app.gridSize
        y0 = row * app.gridSize
        drawRect(x0,y0,app.gridSize,app.gridSize,fill = color,border = "black",borderWidth =0)


    
    def redrawAll(self):
        self.drawMap()
        self.drawRoad()
        self.drawHouse()
        # if not app.pokemonCenterColide:
        #     drawImage(app.ash,app.x,app.y,width=40,height = 40)
        drawImage(app.ash,app.x,app.y,width=40,height = 40)

    def onKeyPress(self,key):
        oldX, oldY = app.x, app.y
        
        if key == "up" and app.y!=0:
            app.y -=app.gridSize
        if key == "down" and app.y!=app.height-app.gridSize:
            app.y +=app.gridSize
        if key == "right" and app.x!= app.width-app.gridSize:
            app.x +=app.gridSize
        if key == "left" and app.x!=0:
            app.x -=app.gridSize
        if self.isCollision(app.x, app.y, app.gridSize, app.gridSize,9*app.gridSize,0,app.gridSize*3,app.gridSize*2):
            app.x, app.y = oldX, oldY
            app.pokemonCenterColide =True
        if self.isCollision(app.x,app.y,app.gridSize,app.gridSize,0*app.gridSize,app.gridSize*12,app.gridSize*3,app.gridSize*4):
            app.x,app.y = oldX,oldY
        if self.isCollision(app.x,app.y,app.gridSize,app.gridSize,app.gridSize*16,app.gridSize*17,app.gridSize*3,app.gridSize*3):
            app.x,app.y = oldX,oldY



    def isCollision(self,x1, y1, w1, h1, x2, y2, w2, h2):
        return (x1 < x2 + w2) and (x1 + w1 > x2) and (y1 < y2 + h2) and (y1 + h1 > y2)



