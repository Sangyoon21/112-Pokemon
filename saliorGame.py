from cmu_graphics import *
import random

class SaliorGame:
    # the subgame wher we need to press 25 tboxes in 20 seconds 
    win = False 
    lose = False 
    def gameDimensions(self):
        rows = 5
        cols = 5
        cellSize = 100
        margin = 125
        return (rows, cols, cellSize, margin)

    def onAppStart(self):
        app.rows, app.cols, app.cellSize, app.margin = self.gameDimensions()
        app.emptyColor = "blue"
        app.board = [[None] * app.cols for _ in range(app.rows)]  # Use None to represent unoccupied cells
        app.currentNumber = 1
        app.stepSG = 0
        app.time = 20
        app.isLost = False 
        app.winGame = False
        app.loseGame = False 
        self.placeRandomNumber()

    def numberToColor(self, number):
        if not self.checkGameOver():
            return "red"

    def drawCell(self, row, col, number=None):
        x0 = app.margin + col * app.cellSize
        y0 = app.margin + row * app.cellSize
        color = app.emptyColor if number is None else self.numberToColor(number)
        drawRect(x0, y0, app.cellSize, app.cellSize, fill=color, border="black", borderWidth=2)
        if number is not None and not self.checkGameOver() and not app.isLost:
            drawLabel(str(number), x0 + app.cellSize // 2, y0 + app.cellSize // 2, size=20)

    def drawBoard(self):
        for row in range(len(app.board)):
            for col in range(len(app.board[0])):
                self.drawCell(row, col, app.board[row][col])

    def isCellOccupied(self, row, col):
        return app.board[row][col] is not None

    def placeRandomNumber(self):
        while True and not self.checkGameOver()  and not app.isLost :
            randomRow, randomCol = random.randint(0, app.rows-1), random.randint(0, app.cols-1)
            if not self.isCellOccupied(randomRow, randomCol):
                app.board[randomRow][randomCol] = app.currentNumber
                break

    def onMousePress(self, x, y):
        row = (y - app.margin) // app.cellSize
        col = (x - app.margin) // app.cellSize
        if not self.checkGameOver() and not app.isLost:
            if 0 <= row < app.rows and 0 <= col < app.cols:
                if app.board[row][col] == app.currentNumber:
                    app.board[row][col] = None  # Reset the cell to unoccupied
                    app.currentNumber += 1
                    self.placeRandomNumber()

    def checkGameOver(self):
        return app.currentNumber > app.rows * app.cols or app.time < 0

    def redrawAll(self):
        drawRect(0, 0, app.width, app.height, fill="orange")
        self.drawBoard()
        drawLabel(f"Time Left: {app.time}", 400, 100)

        if self.checkGameOver():
            drawRect(app.width//2 - 300,app.height//2 - 100,600,250,fill = "white")
            drawLabel("Congratulations! You completed the game!", app.width // 2, app.height // 2, size=30)
            drawLabel("press space to continue", app.width // 2, app.height // 2+50, size=30)
            # self.win = True 
        else:
            drawLabel(f"Click on number {app.currentNumber}", app.width // 2, app.height - 50, size=20)

        if app.isLost ==True:
            drawLabel("You Lost!", app.width // 2, app.height // 2, size=30)
            drawLabel("press space to continue", app.width // 2, app.height // 2+50, size=30)


    def onStep(self):
        app.stepSG += 1
        if app.stepSG % 30 == 0:
            app.time -= 1
        if app.time < 0:
            app.time = 0  # Ensure that time does not go below 0
            app.isLost = True
            app.stepSG =0
            app.loseGame = True 

    #make a variable that stops mocving when the game end

        if self.checkGameOver():
            app.stepSG =0
            app.winGame = True



    def onKeyPress(self,key):
        if key =="space" and app.winGame:
            self.win = True
            app.winGame = False
            # app.currentNumber = 1
            app.stepSG = 0
            app.time = 20
            app.isLost = False 
            app.winGame = False
            app.loseGame = False 
            # self.placeRandomNumber() 
        if key =="space" and app.loseGame:
            self.lose = True
            app.loseGame = False 
            # app.currentNumber = 1
            app.stepSG = 0
            app.time = 20
            app.isLost = False 
            app.winGame = False
            app.loseGame = False 
            # self.placeRandomNumber()




   
