from cmu_graphics import *
import random
chosenPK = "Charmander"
def onAppStart(app):
    global chosenPK
    app.figthingGround = "fighting_ground.png"
    app.xPK1 = 150
    app.yPK1 = 415
    app.xPK2 = 470
    app.yPK2 = 185
    if chosenPK == "Bulbasaur":
        app.namePK1 = "Bulbasaur"
        app.pk1 = "Bulbasaur_back.png"
        app.myPKskillSet = ["Growl","Tackle","Vine Whip","Leech Seed"]

    if chosenPK == "Charmander":
        app.namePK1 = "Charmander"
        app.pk1 = "Charmander_back.png"
        app.myPKskillSet = ["Scratch","Growl","Ember","Dragon Breath"]

    
    if chosenPK == "Squirtle":
        app.namePK1 = "Squirtle"
        app.pk1 = "Squirtle_back.png"
        app.myPKskillSet = ["Tackle","Tail Whip","Water Gun","Bite"]

    if chosenPK == "Pikachu":
        app.namePK1 = "Pikachu"
        

    randomNumPK = random.randint(0,2)
    app.pokemonList = ["Bulbasaur","Charmander","Squirtle"]
    randomOppententPk = app.pokemonList[randomNumPK]
    app.namePK2 = randomOppententPk
    app.hpPK1 = 100
    app.hpPK2 = 100
    app.opacityPK1 = 100
    app.opacityPK2 = 100
    app.oppontentImage = ["Bulbasaur_Front.png","Charmander_Front.png","Squirtle_Front.png"]
    app.pk2 = app.oppontentImage[randomNumPK]
    app.firstSkill = app.myPKskillSet[0]
    app.secondSkill = app.myPKskillSet[1]
    app.thirdSkill = app.myPKskillSet[2]
    app.forthSkill = app.myPKskillSet[3]
    app.skillChosen = None
    app.start = False 
    app.isGrowl = False 
    app.growlImage = "growl.png"
    app.isTackle = False 
    app.step = 0
    app.isVineWhip = False 
    app.vineWhipAni  = "vine_whip.png"
    app.vineWhipRoate = 0
    # randomNum = random.randint(0,3)
    # skill = app.skillSet[randomNum]
    # app.skill  = (skill)
    app.isLeechSeed = False
    app.leechSeedAni = "leechSeed.png"
    app.leechSeedX = 190
    app.leechSeedY = 310
    app.isScratch = False 
    app.scratchAni = "scratch.png"
    app.scratchX = 500
    app.scratchY =180
    app.isEmber = False 
    app.smallEmber = "ember_small.png"
    # app.smallEmber2 = "ember_small.png"
    # app.smallEmber3 = "ember_small.png"
    app.bigEmber = "ember_big.png"
    app.smallEmberX = 260
    app.smallEmberY = 400
    app.isSmallEmber = False
    app.isBigEmber = False
    app.bigEmberX = 450
    app.bigEmberY = 150
    app.isDragonBreath = False 
    app.dragonBreath = "dragon_Breath.png" 
    app.isTailWhip = False
    app.dizzy = "dizzy.png"
    app.isWaterGun = False 
    app.waterGun = "watergun.png"
    app.isBite = False 
    app.biteUp = "bite.png"
    app.biteDown = "bite.png"
    app.biteUpX = 430
    app.biteUpY = 105
    app.biteDownY =300





    

