from cmu_graphics import *
import random
# chosenPK = "Pikachu"
import p

#p.pokemonChosen
class FightingScence:
    #place where we really fight with other pokemons
    endWin = False 
    endLost = False 
    #choase the oppontent pokemon randomly 
    def onAppStart(self):
        # global chosenPK
        # p.loadtedData() 
        app.figthingGround = "fighting_ground.png"
        app.xPK1 = 150
        app.yPK1 = 415
        app.xPK2 = 480
        app.yPK2 = 185
        # app.namePK1 = p.pokemonChosen.name
        # app.pk1 = p.pokemonChosen.backPhoto
        # app.myPKskillSet = p.pokemonChosen.skill
        # app.hpPK1 = p.health
        randomNumPK = random.randint(0,2)
        app.pokemonList = [p. Bulbasaur, p. Charmander , p.Squirtle]
        random0ppententPk = app.pokemonList [randomNumPK]
        # random0ppententPk = p.Squirtle
        app. namePK2 = random0ppententPk. name
        app.pk2 = random0ppententPk. frontPhoto
        app.oppententPKSkillSet = random0ppententPk.skill
        #app.hpPK1 = random0ppententPk.health
        app.hpPK2 = 100
        app.turn = 0
        app.opacityPK1 = 100
        app.opacityPK2 = 100
        app.skillChosen = None
        app.start = False 
        app.isGrowl1 = False 
        app.growlImage = "growl.png"
        app.isTackle1 = False 
        app.step = 0
        app.isVineWhip1 = False 
        app.vineWhipAni  = "vine_whip.png"
        app.vineWhipRoate = 0
        # randomNum = random.randint(0,3)
        # skill = app.skillSet[randomNum]
        # app.skill  = (skill)
        app.isLeechSeed1 = False
        app.leechSeedAni = "leechSeed.png"
        app.leechSeedX = 190
        app.leechSeedY = 310
        app.isScratch1 = False 
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
        app.isSmallEmber1 = False
        app.isBigEmber1 = False
        app.bigEmberX = 450
        app.bigEmberY = 150
        app.isDragonBreath1 = False 
        app.dragonBreath = "dragon_Breath.png" 
        app.isTailWhip1 = False
        app.dizzy = "dizzy.png"
        app.isWaterGun1 = False 
        app.waterGun = "watergun.png"
        app.isBite1 = False 
        app.biteUp = "bite.png"
        app.biteDown = "bite.png"
        app.biteUpX = 430
        app.biteUpY = 105
        app.biteDownY =300
        app.isElectroBall = False 
        app.electroBall = "electroBall.png"
        app.electroBallX = 260
        app.electroBallY = 400
        app.isElectricity = False 
        app.electricity = "electricity.png"
        app.electricityX = 400
        app.electricityY = 150
        app.isThunderBolt = False 
        app.thunderBolt = "thunderBolt.png"
        app.thunderBoltX = 440
        app.thunderBoltY = 80
        app.step2 =0 
        app.oppontentSkillChosen = None
        app.isGrowl2 = False 
        app.isTackle2 = False 
        app.start2 = False 
        app.tackleEnd = False 
        app.isViheWhip2 = False
        app.isLeechSeed2 = False  
        app.leechSeedX2 = 470
        app.leechSeedY2 = 180
        app.isScratch2 = False 
        app.scratchX2 = 210
        app.scratchY2 = 385
        app.isEmber2 = False 
        app.isSmallEmber2 = False
        app.isBigEmber2 = False
        app.smallEmberX2 = 400
        app.smallEmberY2 = 240
        app.bigEmberX2 = 150
        app.bigEmberY2 = 410
        app.isDragonBreath2 = False
        app.isTailWhip2 = False  
        app.isWaterGun2 = False 
        app.isBite2 = False 
        app.biteUpX2 = 130
        app.biteUpY2 = 330
        app.biteDownY2 = 530
        app.keyScreen = True 
        app.loadingImage = "loading.png"
        app.loadImageX = 250
        app.loadImageY = 200
        app.stepInfo = 0
        app.mouseCount = 0
        app.realStart = False 
        app.mouseCheck = True 

    def redrawAll(self):
        #start with a simple information page before we start the battle
        if app.keyScreen:
            drawImage(app.loadingImage,app.loadImageX,app.loadImageY )
            drawLabel("Did You Know the first Pokemon Game in already 27??", 400 ,400, font = "monospace", size = 25,fill = "white")
            drawLabel("There are over 1000 species of Pokémon!", 400,440,font = "monospace", size = 25,fill = "white")
            drawLabel("Pokémon means 'Pocket Monsters'",400,480,font = "monospace", size = 25,fill = "white")
            drawLabel("If you didn't chosee the poemon at the choosing phase'",400,520,font = "monospace", size = 23,fill = "white")
            drawLabel("You would have a pokemon as your Pokemon!!(Hidden piece)",400,560,font = "monospace", size = 23,fill = "white")
            drawLabel("You would be kicked out when you HP is low go to the center to heal",400,600,font = "monospace", size = 23,fill = "white")
            drawLabel("HP is low go to the center to heal",400,640,font = "monospace", size = 23,fill = "white")
            drawLabel("Press space two times to continue",400,700,font = "monospace", size = 23,fill = "white")
        else:
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
            drawRect(40,655,p.health*2.3,20,fill = "green") #app.hpPK2.health
            drawLabel(f"{p.health}/100",50,695,size = 20)
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

            if app.start2 == True:
                drawLabel(f"{app.namePK2} had used",610,700,size = 20,align = "center")
                drawLabel(f"{app.oppontentSkillChosen}!!",610,720,size = 20,align = "center") 

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
            #draw Effect depending on the skills the pokemon use  
        if app.isGrowl1 == True:
            drawImage(app.growlImage,200,400,width = 50,height = 50)
            drawImage(app.growlImage,250,415,width = 50, height = 50 ,rotateAngle = 15)
            drawImage(app.growlImage,290,450,width = 50, height = 50 ,rotateAngle = 30)
        if app.isVineWhip1 == True:
            drawImage(app.vineWhipAni,450,200,width = 120, height = 120,rotateAngle = app.vineWhipRoate)

        
        if app.isLeechSeed1 == True:

            drawImage(app.leechSeedAni,app.leechSeedX,app.leechSeedY,width = 200,height = 200,rotateAngle = 20)
        if app.isScratch1 == True:

            drawImage(app.scratchAni,app.scratchX,app.scratchY,width = 120, height = 120)

        if app.isSmallEmber1 == True:
            emberWidth, emberHeight = getImageSize(app.smallEmber)
            drawImage(app.smallEmber,app.smallEmberX,app.smallEmberY,width = emberWidth//5,height = emberHeight//5,rotateAngle = -20 )

        if app.isBigEmber1 == True:
            drawImage(app.bigEmber,app.bigEmberX,app.bigEmberY)
        if app.isDragonBreath1 == True:
            dwWidth, dwHeight = getImageSize(app.smallEmber)
            drawImage(app.dragonBreath,35,340,width = dwWidth*0.8,height = dwHeight*0.8,rotateAngle = -40)

        if app.isTailWhip1 == True:
            drawImage(app.dizzy,425,165)

        if app.isWaterGun1 == True:
            wgWidth, wgHeight = getImageSize(app.waterGun)
            drawImage(app.waterGun,250,270,width = wgWidth*0.6,height = wgHeight*0.6,rotateAngle = -220)
            
        if app.isBite1 == True:
            drawImage(app.biteUp,app.biteUpX,app.biteUpY)
            drawImage(app.biteDown,app.biteUpX+25,app.biteDownY,rotateAngle = 180)

        if app.isElectroBall == True:
            drawImage(app.electroBall,app.electroBallX,app.electroBallY)

        if app.isElectricity == True:
            drawImage(app.electricity,app.electricityX,app.electricityY)

        if app.isThunderBolt == True:
            tbWidth, twHeight = getImageSize(app.thunderBolt)
            drawImage(app.thunderBolt,app.thunderBoltX,app.thunderBoltY,width = tbWidth*0.6,height = twHeight*0.6)

        if app.isGrowl2 == True:
            drawImage(app.growlImage,470,230,width = 50,height = 50)
            drawImage(app.growlImage,500,280,width = 50, height = 50 ,rotateAngle = -15)
            drawImage(app.growlImage,540,320,width = 50, height = 50 ,rotateAngle = -30)

        if app.isViheWhip2 == True:
            drawImage(app.vineWhipAni,140,385,width = 120, height = 120,rotateAngle = app.vineWhipRoate)

        if app.isLeechSeed2 == True:
            drawImage(app.leechSeedAni,app.leechSeedX2,app.leechSeedY2,width = 200,height = 200,rotateAngle = 20)

        if app.isScratch2 == True:
            drawImage(app.scratchAni,app.scratchX2,app.scratchY2,width = 120, height = 120)

        if app.isSmallEmber2 == True:
            emberWidth, emberHeight = getImageSize(app.smallEmber)
            drawImage(app.smallEmber,app.smallEmberX2,app.smallEmberY2,width = emberWidth//5,height = emberHeight//5,rotateAngle = -20 )

        if app.isBigEmber2 == True:
            drawImage(app.bigEmber,app.bigEmberX2,app.bigEmberY2)

        if app.isDragonBreath2 == True:
            dwWidth, dwHeight = getImageSize(app.smallEmber)
            drawImage(app.dragonBreath,140,220,width = dwWidth*0.8,height = dwHeight*0.8,rotateAngle = -220)

        if app.isTailWhip2 == True:
            drawImage(app.dizzy,140,395)

        if app.isWaterGun2 == True:
            wgWidth, wgHeight = getImageSize(app.waterGun)
            drawImage(app.waterGun,190,240,width = wgWidth*0.6,height = wgHeight*0.6,rotateAngle = 320)

        if app.isBite2 == True:
            drawImage(app.biteUp,app.biteUpX2,app.biteUpY2)
            drawImage(app.biteDown,app.biteUpX2+25,app.biteDownY2,rotateAngle = 180)


    #check what we chose for the skill
    def pointInRect(self,x, y, rectX, rectY, rectWidth, rectHeight, skill):
        if rectX <=x <=rectX + rectWidth and rectY <=y <= rectY +rectHeight:
            app.skillChosen = skill

    def onMousePress(self, x,y):
        if app.turn == 0:
            app.start = True 
            # if app.start2:
            #     app.start2 = False 
            # Check if the mouse click is within the first skill box
            self.pointInRect(x, y, 500, 380, 270, 60, app.firstSkill)
            self.pointInRect(x, y, 500, 445, 270, 60, app.secondSkill)
            self.pointInRect(x, y, 500, 510, 270, 60, app.thirdSkill)
            self.pointInRect(x, y, 500, 575, 270, 60, app.forthSkill)
            if app.skillChosen == "Growl":
                app.isGrowl1 = True
                app.opacityPK2 = 70
            if app.skillChosen == "Tackle":
                app.xPK1 += 230
                app.yPK1 -= 230
                app.yPK2 -= 30
                app.opacityPK2 =70
                app.isTackle1 = True 
            app.isVineWhip1 = True if app.skillChosen == "Vine Whip" else False
            app.isLeechSeed1 = True if app.skillChosen == "Leech Seed" else False 
            app.isScratch1 = True if app.skillChosen == "Scratch" else False 

            if app.skillChosen == "Ember":
                app.isEmber = True 
                app.isSmallEmber1 = True
            app.isDragonBreath1 = True if app.skillChosen == "Dragon Breath" else False 
            app.isTailWhip1 = True if app.skillChosen == "Tail Whip" else False 
            app.isWaterGun1 = True if app.skillChosen == "Water Gun" else False 
            app.isBite1 = True if app.skillChosen == "Bite" else False 
            app.isElectroBall = True if app.skillChosen == "Electro Ball" else False 
            app.isThunderBolt = True if app.skillChosen == "ThunderBolt" else False 

        


        # while app.hpPK1 > 0 and app.hpPK2 >0:
        if app.turn ==0:
            app.turn  = 0.5






    def onStep(self):
        #check if we have some HP left
        if p.health < 0:
            p.health = 0
        if app.hpPK2 < 0:
            app.hpPK2 = 0

        if p.health <0:
            p.health = 0

        if app.keyScreen:
            app.stepInfo +=1
            if app.stepInfo %30==0:
                app.loadImageY +=5
            if app.stepInfo % 50 ==0:
                app.loadImageY -=5

        if p.health <= 1 or app.hpPK2 <=1:
            print("the game eneded")
            # make the end screen 
        # change the valuses that needto changed after the skills iare used or while it is used
        if app.isTackle1 == True:

            app.step +=1 
            if app.step %60 ==0:

                app.xPK1 -=230
                app.yPK1 +=230
                app.yPK2 += 30
                app.step = 0 
                app.opacityPK2 = 100
                app.isTackle1 = False 
                app.start = False
                app.hpPK2 -= random.randint(10,20) 


        if app.isGrowl1 == True:
            app.step +=1
            if app.step %30 ==0:
                app.isGrowl1 = False 
                app.opacityPK2 =100
                app.step = 0 
                app.start = False 
                app.hpPK2 -= random.randint(10,20)

        if app.isVineWhip1 == True:
            app.step +=1
            if app.step % 10==0:
                app.vineWhipRoate = 30
                app.opacityPK2 =70
            if app.step %50 ==0:
                app.isVineWhip1 = False
                app.step = 0
                app.vineWhipRoate = 0
                app.opacityPK2 =100
                app.start = False 
                app.hpPK2 -= random.randint(10,20)

        if app.isLeechSeed1 == True:
            app.step +=1
            if app.step %10 ==0:
                app.leechSeedX +=55
                app.leechSeedY -=25
            if app.step %60 ==0:
                app.opacityPK2 =70
                app.leechSeedX = 190
                app.leechSeedY = 310
            if app.step > 61:
                app.step = 0
                app.opacityPK2 = 100
                app.isLeechSeed1 = False 
                app.start = False
                app.hpPK2 -= random.randint(10,20)

        if app.isScratch1 ==True:
            app.step +=1 
            if app.step %5 ==0:
                app.scratchX -= 5
                app.scratchY +=5
            if app.step == app.stepsPerSecond * 0.5:
                app.opacityPK2 =70
            if app.step > 70:
                app.step = 0
                app.opacityPK2 = 100
                app.isScratch1 = False 
                app.scratchX = 500
                app.scratchY =180
                app.start = False
                app.hpPK2 -= random.randint(10,20)

        if app.isSmallEmber1 == True:
            app.step+=1
            if app.step %10 ==0:
                app.smallEmberX +=35
                app.smallEmberY -=25
            if app.step == app.stepsPerSecond *2.3:
                app.smallEmberX = 260
                app.smallEmberY = 400
                app.isSmallEmber1 = False
                app.step = 0
                app.isBigEmber1 = True
                app.hpPK2 -= random.randint(10,20)

        if app.isBigEmber1 == True:
            app.step +=1
            app.opacityPK2 = 70
            if app.step % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 10  # Adjust the shake amount
                    app.bigEmberX += random.uniform(-shake_amount, shake_amount)
            if app.step > app.stepsPerSecond * 1.1:
                app.step = 0
                app.opacityPK2 = 100
                app.isBigEmber1 = False 
                app.bigEmberX = 450
                app.bigEmberY = 150
                app.xPK2 = 470
                app.start = False
                app.hpPK2 -= random.randint(10,20)
                app.ember = False 

        if app.isDragonBreath1 == True:
            app.step +=1
            app.opacityPK2 = 70
            if app.step % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 10  # Adjust the shake amount
                    app.xPK2 += random.uniform(-shake_amount, shake_amount)
            if app.step % 30 ==0:
                app.isDragonBreath1 = False
                app.step = 0
                app.opacityPK2 =100
                app.xPK2 = 470
                app.start = False 
                app.hpPK2 -= random.randint(10,20)


        if app.isTailWhip1 == True:
            app.step+=1
            if app.step % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 10  # Adjust the shake amount
                    app.xPK1 += random.uniform(-shake_amount, shake_amount)
                    app.yPK1 += random.uniform(-shake_amount, shake_amount)
                    app.opacityPK2 = 70
            if app.step  %30 ==0:
                app.isTailWhip1 = False
                app.step = 0
                app.opacityPK2 =100
                app.xPK1 = 150
                app.yPK1 = 415
                app.start = False
                app.hpPK2 -= random.randint(10,20)


        if app.isWaterGun1 == True:
            app.step +=1
            app.opacityPK2 = 70
            if app.step  %30 ==0:
                app.isWaterGun1 = False 
                app.opacityPK2 =100
                app.step = 0 
                app.start = False 
                app.hpPK2 -= random.randint(10,20)


        if app.isBite1 ==True:
            app.step +=1
            if app.step % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 5  # Adjust the shake amount
                    app.xPK2 += random.uniform(-shake_amount, shake_amount)
                    app.yPK2 += random.uniform(-shake_amount, shake_amount)
                    app.opacityPK2 = 70
            if app.step % 5==0:
                app.biteUpY +=5
                app.biteDownY -=5
            if app.step  %60 ==0:
                app.isBite1 = False 
                app.xPK2 = 470
                app.yPK2 = 185
                app.biteUpX = 430
                app.biteUpY = 105
                app.step = 0
                app.biteDownY =300
                app.opacityPK2 = 100
                app.start = False 
                app.hpPK2 -= random.randint(10,20)

        if app.isElectroBall == True:
            app.step+=1
            if app.step %10 ==0:
                app.electroBallX +=35
                app.electroBallY -=25
            if app.step  %(30*2.3) ==0:
                app.electroBallX = 260
                app.electroBallY = 400
                app.isElectroBall = False
                app.step = 0
                app.isElectricity = True
                app.start = False 
                app.hpPK2 -= random.randint(10,20)


        if app.isElectricity == True:
            app.step +=1
            app.opacityPK2 = 70
            if app.step % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 10  # Adjust the shake amount
                    app.electricityX += random.uniform(-shake_amount, shake_amount)
            if app.step >  30*1.1:
                app.step = 0
                app.opacityPK2 = 100
                app.isElectricity = False 
                app.electricityX = 400
                app.electricityY = 150
                app.xPK2 = 470
                app.start = False 
                app.hpPK2 -= random.randint(10,20)



        if app.isThunderBolt ==True:
            app.step+=1
            if app.step % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 10  # Adjust the shake amount
                    app.xPK1 += random.uniform(-shake_amount, shake_amount)
                    app.yPK1 += random.uniform(-shake_amount, shake_amount)
                    app.opacityPK2 = 70
                    app.start = False 

            if app.step  %30 ==0:
                app.isThunderBolt = False
                app.step = 0
                app.opacityPK2 =100
                app.xPK1 = 150
                app.yPK1 = 415
                app.hpPK2 -= random.randint(10,20)

        if app.turn ==0.5:
            app.step2 +=1
            #change 50 to 150
            if app.step2 %100 ==0:
                app.turn =1
                app.step2 =0
                app.start2 = True
                app.mouseCheck = False 

        # this is effects for the oppotent pokemon 
        if app.turn ==1:

            app.turn = 0
            skillRandom = random.randint(0,3)
            app.oppontentSkillChosen = app.oppententPKSkillSet[skillRandom]

            # app.hpPK1 -=50
            if app.oppontentSkillChosen == "Growl":
                app.isGrowl2 = True
                app.opacityPK1 = 70 
                app.turn = 0

            if app.oppontentSkillChosen == "Tackle":
                app.isTackle2 = True
                app.opacityPK1 = 70 
                app.turn = 0
                # app.start2 = False 

            if app.oppontentSkillChosen == "Vine Whip":
                app.isViheWhip2 = True 
                app.opacityPK1 = 70
                app.turn = 0

            if app.oppontentSkillChosen == "Leech Seed":
                app.isLeechSeed2 = True
                app.turn = 0

            if app.oppontentSkillChosen == "Scratch":
                app.isScratch2 = True
                app.turn = 0

            if app.oppontentSkillChosen== "Ember":
                app.isEmber2 = True
                app.turn = 0

            if app.oppontentSkillChosen == "Dragon Breath":
                app.isDragonBreath2 = True
                app.turn = 0

            if app.oppontentSkillChosen== "Tail Whip":
                app.isTailWhip2 = True
                app.turn = 0

            if app.oppontentSkillChosen == "Water Gun":
                app.isWaterGun2 = True
                app.turn = 0

            if app.oppontentSkillChosen == "Bite":
                app.isBite2 = True 
                app.turn = 0


        if app.isGrowl2 == True:
            app.step2 +=1
            if app.step2 ==app.stepsPerSecond:
                app.isGrowl2 = False
                app.opacityPK1 =100
                app.step2 = 0 
                app.start2 = False 
                app.turn = 0
                p.health -= random.randint(10,20)


        if app.isTackle2 == True:
            app.xPK2 = 250
            app.yPK2 = 415
            app.yPK1 = 445
            # app.tackleEnd = True 
            app.step2 +=1 
            if app.step2 ==app.stepsPerSecond:
                app.xPK2 = 480
                app.yPK2 = 185
                app.yPK1 = 414
                app.step2 = 0 
                app.opacityPK1 = 100
                app.isTackle2 = False 
                app.start2 = False 
                app.tackleEnd = False
                app.turn =0
                p.health -= random.randint(10,20)


        if app.isViheWhip2 == True:
            app.step2 += 1
            if app.step2 == app.stepsPerSecond // 4:
                app.vineWhipRoate = 30
                app.opacityPK1 = 70
            if app.step2 == app.stepsPerSecond:
                app.isViheWhip2 = False
                app.step2 = 0
                app.vineWhipRoate = 0
                app.opacityPK1 = 100
                app.start2 = False
                app.turn = 0
                p.health -= random.randint(10,20)

        if app.isViheWhip2 == True and app.step2 > app.stepsPerSecond:
            app.isViheWhip2 = False
            app.step2 = 0
            app.vineWhipRoate = 0
            app.opacityPK1 = 100
            app.start2 = False
            app.turn = 0
            p.health -= random.randint(10,20)


        if app.isLeechSeed2 == True:
                app.step2 += 1
                if app.step2 % 10 == 0:
                    app.leechSeedX2 -= 55
                    app.leechSeedY2 += 35
                if app.step2 == app.stepsPerSecond * 2:
                    app.opacityPK1 = 70
                    app.leechSeedX2 = 450  # Adjust the starting position for isLeechSeed2
                    app.leechSeedY2 = 150  # Adjust the starting position for isLeechSeed2
                if app.step2 > app.stepsPerSecond * 2:
                    app.step2 = 0
                    app.opacityPK1 = 100
                    app.isLeechSeed2 = False
                    app.start2 = False
                    p.health-= random.randint(10,20)

                app.turn = 0

        if app.isScratch2==True:
            app.step2 +=1 
            if app.step2 %5 ==0:
                app.scratchX2 -= 5
                app.scratchY2 +=5
            if app.step2 == app.stepsPerSecond * 0.5:
                app.opacityPK1 =70
            if app.step2 > app.stepsPerSecond * 1.2:
                app.step2 = 0
                app.opacityPK1 = 100
                app.isScratch2 = False 
                app.scratchX2 = 210
                app.scratchY2 =385
                app.start2 = False
                p.health -= random.randint(10,20)

            app.turn = 0

        if app.isEmber2 == True:
            app.isSmallEmber2 = True

        if app.isSmallEmber2 == True:
            app.step2+=1
            if app.step2 %10 ==0:
                app.smallEmberX2 -=35
                app.smallEmberY2 +=35
            if app.step2 == app.stepsPerSecond *2.3:
                app.smallEmberX2 = 380
                app.smallEmberY2 = 240
                app.isSmallEmber2 = False
                app.step2 = 0
                app.isBigEmber2= True
                app.isEmber2 = False 

        if app.isBigEmber2 == True:
            app.step2 +=1
            app.opacityPK1 = 70
            if app.step2 % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 10  # Adjust the shake amount
                    app.bigEmberX2 += random.uniform(-shake_amount, shake_amount)
            if app.step2 > app.stepsPerSecond * 1.1:
                app.step2 = 0
                app.opacityPK1 = 100
                app.isBigEmber2 = False 
                app.bigEmberX2 = 150
                app.bigEmberY2 = 410
                app.xPK2 = 470
                app.start2 = False
                p.health-= random.randint(10,20)


            app.turn = 0


        if app.isDragonBreath2 == True:
            app.step2 +=1
            app.opacityPK1 = 70
            if app.step2 % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 10  # Adjust the shake amount
                    app.xPK1 += random.uniform(-shake_amount, shake_amount)
            if app.step2 ==app.stepsPerSecond:
                app.isDragonBreath2 = False
                app.step2 = 0
                app.opacityPK1 =100
                app.xPK1 = 140
                app.start2 = False 
                p.health -= random.randint(10,20)
                app.turn = 0


        if app.isTailWhip2 == True:
            app.step2+=1
            if app.step2 % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 10  # Adjust the shake amount
                    app.xPK2 += random.uniform(-shake_amount, shake_amount)
                    app.yPK2 += random.uniform(-shake_amount, shake_amount)
                    app.opacityPK1 = 70
            if app.step2 ==app.stepsPerSecond:
                app.isTailWhip2 = False
                app.step2 = 0
                app.opacityPK1 =100
                app.xPK2 = 480
                app.yPK2 = 185
                app.start2 = False
                p.health -= random.randint(10,20)
                app.turn = 0

        if app.isWaterGun2 ==True:
            app.step2 +=1
            app.opacityPK1 = 70
            if app.step2 ==app.stepsPerSecond:
                app.isWaterGun2 = False 
                app.opacityPK1 =100
                app.step2 = 0 
                app.start2 = False 
                p.health -= random.randint(10,20)
                app.turn = 0


        if app.isBite2 == True:
            app.step2 +=1
            if app.step2 % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 5  # Adjust the shake amount
                    app.xPK1 += random.uniform(-shake_amount, shake_amount)
                    app.yPK1 += random.uniform(-shake_amount, shake_amount)
                    app.opacityPK1 = 70
            if app.step2 % 5==0:
                app.biteUpY2 +=5
                app.biteDownY2 -=5
            if app.step2 ==app.stepsPerSecond*2:
                app.isBite2 = False 
                app.xPK1 = 150
                app.yPK1 = 415
                app.biteUpX2 = 130
                app.biteUpY2 = 330
                app.biteDownY2 = 530
                app.step2 = 0
                app.opacityPK1 = 100
                app.start2 = False 
                p.health -= random.randint(10,20)
                app.turn = 0

        if app.hpPK2 <=0:
            self.endWin = True
            app.hpPK2 = 100

        if p.health <=1:
            self.endLost = True
            app.hpPK2 = 100




    def onKeyPress(self,key):
        #gcalling the values from p as we pass the information page 
        if key != None: 
            app.mouseCount +=1
            app.stepInfo = 0

            app.namePK1 = p.pokemonChosen.name
            app.pk1 = p.pokemonChosen.backPhoto
            app.myPKskillSet = p.pokemonChosen.skill
            app.realStart = True 
            app.firstSkill = app.myPKskillSet[0]
            app.secondSkill = app.myPKskillSet[1]
            app.thirdSkill = app.myPKskillSet[2]
            app.forthSkill = app.myPKskillSet[3]
            app.step = 0


        if app.mouseCount ==2:
            app.keyScreen = False
            app.stepInfo = 0
            app.namePK1 = p.pokemonChosen.name
            app.pk1 = p.pokemonChosen.backPhoto
            app.myPKskillSet = p.pokemonChosen.skill
            app.realStart = True 
            app.firstSkill = app.myPKskillSet[0]
            app.secondSkill = app.myPKskillSet[1]
            app.thirdSkill = app.myPKskillSet[2]
            app.forthSkill = app.myPKskillSet[3]
            app.step =0
            # app.hpPK1 = p.health




        





    



