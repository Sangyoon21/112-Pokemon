
from cmu_graphics import *

def onAppStart(app):
    app.start = False 
    app.startMiddle = False 
    backgroundColor = rgb(90, 90, 113)
    app.background = backgroundColor
    app.tileColor = rgb(97, 97, 115)
    app.squareSize = 80
    app.ashBack = "ashBack2.png"
    app.ashX2 = app.squareSize * 4
    app.ashY2 = app.squareSize * 6
    app.playCard = "playCard.png"
    app.isFirstPlayCard = False 
    app.door = "door.png"
    app.isWrong1 = False 
    app.hpInnerBox = rgb(193, 193, 193)
    app.isFirst = False
    app.isRight1 = False
    app.step = 0
    app.ashOpacity = 100
    app.brock = "brock.png"
    app.isBrock = True 
    app.isPlayCard = False
    app.isSecondPlayCard = False
    app.count = 0
    app.secondStep = False
    app.isThirdPlayCard = False 
    app.thirdStep = False


def redrawAll(app):
    for i in range(app.width // app.squareSize):
        for j in range(app.height // app.squareSize):
            x = i * app.squareSize
            y = j * app.squareSize
            if (i + j) % 2 == 0:
                drawRect(x, y, app.squareSize, app.squareSize, fill=app.background)
            else:
                drawRect(x, y, app.squareSize, app.squareSize, fill=app.tileColor)

    drawImage(app.ashBack, app.ashX2, app.ashY2, width=app.squareSize, height=app.squareSize, opacity=app.ashOpacity)
    drawRect(app.squareSize * 4, app.squareSize * 5, app.squareSize, app.squareSize, fill=None)
    if app.isBrock == True:
        drawImage(app.brock, app.squareSize * 4, app.squareSize * 5, width=app.squareSize, height=app.squareSize)
        drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
        drawLabel("Welcom to my stadium!!! ", 400, 670, size=20, align="center")
        drawLabel("Come to me!! ", 400, 700, size=20, align="center")

    if app.isPlayCard == True:
        drawImage(app.playCard, app.squareSize * 4, app.squareSize * 5, width=app.squareSize, height=app.squareSize)
    drawRect(app.squareSize * 4, app.squareSize * 0, app.squareSize, app.squareSize, fill=None)
    drawImage(app.door, app.squareSize * 4, app.squareSize * 0, width=app.squareSize, height=app.squareSize)
    drawRect(app.squareSize * 1, app.squareSize * 0, app.squareSize, app.squareSize, fill=None)
    drawImage(app.door, app.squareSize * 1, app.squareSize * 0, width=app.squareSize, height=app.squareSize)
    drawRect(app.squareSize * 7, app.squareSize * 0, app.squareSize, app.squareSize, fill=None)
    drawImage(app.door, app.squareSize * 7, app.squareSize * 0, width=app.squareSize, height=app.squareSize)
    if app.startMiddle == True and app.count == 0:
        drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
        drawLabel("To Play a Game with me You need to Solve this Puzzle!!", 400, 670, size=20, align="center")
        drawLabel("HAHAHAHAH See you Later!", 400, 700, size=20, align="center")

    if app.isFirstPlayCard == True and app.count == 0:
        drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
        drawLabel("Question: 3 plus 5 plus 7 is ?", 400, 670, size=20, align="center")
        drawLabel("Left: 2 Middle: 16 Right: 15", 400, 700, size=20, align="center")

    if app.isWrong1 == True:
        drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
        drawLabel("You are wrong!!", 400, 670, size=20, align="center")
        print("line 72: this is printing")


    if app.isRight1 == True:
        drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
        drawLabel("You are Right!!", 400, 670, size=20, align="center")
        print("line 77 is printing")

    if app.secondStep == True and app.count == 1:
        drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
        drawLabel("Question: 6 plus 3 plus 4 is ?", 400, 670, size=20, align="center")
        drawLabel("Left: 13 Middle: 16 Right: 12", 400, 700, size=20, align="center")

    if app.isThirdPlayCard == True and app.count ==2:
        drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
        drawLabel("Question: 10 plus 4 plus 4 is ?", 400, 670, size=20, align="center")
        drawLabel("Left: 12 Middle: 28 Right: 18", 400, 700, size=20, align="center")

    if app.count ==3:
        for i in range(app.width // app.squareSize):
            for j in range(app.height // app.squareSize):
                x = i * app.squareSize
                y = j * app.squareSize
                if (i + j) % 2 == 0:
                    drawRect(x, y, app.squareSize, app.squareSize, fill=app.background)
                else:
                    drawRect(x, y, app.squareSize, app.squareSize, fill=app.tileColor)

        drawImage(app.brock, app.squareSize * 5, app.squareSize * 3, width=app.squareSize, height=app.squareSize)
        drawRect(100, 600, 600, 180, fill="gray", border=app.hpInnerBox, borderWidth=5)
        drawLabel("Finally you came good to see you!!", 400, 670, size=20, align="center")
        drawLabel("However you came to late!! I will be in the", 400, 700, size=20, align="center")
        drawLabel("stadium on the Right!! GoodBye!! Press q to exit", 400, 730, size=20, align="center")
        drawImage(app.ashBack, app.squareSize * 3, app.squareSize * 5, width=app.squareSize, height=app.squareSize, opacity=app.ashOpacity)
#         # self.pageEnd = True





def onKeyPress(app,key):
    oldX, oldY = app.ashX2, app.ashY2

    if key == "up" and app.ashY2 != 0:
        app.ashY2 -= app.squareSize
    if key == "down" and app.ashY2 != app.height - app.squareSize:
        app.ashY2 += app.squareSize
    if key == "right" and app.ashX2 != app.width - app.squareSize:
        app.ashX2 += app.squareSize
    if key == "left" and app.ashX2 != 0:
        app.ashX2 -= app.squareSize

    if app.count == 0:
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 4, app.squareSize * 5,
                        app.squareSize, app.squareSize) and app.start == False:
            app.ashX2, app.ashY2 = oldX, oldY
            app.startMiddle = True

        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 4, app.squareSize * 5,
                        app.squareSize, app.squareSize) and app.start == True:
            app.ashX2, app.ashY2 = oldX, oldY
            app.isFirstPlayCard = True
            print("line 133:",app.isFirstPlayCard)

    if app.count == 1:
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 4, app.squareSize * 5, app.squareSize, app.squareSize):
            app.ashX2, app.ashY2 = oldX, oldY
            app.isSecondPlayCard = True
            print("line 138",app.isSecondPlayCard)

    if app.count ==2:
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 4, app.squareSize * 5, app.squareSize, app.squareSize):
            app.ashX2, app.ashY2 = oldX, oldY
            app.isThirdPlayCard = True
            print("line 144",app.isThirdPlayCard)


    if app.isFirstPlayCard == True:
        app.isFirst = True

    if app.isFirst == True: 
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 4, app.squareSize * 0,
                        app.squareSize, app.squareSize) and app.count == 0:
            app.ashX2, app.ashY2 = oldX, oldY
            app.isFirstPlayCard = False 
            app.isWrong1 = True
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 1, app.squareSize * 0,
                        app.squareSize, app.squareSize) and app.count == 0:
            app.ashX2, app.ashY2 = oldX, oldY
            app.isFirstPlayCard = False 
            app.isWrong1 = True
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 7, app.squareSize * 0,
                        app.squareSize, app.squareSize) and app.count == 0:
            # app.ashX2, app.ashY2 = oldX, oldY
            app.isFirstPlayCard = False 
            app.isRight1 = True
            app.ashOpacity = 0
            app.count = 1 

    if app.secondStep == True:
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 1, app.squareSize * 0,
                        app.squareSize, app.squareSize) and app.count == 1:
            app.ashX2, app.ashY2 = oldX, oldY
            app.isRight1 = True
            app.ashOpacity = 0
            app.count = 2 
            app.isSecondPlayCard = False 
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 4, app.squareSize * 0,
                        app.squareSize, app.squareSize) and app.count == 1:
            app.ashX2, app.ashY2 = oldX, oldY
            app.isSecondPlayCard = False 
            app.isWrong1 = True
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 7, app.squareSize * 0,
                        app.squareSize, app.squareSize) and app.count == 1:
            app.ashX2, app.ashY2 = oldX, oldY
            app.isSecondPlayCard = False 
            app.isWrong1 = True

    if app.thirdStep == True:
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 4, app.squareSize * 0,
                        app.squareSize, app.squareSize) and app.count == 2:
            app.ashX2, app.ashY2 = oldX, oldY
            app.isThirdPlayCard = False 
            app.isWrong1 = True
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 1, app.squareSize * 0,
                        app.squareSize, app.squareSize) and app.count == 2:
            app.ashX2, app.ashY2 = oldX, oldY
            app.isThirdPlayCard = False 
            app.isWrong1 = True
        if isCollision(app.ashX2, app.ashY2, app.squareSize, app.squareSize, app.squareSize * 7, app.squareSize * 0,
                        app.squareSize, app.squareSize) and app.count == 2:
            app.ashX2, app.ashY2 = oldX, oldY
            app.isThirdPlayCard = False 
            app.isRight1 = True
            app.ashOpacity = 0
            app.count = 3 

    if app.count ==3:
        if key == "q":
            print("this is printing")
            app.count = 4