def redrawAll(app):
    firstColor = rgb(110,213,192)
    secondColor = rgb(134,210,116)
    gradientColor = gradient(firstColor,secondColor,start = "top")
    drawRect(0,0,app.width,app.height,fill = gradientColor)
    imageWidth, imageHeight = getImageSize(app.figthingGround)
    drawImage(app.figthingGround,350,200,width =imageWidth*1.5 ,height =imageHeight*1.5 )
    drawImage(app.figthingGround,50,450,width =imageWidth*1.5 ,height =imageHeight*1.5)
    hpBox = rgb(103,103,88)
    #lowerBox(firstBox)
    drawRect(-3,620,300,95,fill = "white", border = hpBox, borderWidth = 5)
    drawLabel(f"{app.namePK1}",60,635,size = 20,bold = True)
    hpInnerBox = rgb(193,193,193)
    #black box 
    drawRect(10,650,250,30)
    drawLabel("HP",25,665,fill = "red",size = 20,bold = True )
    drawRect(40,650,240,30,fill = hpInnerBox,borderWidth = 3)
    drawRect(40,655,app.hpPK1*2.3,20,fill = "green")
    drawLabel(f"{app.hpPK1}/100",50,695,size = 20)
    #second box 
    drawRect(570,50,300,70,fill = "white", border = hpBox, borderWidth = 5)
    drawLabel(f"{app.namePK2}",640,70,size = 20,bold = True)
    drawRect(580,80,200,30)
    drawRect(610,80,210,30,fill = hpInnerBox,borderWidth = 3)
    drawLabel("HP",595,95,fill = "red",size = 20,bold = True )
    drawRect(610,85,app.hpPK2*2,20,fill = "green")
    # drawCircle(app.xPK1,app.yPK1,30,fill= "red")
    # drawCircle(app.xPK2,app.yPK2,30,fill = "blue")
    #draw pokemon Image
    drawImage(app.pk1,app.xPK1,app.yPK1,width = 150,height = 150,opacity = app.opacityPK1)
    drawImage(app.pk2,app.xPK2,app.yPK2,width= 150,height = 150,opacity = app.opacityPK2)
    #Narrative Box
    drawRect(450,660,320,100,fill = "gray",border = hpInnerBox,borderWidth = 5)
    if app.start:
        drawLabel(f"{app.namePK1} had used",610,700,size = 20,align = "center")
        drawLabel(f"{app.skillChosen}!!",610,720,size = 20,align = "center") 
    #Skill Set Box 1
    drawRect(500,380,270,60,fill = "gray",border = hpInnerBox,borderWidth = 3)
    drawLabel(app.firstSkill,630,410,size = 30)
    #skill set box 2
    drawRect(500,445,270,60,fill = "gray",border = hpInnerBox,borderWidth = 3)
    drawLabel(app.secondSkill,630,475,size = 30)
    #skill set box 3
    drawRect(500,510,270,60,fill = "gray",border = hpInnerBox,borderWidth = 3)
    drawLabel(app.thirdSkill,630,540,size = 30)
    #skill set box 4
    drawRect(500,575,270,60,fill = "gray",border = hpInnerBox,borderWidth = 3)
    drawLabel(app.forthSkill,630,605,size = 30,align = "center")
    #draw Growl Effect 
    if app.isGrowl == True:
        drawImage(app.growlImage,200,400,width = 50,height = 50)
        drawImage(app.growlImage,250,415,width = 50, height = 50 ,rotateAngle = 15)
        drawImage(app.growlImage,290,450,width = 50, height = 50 ,rotateAngle = 30)
        #drawImage(app.growlImage,app.xPK2 +50,app.yPK2 -15,width = 50, height = 50,rotateAngle = -30)
    if app.isVineWhip == True:
        drawImage(app.vineWhipAni,450,200,width = 120, height = 120,rotateAngle = app.vineWhipRoate)
    
    if app.isLeechSeed == True:
        drawImage(app.leechSeedAni,app.leechSeedX,app.leechSeedY,width = 200,height = 200,rotateAngle = 20)
    if app.isScratch == True:
        drawImage(app.scratchAni,app.scratchX,app.scratchY,width = 120, height = 120)

    if app.isSmallEmber == True:
        emberWidth, emberHeight = getImageSize(app.smallEmber)
        drawImage(app.smallEmber,app.smallEmberX,app.smallEmberY,width = emberWidth//5,height = emberHeight//5,rotateAngle = -20 )

    if app.isBigEmber == True:
        drawImage(app.bigEmber,app.bigEmberX,app.bigEmberY)
    if app.isDragonBreath == True:
        dwWidth, dwHeight = getImageSize(app.smallEmber)
        drawImage(app.dragonBreath,35,340,width = dwWidth*0.8,height = dwHeight*0.8,rotateAngle = -40)

    if app.isTailWhip == True:
        drawImage(app.dizzy,425,165)

    if app.isWaterGun == True:
        wgWidth, wgHeight = getImageSize(app.waterGun)
        drawImage(app.waterGun,250,270,width = wgWidth*0.6,height = wgHeight*0.6,rotateAngle = -220)
        
    if app.isBite == True:
        drawImage(app.biteUp,app.biteUpX,app.biteUpY)
        drawImage(app.biteDown,app.biteUpX+25,app.biteDownY,rotateAngle = 180)
    
    
def pointInRect(x, y, rectX, rectY, rectWidth, rectHeight):
    """
    Checks if the point (x, y) is within the rectangle defined by
    (rectX, rectY, rectWidth, rectHeight).
    """
    return rectX <= x <= rectX + rectWidth and rectY <= y <= rectY + rectHeight

def onMousePress(app, x,y):
    app.start = True 
    # Check if the mouse click is within the first skill box
    if pointInRect(x, y, 500, 380, 270, 60):
        app.skillChosen = app.firstSkill
        print(f"Clicked on {app.skillChosen}")

    # Check if the mouse click is within the second skill box
    elif pointInRect(x, y, 500, 445, 270, 60):
        app.skillChosen = app.secondSkill
        print(f"Clicked on {app.skillChosen}")

    # Check if the mouse click is within the third skill box
    elif pointInRect(x,y, 500, 510, 270, 60):
        app.skillChosen = app.thirdSkill
        print(f"Clicked on {app.skillChosen}")

    # Check if the mouse click is within the fourth skill box
    elif pointInRect(x, y, 500, 575, 270, 60):
        app.skillChosen = app.forthSkill
        print(f"Clicked on {app.skillChosen}")
    
    if app.skillChosen == "Growl":
        app.isGrowl = True
        app.opacityPK2 = 70


    if app.skillChosen == "Tackle":
        app.xPK1 += 230
        app.yPK1 -= 230
        app.yPK2 -= 30
        app.opacityPK2 =70
        app.isTackle = True 

    if app.skillChosen == "Vine Whip":
        app.isVineWhip = True 

    if app.skillChosen == "Leech Seed":
        app.isLeechSeed = True 

    if app.skillChosen == "Scratch":
        app.isScratch = True 

    if app.skillChosen == "Ember":
        app.isEmber = True 
        app.isSmallEmber = True

    if app.skillChosen == "Dragon Breath":
        app.isDragonBreath = True 

    if app.skillChosen == "Tail Whip":
        app.isTailWhip = True

    if app.skillChosen == "Water Gun":
        app.isWaterGun = True

    if app.skillChosen == "Bite":
        app.isBite = True 


def onStep(app):
    if app.isTackle == True:
        app.step +=1 
        if app.step ==app.stepsPerSecond:
            app.xPK1 -=230
            app.yPK1 +=230
            app.yPK2 += 30
            app.step = 0 
            app.opacityPK2 = 100
            app.isTackle = False 

    if app.isGrowl == True:
        app.step +=1
        if app.step ==app.stepsPerSecond:
            app.isGrowl = False 
            app.opacityPK2 =100
            app.step = 0 

    if app.isVineWhip == True:
        app.step +=1
        if app.step == app.stepsPerSecond //4:
            app.vineWhipRoate = 30
            app.opacityPK2 =70
        if app.step ==app.stepsPerSecond:
            app.isVineWhip = False
            app.step = 0
            app.vineWhipRoate = 0
            app.opacityPK2 =100

    if app.isLeechSeed == True:
        app.step +=1
        if app.step %10 ==0:
            app.leechSeedX +=55
            app.leechSeedY -=25
        if app.step == app.stepsPerSecond * 2:
            app.opacityPK2 =70
            app.leechSeedX = 190
            app.leechSeedY = 310
        if app.step > app.stepsPerSecond * 2:
            app.step = 0
            app.opacityPK2 = 100
            app.isLeechSeed = False 

    
    if app.isScratch ==True:
        app.step +=1 
        if app.step %5 ==0:
            app.scratchX -= 5
            app.scratchY +=5
        if app.step == app.stepsPerSecond * 0.5:
            app.opacityPK2 =70
        if app.step > app.stepsPerSecond * 1.1:
            app.step = 0
            app.opacityPK2 = 100
            app.isScratch = False 
            app.scratchX = 500
            app.scratchY =180

    if app.isSmallEmber == True:
        app.step+=1
        if app.step %10 ==0:
            app.smallEmberX +=35
            app.smallEmberY -=25
        if app.step == app.stepsPerSecond *2.3:
            app.smallEmberX = 260
            app.smallEmberY = 400
            app.isSmallEmber = False
            app.step = 0
            app.isBigEmber = True

    if app.isBigEmber == True:
        app.step +=1
        app.opacityPK2 = 70
        if app.step % 5 == 0:  # Adjust the frequency of the shake
                shake_amount = 10  # Adjust the shake amount
                app.bigEmberX += random.uniform(-shake_amount, shake_amount)
        if app.step > app.stepsPerSecond * 1.1:
            app.step = 0
            app.opacityPK2 = 100
            app.isBigEmber = False 
            app.bigEmberX = 450
            app.bigEmberY = 150
            app.xPK2 = 470

    if app.isDragonBreath == True:
        app.step +=1
        app.opacityPK2 = 70
        if app.step % 5 == 0:  # Adjust the frequency of the shake
                shake_amount = 10  # Adjust the shake amount
                app.xPK2 += random.uniform(-shake_amount, shake_amount)
        if app.step ==app.stepsPerSecond:
            app.isDragonBreath = False
            app.step = 0
            app.opacityPK2 =100
            app.xPK2 = 470


    if app.isTailWhip == True:
        app.step+=1
        if app.step % 5 == 0:  # Adjust the frequency of the shake
                shake_amount = 10  # Adjust the shake amount
                app.xPK1 += random.uniform(-shake_amount, shake_amount)
                app.yPK1 += random.uniform(-shake_amount, shake_amount)
                app.opacityPK2 = 70
        if app.step ==app.stepsPerSecond:
            app.isTailWhip = False
            app.step = 0
            app.opacityPK2 =100
            app.xPK1 = 150
            app.yPK1 = 415

    if app.isWaterGun == True:
        app.step +=1
        app.opacityPK2 = 70
        if app.step ==app.stepsPerSecond:
            app.isWaterGun = False 
            app.opacityPK2 =100
            app.step = 0 

    if app.isBite ==True:
        app.step +=1
        if app.step % 5 == 0:  # Adjust the frequency of the shake
                shake_amount = 5  # Adjust the shake amount
                app.xPK2 += random.uniform(-shake_amount, shake_amount)
                app.yPK2 += random.uniform(-shake_amount, shake_amount)
                app.opacityPK2 = 70
        if app.step % 5==0:
            app.biteUpY +=5
            app.biteDownY -=5
        if app.step ==app.stepsPerSecond*2:
            app.isBite = False 
            app.xPK2 = 470
            app.yPK2 = 185
            app.biteUpX = 430
            app.biteUpY = 105
            app.step = 0
            app.biteDownY =300
            app.opacityPK2 = 100

        


        

        
                
                

        


    


skill = {
    "Growl" : [0.05,0] ,
    "Tackle" : [0.1,0] ,
    "Vine Whip": [0,0.2] ,
    "Leech Seed": [0.2,0] ,
    "Razor Leaf": [0.15,0] ,
    "Seed Bomb": [0.23,0] ,
    "Scratch": [0.1,0.02] ,
    "Growl":[0.02,0.3] ,
    "Ember": [0.12,0] ,
    "Dragon Breath": [0.23,0] , 
    "Fire Fang": [0.21,0] ,
    "Slash": [0.12,0],
    "Tail Whip" : [0,0.25],
    "Water Gun": [0.2,0],
    "Bite": [0.12,0] ,
    "Water Pulse": [0.23,0],
    "Slash": [0.1,0],
    "Nuzzle": [0.07,0],
    "Nasty Plot": [0.12,0],
    "Thunder Shock":[0.16,0],
    "Electro Ball": [0.2,0],
    "ThunderBolt": [0.3,0]
}

# def skills(app):
#     if skill == "growl":







runApp(800,800)