from cmu_graphics import * 
import p
import random

class SaliorStadium:
    #only battles with  Gyarados as it is saluir's stadium 
    # it is mostly same alogrthim but had to fix all of  the x and y values as the 
    # background chnages. 
    battleEndLose = False 
    battleEndWin = False 
    def onAppStart(self):
        # p.loadtedData() 
        app.figthingGroundS = "fighting_ground.png"
        app.xPK1S = 100
        app.yPK1S = 450
        app.xPK2S = 440
        app.yPK2S = 100
        # app.namePK1 = p.pokemonChosen.name
        # app.pk1 = p.pokemonChosen.backPhoto
        # app.myPKskillSet = p.pokemonChosen.skill
        app.pk2S = p.Gyarados.frontPhoto
        app.namePK2S = p.Gyarados.name
        app.oppententPKSkillSetS = p.Gyarados.skill
        app.hpPK1S = 100
        app.hpPK2S = 100
        app.turnS = 0
        app.opacityPK1S = 100
        app.opacityPK2S = 100
        app.startS = False
        app.start2S = False 
        app.keyScreenS = True
        app.loadingImageS = "loading.png"
        app.loadImageXS = 250
        app.loadImageYS = 200
        app.stepInfoS = 0
        app.mouseCountS = 0
        app.realStartS = False  
    #     # app.firstSkill = app.myPKskillSet[0]
    #     # app.secondSkill = app.myPKskillSet[1]
    #     # app.thirdSkill = app.myPKskillSet[2]
    #     # app.forthSkill = app.myPKskillSet[3]
        app.skillChosenS = None
        app.startS = False 
        app.isGrowl1S = False 
        app.growlImageS = "growl.png"
        app.isTackle1S = False 
        app.stepS = 0
        app.isVineWhip1S = False 
        app.vineWhipAniS  = "vine_whip.png"
        app.vineWhipRoateS = 0
        # randomNum = random.randint(0,3)
        # skill = app.skillSet[randomNum]
        # app.skill  = (skill)
        app.isLeechSeed1S = False
        app.leechSeedAniS = "leechSeed.png"
        app.leechSeedXS = 190
        app.leechSeedYS = 310
        app.isScratch1S = False 
        app.scratchAniS = "scratch.png"
        app.scratchXS = 450
        app.scratchYS =100
        app.isEmberS = False 
        app.smallEmberS = "ember_small.png"
        # app.smallEmber2 = "ember_small.png"
        # app.smallEmber3 = "ember_small.png"
        app.bigEmberS = "ember_big.png"
        app.smallEmberXS = 260
        app.smallEmberYS = 400
        app.isSmallEmber1S = False
        app.isBigEmber1S = False
        app.bigEmberXS = 450
        app.bigEmberYS = 150
        app.isDragonBreath1S = False 
        app.dragonBreathS = "dragon_Breath.png" 
        app.isTailWhip1S = False
        app.dizzyS = "dizzy.png"
        app.isWaterGun1S = False 
        app.waterGunS = "watergun.png"
        app.isBite1S = False 
        app.biteUpS = "bite.png"
        app.biteDownS = "bite.png"
        app.biteUpXS = 430
        app.biteUpYS = 60
        app.biteDownYS =270
        app.isElectroBallS = False 
        app.electroBallS = "electroBall.png"
        app.electroBallXS = 200
        app.electroBallYS = 420
        app.isElectricityS = False 
        app.electricityS = "electricity.png"
        app.electricityXS = 300
        app.electricityYS = 100
        app.isThunderBoltS = False 
        app.thunderBoltS = "thunderBolt.png"
        app.thunderBoltXS = 440
        app.thunderBoltYS = 40
        app.step2S =0 
        app.oppontentSkillChosenS = None
        # app.isGrowl2 = False 
        # app.isTackle2 = False 
        app.start2S = False 
        # app.tackleEnd = False 
        # app.isViheWhip2 = False
        # app.isLeechSeed2 = False  
        # app.leechSeedX2 = 470
        # app.leechSeedY2 = 180
        app.isScratch2S = False 
        app.scratchX2S = 210
        app.scratchY2S = 385
        # app.isEmber2 = False 
        # app.isSmallEmber2 = False
        # app.isBigEmber2 = False
        # app.smallEmberX2 = 400
        # app.smallEmberY2 = 240
        # app.bigEmberX2 = 150
        # app.bigEmberY2 = 410
        app.isDragonBreath2S = False
        # app.isTailWhip2 = False  
        app.isWaterGun2S = False
        app.isThunderBolt2S = False  
        # app.isBite2 = False 
        # app.biteUpX2 = 130
        # app.biteUpY2 = 330
        # app.biteDownY2 = 530
        app.keyScreen = True 
        app.loadingImage = "loading.png"
        app.loadImageX = 250
        app.loadImageY = 200
        app.stepInfo = 0
        app.mouseCount = 0
        app.realStart = False
        app.isThunderBoltS2 = False  

    def redrawAll(self):
        if app.keyScreenS:
            drawImage(app.loadingImageS,app.loadImageXS,app.loadImageYS )
            drawLabel("Did You Know the first Pokemon Game in already 27??", 400 ,400, font = "monospace", size = 25,fill = "white")
            drawLabel("There are over 1000 species of Pokémon!", 400,440,font = "monospace", size = 25,fill = "white")
            drawLabel("Pokémon means 'Pocket Monsters'",400,480,font = "monospace", size = 25,fill = "white")
            drawLabel("If you didn't chosee the poemon at the choosing phase'",400,520,font = "monospace", size = 23,fill = "white")
            drawLabel("You would have a pokemon as your Pokemon!!(Hidden piece)",400,560,font = "monospace", size = 23,fill = "white")
            drawLabel("You would be kicked out when you HP is low go to the center to heal",400,600,font = "monospace", size = 23,fill = "white")
            drawLabel("HP is low go to the center to heal",400,640,font = "monospace", size = 23,fill = "white")
            drawLabel("Press space two times to continue",400,700,font = "monospace", size = 23,fill = "white")
        else:
            color1 = rgb(148,144,144)
            color2 = rgb(159,123,80)
            gradientColor = gradient(color1, color2,start="top")
            drawRect(0,0,800,800,fill = gradientColor)
            drawImage("pkfloor.png",300,300,rotateAngle = 70)
            imageWidthS, imageHeightS = getImageSize(app.figthingGroundS)
            drawImage(app.figthingGroundS,330,130,width =imageWidthS*1.5 ,height =imageHeightS*1.5 )
            drawImage(app.figthingGroundS,30,470,width =imageWidthS*1.5 ,height =imageHeightS*1.5)
            hpBox = rgb(103,103,88)
            #lowerBox(firstBox)
            drawRect(-3,620,300,95,fill = "white", border = hpBox, borderWidth = 5)
            drawLabel(f"{app.namePK1S}",60,635,size = 20,bold = True)
            hpInnerBox = rgb(193,193,193)
            #black box 
            drawRect(10,650,250,30)
            drawLabel("HP",25,665,fill = "red",size = 20,bold = True )
            drawRect(40,650,240,30,fill = hpInnerBox,borderWidth = 3)
            drawRect(40,655,p.health*2.3,20,fill = "green") #app.hpPK2.health
            drawLabel(f"{p.health}/100",50,695,size = 20)
            #second box 
            drawRect(570,50,300,70,fill = "white", border = hpBox, borderWidth = 5)
            drawLabel(f"{app.namePK2S}",640,70,size = 20,bold = True)
            drawRect(580,80,200,30)
            drawRect(610,80,210,30,fill = hpInnerBox,borderWidth = 3)
            drawLabel("HP",595,95,fill = "red",size = 20,bold = True )
            # if app.hpPK2 <=0:
            #     pass
            #     # self.end = True
            #     # app.hpPK2 = 100
            # else:
            drawRect(610,85,app.hpPK2S*2,20,fill = "green")
            # drawCircle(app.xPK1,app.yPK1,30,fill= "red")
            # drawCircle(app.xPK2,app.yPK2,30,fill = "blue")
            #draw pokemon Image
            drawImage(app.pk1S,app.xPK1S,app.yPK1S,width = 150,height = 150,opacity = app.opacityPK1S)
            drawImage(app.pk2S,app.xPK2S,app.yPK2S,width= 150,height = 150,opacity = app.opacityPK2S)
            #Narrative Box
            drawRect(450,660,320,100,fill = "gray",border = hpInnerBox,borderWidth = 5)
            if app.startS:
                drawLabel(f"{app.namePK1S} had used",610,700,size = 20,align = "center")
                drawLabel(f"{app.skillChosenS}!!",610,720,size = 20,align = "center") 

            if app.start2S == True:
                drawLabel(f"{app.namePK2S} had used",610,700,size = 20,align = "center")
                # print("this is pringint in lin 143")
                drawLabel(f"{app.oppontentSkillChosenS}!!",610,720,size = 20,align = "center") 

            #Skill Set Box 1
            drawRect(500,380,270,60,fill = "gray",border = hpInnerBox,borderWidth = 3)
            drawLabel(app.firstSkillS,630,410,size = 30)
            #skill set box 2
            drawRect(500,445,270,60,fill = "gray",border = hpInnerBox,borderWidth = 3)
            drawLabel(app.secondSkillS,630,475,size = 30)
            #skill set box 3
            drawRect(500,510,270,60,fill = "gray",border = hpInnerBox,borderWidth = 3)
            drawLabel(app.thirdSkillS,630,540,size = 30)
            #skill set box 4
            drawRect(500,575,270,60,fill = "gray",border = hpInnerBox,borderWidth = 3)
            drawLabel(app.forthSkillS,630,605,size = 30,align = "center")

        if app.isGrowl1S == True:
            drawImage(app.growlImageS,200,400,width = 50,height = 50)
            drawImage(app.growlImageS,250,415,width = 50, height = 50 ,rotateAngle = 15)
            drawImage(app.growlImageS,290,450,width = 50, height = 50 ,rotateAngle = 30)
            #drawImage(app.growlImage,app.xPK2 +50,app.yPK2 -15,width = 50, height = 50,rotateAngle = -30)

        
        
        if app.isVineWhip1S == True:
            drawImage(app.vineWhipAniS,450,70,width = 120, height = 120,rotateAngle = app.vineWhipRoateS)

        
        if app.isLeechSeed1S == True:
            print("the image of leechseed is printing")
            drawImage(app.leechSeedAniS,app.leechSeedXS,app.leechSeedYS,width = 200,height = 200,rotateAngle = 20)
        if app.isScratch1S == True:
            print("the iamge of scartch is printing")
            drawImage(app.scratchAniS,app.scratchXS,app.scratchYS,width = 120, height = 120)

        if app.isSmallEmber1S == True:
            emberWidth, emberHeight = getImageSize(app.smallEmberS)
            drawImage(app.smallEmberS,app.smallEmberXS,app.smallEmberYS,width = emberWidth//5,height = emberHeight//5,rotateAngle = -20 )

        if app.isBigEmber1S == True:
            drawImage(app.bigEmberS,app.bigEmberXS,app.bigEmberYS)
        if app.isDragonBreath1S == True:
            dwWidth, dwHeight = getImageSize(app.smallEmberS)
            drawImage(app.dragonBreathS,35,340,width = dwWidth*0.8,height = dwHeight*0.8,rotateAngle = -40)

        if app.isTailWhip1S == True:
            drawImage(app.dizzyS,410,70)

        if app.isWaterGun1S == True:
            wgWidth, wgHeight = getImageSize(app.waterGunS)
            drawImage(app.waterGunS,160,240,width = wgWidth*0.8,height = wgHeight*0.8,rotateAngle = -240)
            
        if app.isBite1S == True:
            drawImage(app.biteUpS,app.biteUpXS,app.biteUpYS)
            drawImage(app.biteDownS,app.biteUpXS+25,app.biteDownYS,rotateAngle = 180)

        if app.isElectroBallS == True:
            drawImage(app.electroBallS,app.electroBallXS,app.electroBallYS)

        if app.isElectricityS == True:
            drawImage(app.electricityS,app.electricityXS,app.electricityYS)

        if app.isThunderBoltS == True:
            tbWidth, twHeight = getImageSize(app.thunderBoltS)
            drawImage(app.thunderBoltS,app.thunderBoltXS,app.thunderBoltYS,width = tbWidth*0.6,height = twHeight*0.6)

        if app.isScratch2S == True:
            drawImage(app.scratchAniS,app.scratchX2S,app.scratchY2S,width = 120, height = 120)


        if app.isWaterGun2S == True:
            wgWidth, wgHeight = getImageSize(app.waterGunS)
            drawImage(app.waterGunS,100,200,width = wgWidth*0.8,height = wgHeight*0.9,rotateAngle = 300)

        
        if app.isDragonBreath2S == True:
            dwWidth, dwHeight = getImageSize(app.smallEmberS)
            print("isDragonBreath2S is printing")
            drawImage(app.dragonBreathS,140,220,width = dwWidth*0.8,height = dwHeight*0.8,rotateAngle = -220)

        if app.isThunderBoltS2 == True:
            tbWidth, twHeight = getImageSize(app.thunderBoltS)
            drawImage(app.thunderBoltS,40,330,width = tbWidth*0.6,height = twHeight*0.6)


    def onKeyPress(self,key):
   
        if key != None: 
            app.mouseCountS +=1
            app.stepInfoS = 0
            app.namePK1S = p.pokemonChosen.name
            app.pk1S = p.pokemonChosen.backPhoto
            app.myPKskillSetS = p.pokemonChosen.skill
            app.realStartS = True 
            app.firstSkillS = app.myPKskillSetS[0]
            app.secondSkillS = app.myPKskillSetS[1]
            app.thirdSkillS = app.myPKskillSetS[2]
            app.forthSkillS = app.myPKskillSetS[3]
            print(app.namePK1S)

        if app.mouseCountS ==2:
            app.keyScreenS = False
            app.stepInfoS = 0
            app.namePK1S = p.pokemonChosen.name
            app.pk1S = p.pokemonChosen.backPhoto
            app.myPKskillSetS = p.pokemonChosen.skill
            app.realStartS = True 
            app.firstSkillS = app.myPKskillSetS[0]
            app.secondSkillS = app.myPKskillSetS[1]
            app.thirdSkillS = app.myPKskillSetS[2]
            app.forthSkillS = app.myPKskillSetS[3]
            # app.hpPK1 = p.health
            print(app.namePK1S)

    def pointInRect(self,x, y, rectX, rectY, rectWidth, rectHeight, skill):
        if rectX <=x <=rectX + rectWidth and rectY <=y <= rectY +rectHeight:
            app.skillChosenS = skill

    def onMousePress(self, x,y):
        if app.turnS ==0:
            app.startS = True 
            # if app.start2:
            #     app.start2 = False 
            # Check if the mouse click is within the first skill box

            self.pointInRect(x, y, 500, 380, 270, 60, app.firstSkillS)
            self.pointInRect(x, y, 500, 445, 270, 60, app.secondSkillS)
            self.pointInRect(x, y, 500, 510, 270, 60, app.thirdSkillS)
            self.pointInRect(x, y, 500, 575, 270, 60, app.forthSkillS)
            if app.skillChosenS == "Growl":
                app.isGrowl1S = True
                app.opacityPK2S = 70
            if app.skillChosenS == "Tackle":
                app.xPK1S += 230
                app.yPK1S -= 230
                app.yPK2S -= 30
                app.opacityPK2S =70
                app.isTackle1S = True 
            app.isVineWhip1S = True if app.skillChosenS == "Vine Whip" else False
            app.isLeechSeed1S = True if app.skillChosenS == "Leech Seed" else False 
            app.isScratch1S = True if app.skillChosenS == "Scratch" else False 

            if app.skillChosenS == "Ember":
                app.isEmberS = True 
                app.isSmallEmber1S = True
            app.isDragonBreath1S = True if app.skillChosenS == "Dragon Breath" else False 
            app.isTailWhip1S = True if app.skillChosenS == "Tail Whip" else False
            app.isWaterGun1S = True if app.skillChosenS == "Water Gun" else False 
            app.isBite1S = True if app.skillChosenS == "Bite" else False
            app.isElectroBallS = True if app.skillChosenS == "Electro Ball" else False 
            app.isThunderBoltS = True if app.skillChosenS == "ThunderBolt" else False 
        if app.turnS ==0:
            app.turnS  = 0.5

    def onStep(self):

        if p.health <= 0:
            p.health = 1
        
        if app.hpPK2S <= 0:
            app.hpPK2S = 1
            print("app.hpK2S becoming 0 ")
        

        # if p.health <0:
        #     p.health = 0

        # if app.hpPK2S <=0:
        #     self.battleEnd = True
        #     app.hpPK2S = 100

        # if p.health <=1:
        #     self.battleEnd = True
        #     app.hpPK2S = 100


        if app.keyScreenS:
            app.stepInfoS +=1
            if app.stepInfoS %30==0:
                app.loadImageYS +=5
            if app.stepInfoS % 50 ==0:
                app.loadImageYS -=5

        if p.health <= 1 or app.hpPK2S <=1:
            print("the game eneded")
            # make the end screen 

        if app.isTackle1S == True:
            # print("this is pringing in line 372 ")
            app.stepS +=1 
            if app.stepS %60 ==0:
                # print("this is running in 374")
                app.xPK1S -=230
                app.yPK1S +=230
                app.yPK2S += 30
                app.stepS = 0 
                app.opacityPK2S = 100
                app.isTackle1S = False 
                app.startS = False
                app.hpPK2S -= random.randint(10,20) 
                # print("thi si runnninh ")

        if app.isGrowl1S == True:
            app.stepS +=1
            if app.stepS %30 ==0:
                app.isGrowl1S = False 
                app.opacityPK2S =100
                app.stepS = 0 
                app.startS = False 
                app.hpPK2S -= random.randint(10,20)

        if app.isVineWhip1S == True:
            app.stepS +=1
            if app.stepS % 10==0:
                app.vineWhipRoateS = 30
                app.opacityPK2S =70
            if app.stepS %50 ==0:
                app.isVineWhip1S = False
                app.stepS = 0
                app.vineWhipRoateS = 0
                app.opacityPK2S =100
                app.startS = False 
                app.hpPK2S -= random.randint(10,20)

        if app.isLeechSeed1S == True:
            app.stepS +=1
            print("this is printing in line 410")
            if app.stepS %10 ==0:
                print("this is printing in line 412")
                app.leechSeedXS +=55
                app.leechSeedYS -=25
            if app.stepS %60 ==0:
                print("this is printing in line 416")
                app.opacityPK2S =70
                app.leechSeedXS = 190
                app.leechSeedYS = 310
            if app.stepS > 61:
                print("this is printing in line 421")
                app.stepS = 0
                app.opacityPK2S = 100
                app.isLeechSeed1S = False 
                app.startS = False
                app.hpPK2S -= random.randint(10,20)

        if app.isScratch1S ==True:
            app.stepS +=1 
            print("it is printing now in line 432")
            if app.stepS %5 ==0:
                app.scratchXS -= 5
                app.scratchYS +=5
            print("it is printing now in line 436")
            if app.stepS == app.stepsPerSecond * 0.5:
                app.opacityPK2S =70
            if app.stepS > 70:
                print("it is printing now in line 440")
                app.stepS = 0
                app.opacityPK2S = 100
                app.isScratch1S = False 
                app.scratchXS = 450
                app.scratchYS =100
                app.startS = False
                app.hpPK2S -= random.randint(10,20)

        if app.isSmallEmber1S == True:
            app.stepS+=1
            if app.stepS %10 ==0:
                app.smallEmberXS +=35
                app.smallEmberYS -=35
            if app.stepS == app.stepsPerSecond *2.3:
                app.smallEmberXS = 260
                app.smallEmberYS = 400
                app.isSmallEmber1S = False
                app.stepS = 0
                app.isBigEmberS = True
                app.hpPK2S -= random.randint(10,20)
                app.startS = False 

        # if app.isBigEmber1S == True:
        #     app.stepS +=1
        #     app.opacityPK2S = 70
        #     if app.stepS % 5 == 0:  # Adjust the frequency of the shake
        #             shake_amountS = 10  # Adjust the shake amount
        #             app.bigEmberXS += random.uniform(-shake_amountS, shake_amountS)
        #     if app.stepS > app.stepsPerSecond * 1.1:
        #         app.stepS = 0
        #         app.opacityPK2S = 100
        #         app.isBigEmber1S = False 
        #         app.bigEmberXS = 450
        #         app.bigEmberYS = 150
        #         app.xPK2S = 470
        #         app.startS = False
        #         app.hpPK2S -= random.randint(10,20)
        #         app.emberS = False 

        if app.isDragonBreath1S == True:
            app.stepS +=1
            app.opacityPK2S = 70
            print("this is printing in line 470")
            if app.stepS % 5 == 0:  # Adjust the frequency of the shake
                    print("this is printing in line 472")
                    shake_amountS = 10  # Adjust the shake amount
                    app.xPK2S += random.uniform(-shake_amountS, shake_amountS)
            if app.stepS % 30 ==0:
                print("this is printing in line 476" , app.stepsPerSecond)
                app.isDragonBreath1S = False
                app.stepS = 0
                app.opacityPK2S =100
                app.xPK2S = 470
                app.startS = False 
                app.hpPK2S -= random.randint(10,20)


        if app.isTailWhip1S == True:
            app.stepS+=1
            if app.stepS % 5 == 0:  # Adjust the frequency of the shake
                    shake_amountS = 10  # Adjust the shake amount
                    app.xPK1S += random.uniform(-shake_amountS, shake_amountS)
                    app.yPK1S += random.uniform(-shake_amountS, shake_amountS)
                    app.opacityPK2S = 70
            if app.stepS  %30 ==0:
                app.isTailWhip1S = False
                app.stepS = 0
                app.opacityPK2S =100
                app.xPK1S = 100
                app.yPK1S = 450
                app.startS = False
                app.hpPK2S -= random.randint(10,20)


        if app.isWaterGun1S == True:
            app.stepS +=1
            app.opacityPK2S = 70
            if app.stepS  %30 ==0:
                app.isWaterGun1S = False 
                app.opacityPK2S =100
                app.stepS = 0 
                app.startS = False 
                app.hpPK2S -= random.randint(10,20)


        if app.isBite1S ==True:
            app.stepS +=1
            if app.stepS % 5 == 0:  # Adjust the frequency of the shake
                    shake_amountS = 5  # Adjust the shake amount
                    app.xPK2S += random.uniform(-shake_amountS, shake_amountS)
                    app.yPK2S += random.uniform(-shake_amountS, shake_amountS)
                    app.opacityPK2S = 70
            if app.stepS % 5==0:
                app.biteUpYS +=5
                app.biteDownYS -=5
            if app.stepS  %60 ==0:
                app.isBite1S = False 
                app.xPK2S = 440
                app.yPK2S = 100
                app.biteUpXS = 430
                app.biteUpYS = 60
                app.stepS = 0
                app.biteDownYS =270
                app.opacityPK2S = 100
                app.startS = False 
                app.hpPK2S -= random.randint(10,20)

        if app.isElectroBallS == True:
            app.stepS+=1
            if app.stepS %10 ==0:
                app.electroBallXS +=35
                app.electroBallYS -=35
            if app.stepS  %(30*2.3) ==0:
                app.electroBallXS = 200
                app.electroBallYS = 420
                app.isElectroBallS = False
                app.stepS = 0
                app.isElectricityS = True
                app.startS = False 
                app.hpPK2S -= random.randint(10,20)


        if app.isElectricityS == True:
            app.stepS +=1
            app.opacityPK2S = 70
            if app.stepS % 5 == 0:  # Adjust the frequency of the shake
                    shake_amountS = 10  # Adjust the shake amount
                    app.electricityXS += random.uniform(-shake_amountS, shake_amountS)
            if app.stepS >  30*1.1:
                app.stepS = 0
                app.opacityPK2S= 100
                app.isElectricityS = False 
                app.electricityXS = 300
                app.electricityYS = 100
                app.xPK2S = 470
                app.startS = False 
                app.hpPK2S -= random.randint(10,20)



        if app.isThunderBoltS ==True:
            app.stepS+=1
            if app.stepS % 5 == 0:  # Adjust the frequency of the shake
                    shake_amountS = 10  # Adjust the shake amount
                    app.xPK1S += random.uniform(-shake_amountS, shake_amountS)
                    app.yPK1S += random.uniform(-shake_amountS, shake_amountS)
                    app.opacityPK2S = 70
                    app.startS = False 

            if app.stepS  %30 ==0:
                app.isThunderBoltS = False
                app.stepS = 0
                app.opacityPK2S =100
                app.xPK1S = 100
                app.yPK1S = 450
                app.hpPK2S -= random.randint(10,20)

        if app.turnS ==0.5:
            app.step2S +=1
            #change 50 to 150
            if app.step2S %100 ==0:
                app.turnS =1
                app.step2S =0
                app.start2S = True
                # print("line 497" , app.start2S)

        if app.turnS ==1:
            app.step2S +=1
            #change 50 to 150
            if app.step2S %100 ==0:
                app.turnS =1
                app.stepS =0
                app.start2S = True
                # print("line 497" , app.start2S)

        if app.turnS ==1:
            # print("this is working in line 588")
            app.turnS = 0
            skillRandom = random.randint(0,2)
            app.oppontentSkillChosenS = app.oppententPKSkillSetS[skillRandom]
            print(app.oppontentSkillChosenS)
            if app.oppontentSkillChosenS == "Scratch":
                print("Scratch is chosen for 2 ")
                app.isScratch2S = True
                app.turnS = 0

            if app.oppontentSkillChosenS == "Water Gun":
                print("water gun is chosen for 2 ")
                app.isWaterGun2S = True
                app.turnS = 0

            if app.oppontentSkillChosenS == "ThunderBolt":
                print("ThunderBolt is chosen for 2 ")
                app.isThunderBoltS2 = True
                app.turnS = 0
            if app.oppontentSkillChosenS == "Dragon Breath":
                print("Dragon Breath is chosen for 2 ")
                app.isDragonBreath2S = True
                app.turnS = 0
        if app.isScratch2S==True:
            app.step2S +=1 
            if app.step2S %5 ==0:
                app.scratchX2S -= 10
                app.scratchY2S += 10
            if app.step2S == app.stepsPerSecond * 0.5:
                app.opacityPK1S =70
            if app.step2S > app.stepsPerSecond * 1.4:
                app.step2S = 0
                app.opacityPK1S = 100
                app.isScratch2S = False 
                app.scratchX2S = 210
                app.scratchY2S =385
                app.start2S = False
                p.health -= random.randint(10,20)

            app.turn = 0

        if app.isDragonBreath2S == True:
            app.step2S +=1
            app.opacityPK1S = 70
            if app.step2S % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 10  # Adjust the shake amount
                    app.xPK1S += random.uniform(-shake_amount, shake_amount)
            if app.step2S ==app.stepsPerSecond:
                app.isDragonBreath2S = False
                app.step2S = 0
                app.opacityPK1S =100
                app.xPK1S = 140
                app.start2S = False 
                p.health -= random.randint(10,20)
                app.turnS = 0

        if app.isWaterGun2S ==True:
            app.step2S +=1
            app.opacityPK1S = 70
            if app.step2S ==app.stepsPerSecond:
                app.isWaterGun2S = False 
                app.opacityPK1S =100
                app.step2S = 0 
                app.start2S = False 
                p.health -= random.randint(10,20)
                app.turnS = 0

        if app.isThunderBoltS2 == True: 
            app.step2S +=1
            if app.step2S % 5 == 0:  # Adjust the frequency of the shake
                    shake_amountS = 10  # Adjust the shake amount
                    app.xPK2S += random.uniform(-shake_amountS, shake_amountS)
                    app.yPK2S += random.uniform(-shake_amountS, shake_amountS)
                    app.opacityPK1S = 70
                    # app.start2S = False
                    # p.health -= random.randint(10,20)
                    # app.turnS = 0 

            if app.step2S  %30 ==0:
                app.isThunderBoltS2 = False
                app.step2S = 0
                app.opacityPK1S =100
                app.xPK2S = 440
                app.yPK2S = 100
                app.turnS = 0
                app.start2S = False
                p.health  -= random.randint(10,20)

        if p.health <= 0:
            self.battleEndLose = True

        if app.hpPK2S <= 0:
            app.hpPK2S = 100
            self.battleEndWin = True            