def isCollision(x1, y1, w1, h1, x2, y2, w2, h2):
    return (x1 < x2 + w2) and (x1 + w1 > x2) and (y1 < y2 + h2) and (y1 + h1 > y2)


def onStep(app):
    print(app.ashX2)
    if app.startMiddle == True and app.count == 0:
        app.step += 1
        if app.step % 30 == 0:
            app.startMiddle = False
            app.isBrock = False 
            app.ashX2 = app.squareSize * 4
            app.ashY2 = app.squareSize * 6
            app.isPlayCard = True
            app.step = 0 
            app.start = True

    if app.isRight1 == True:
        print("line 235 is working")
        app.ashX2 = app.squareSize * 4
        app.ashY2 = app.squareSize * 6
        app.step += 1
        if app.step % 30 == 0:
            app.ashOpacity = 100
            app.step = 0
            app.isRight1 = False 
            app.isWrong1 = False 

    if app.isSecondPlayCard == True:
        app.step += 1
        if app.step % 30 == 0:
            app.secondStep = True
            app.step = 0

    if app.isThirdPlayCard == True:
        app.step += 1
        if app.step % 30 == 0:
            app.thirdStep = True
            app.step = 0

    if app.count ==4:
        # self.pageEnd = True
        app.count =0
        app.start = False
        app.startMiddle = False
        app.isSecondPlayCard = False
        app.count = 0
        app.secondStep = False
        app.isThirdPlayCard = False 
        app.thirdStep = False 

runApp(800,800)