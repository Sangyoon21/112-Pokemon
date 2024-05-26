from cmu_graphics import *
import random

def gameDimensions():
    rows = 1
    cols = 1
    cellSize = 100
    margin = 125
    return (rows, cols, cellSize, margin)

def onAppStart(app):
    app.rows, app.cols, app.cellSize, app.margin = gameDimensions()
    app.emptyColor = "blue"
    app.board = [[None] * app.cols for _ in range(app.rows)]  # Use None to represent unoccupied cells
    app.currentNumber = 1
    app.step = 0
    app.time = 25
    app.isLost = False 
    placeRandomNumber(app)

def numberToColor(app, number):
    if not checkGameOver(app):
        return "red"

def drawCell(app, row, col, number=None):
    x0 = app.margin + col * app.cellSize
    y0 = app.margin + row * app.cellSize
    color = app.emptyColor if number is None else numberToColor(app, number)
    drawRect(x0, y0, app.cellSize, app.cellSize, fill=color, border="black", borderWidth=2)
    if number is not None and not checkGameOver(app) and not app.isLost:
        drawLabel(str(number), x0 + app.cellSize // 2, y0 + app.cellSize // 2, size=20)

def drawBoard(app):
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            drawCell(app, row, col, app.board[row][col])

def isCellOccupied(app, row, col):
    return app.board[row][col] is not None

def placeRandomNumber(app):
    while True and not checkGameOver(app)  and not app.isLost :
        randomRow, randomCol = random.randint(0, app.rows-1), random.randint(0, app.cols-1)
        if not isCellOccupied(app, randomRow, randomCol):
            app.board[randomRow][randomCol] = app.currentNumber
            break

def onMousePress(app, x, y):
    row = (y - app.margin) // app.cellSize
    col = (x - app.margin) // app.cellSize
    if not checkGameOver(app) and not app.isLost:
        if 0 <= row < app.rows and 0 <= col < app.cols:
            if app.board[row][col] == app.currentNumber:
                app.board[row][col] = None  # Reset the cell to unoccupied
                app.currentNumber += 1
                placeRandomNumber(app)

def checkGameOver(app):
    return app.currentNumber > app.rows * app.cols or app.time < 0

def redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill="orange")
    drawBoard(app)
    drawLabel(f"Time Left: {app.time}", 400, 100)

    if checkGameOver(app):
        drawRect(app.width//2 - 300,app.height//2 - 50,600,100,fill = "white")
        drawLabel("Congratulations! You completed the game!", app.width // 2, app.height // 2, size=30)
    else:
        drawLabel(f"Click on number {app.currentNumber}", app.width // 2, app.height - 50, size=20)

    if app.isLost ==True:
        drawLabel("You Lost!", app.width // 2, app.height // 2, size=30)


def onStep(app):
    app.step += 1
    if app.step % 30 == 0:
        app.time -= 1
    if app.time < 0:
        app.time = 0  # Ensure that time does not go below 0
        app.isLost = True
        app.step =0

#make a variable that stops mocving when the game end

    if checkGameOver(app):
        app.step =0





runApp(800, 800)
