from cmu_graphics import *
import random
import p

class HigherFight:
    # it is batllte scnece when we have to fight with a Onix 
    battleEndLoseH = False 
    battleEndWinH = False 
    def onAppStart(self):
        # p.loadtedData() 
        app.figthingGroundS = "fighting_ground.png"
        app.xPK1H = 100
        app.yPK1H = 450
        app.xPK2H = 440
        app.yPK2H = 100
        # app.namePK1 = p.pokemonChosen.name
        # app.pk1 = p.pokemonChosen.backPhoto
        # app.myPKskillSet = p.pokemonChosen.skill
        app.pk2H = p.Onix.frontPhoto
        app.namePK2H = p.Onix.name
        app.oppententPKSkillSetH = p.Onix.skill
        app.hpPK1H = 100
        app.hpPK2H = 100
        app.turnH = 0
        app.opacityPK1H = 100
        app.opacityPK2H = 100
        app.startH = False
        app.start2H = False 
        app.keyScreenHH = True
        app.loadingImageHH = "loading.png"
        app.loadImageXHH = 250
        app.loadImageYHH = 200
        app.stepInfoHH = 0
        app.mouseCountHH = 0
        app.realStartHH = False  
    #     # app.firstSkill = app.myPKskillSet[0]
    #     # app.secondSkill = app.myPKskillSet[1]
    #     # app.thirdSkill = app.myPKskillSet[2]
    #     # app.forthSkill = app.myPKskillSet[3]
        app.skillChosenH = None
        app.startH = False 
        app.isGrowl1H = False 
        app.growlImageH = "growl.png"
        app.isTackle1H = False 
        app.stepH = 0
        app.isVineWhip1H = False 
        app.vineWhipAniH  = "vine_whip.png"
        app.vineWhipRoateH = 0
        # randomNum = random.randint(0,3)
        # skill = app.skillSet[randomNum]
        # app.skill  = (skill)
        app.isLeechSeed1H = False
        app.leechSeedAniH = "leechSeed.png"
        app.leechSeedXH = 190
        app.leechSeedYH = 310
        app.isScratch1H = False 
        app.scratchAniH = "scratch.png"
        app.scratchXH = 450
        app.scratchYH =100
        app.isEmberH = False 
        app.smallEmberH = "ember_small.png"
        # app.smallEmber2 = "ember_small.png"
        # app.smallEmber3 = "ember_small.png"
        app.bigEmberH = "ember_big.png"
        app.smallEmberXH = 260
        app.smallEmberYH = 400
        app.isSmallEmber1H = False
        app.isBigEmber1H = False
        app.bigEmberXH = 450
        app.bigEmberYH = 150
        app.isDragonBreath1H = False 
        app.dragonBreathH = "dragon_Breath.png" 
        app.isTailWhip1H = False
        app.dizzyH = "dizzy.png"
        app.isWaterGun1H = False 
        app.waterGunH = "watergun.png"
        app.isBite1H = False 
        app.biteHUpH = "bite.png"
        app.biteHDownH = "bite.png"
        app.biteHUpXH = 430
        app.biteHUpYH = 60
        app.biteHDownYH =270
        app.isElectroBallH = False 
        app.electroBallH = "electroBall.png"
        app.electroBallXH = 200
        app.electroBallYH = 420
        app.isElectricityH = False 
        app.electricityH = "electricity.png"
        app.electricityXH = 300
        app.electricityYH = 100
        app.isThunderBoltH = False 
        app.thunderBoltH = "thunderBolt.png"
        app.thunderBoltXH = 440
        app.thunderBoltYH = 40
        app.step2HH =0 
        app.oppontentSkillChosenH = None
        app.isGrowl2H = False 
        app.isTackle2H = False 
        app.start2H = False 
        # app.tackleEnd = False 
        # app.isViheWhip2 = False
        # app.isLeechSeed2 = False  
        # app.leechSeedX2 = 470
        # app.leechSeedY2 = 180
        app.isScratch2H = False 
        app.scratchX2H = 210
        app.scratchY2H = 385
        # app.isEmber2 = False 
        # app.isSmallEmber2 = False
        # app.isBigEmber2 = False
        # app.smallEmberX2 = 400
        # app.smallEmberY2 = 240
        # app.bigEmberX2 = 150
        # app.bigEmberY2 = 410
        app.isBite2H = False
        # app.isTailWhip2 = False  
        app.isWaterGun2S = False
        app.isThunderBolt2S = False  
        # app.isBite2 = False 
        app.biteUpX2H = 130
        app.biteUpY2H = 330
        app.biteDownY2H = 530
        app.keyScreenH = True 
        app.loadingImageH = "loading.png"
        app.loadImageXH = 250
        app.loadImageYH = 200
        app.stepInfoH = 0
        app.mouseCountH = 0
        app.realStartH = False
        app.isThunderBoltH2 = False 
  

    def redrawAll(self):
        if app.keyScreenHH:
            drawImage(app.loadingImageHH,app.loadImageXHH,app.loadImageYHH )
            drawLabel("Did You Know the first Pokemon Game in already 27??", 400 ,400, font = "monospace", size = 25,fill = "white")
            drawLabel("There are over 1000 species of Pokémon!", 400,440,font = "monospace", size = 25,fill = "white")
            drawLabel("Pokémon means 'Pocket Monsters'",400,480,font = "monospace", size = 25,fill = "white")
            drawLabel("If you didn't chosee the poemon at the choosing phase'",400,520,font = "monospace", size = 23,fill = "white")
            drawLabel("You would have a pokemon as your Pokemon!!(Hidden piece)",400,560,font = "monospace", size = 23,fill = "white")
            drawLabel("You would be kicked out when you HP is low go to the center to heal",400,600,font = "monospace", size = 23,fill = "white")
            drawLabel("HP is low go to the center to heal",400,640,font = "monospace", size = 23,fill = "white")
            drawLabel("Press space two times to continue",400,700,font = "monospace", size = 23,fill = "white")
        else:
            blueColor = rgb(0,151,217)
            firstColor = rgb(110,213,192)
            secondColor = rgb(134,210,116)
            gradientColor = gradient(blueColor,firstColor,secondColor,start = "top")
            drawRect(0,0,app.width,app.height,fill = gradientColor)
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
            drawLabel(f"{app.namePK2H}",640,70,size = 20,bold = True)
            drawRect(580,80,200,30)
            drawRect(610,80,210,30,fill = hpInnerBox,borderWidth = 3)
            drawLabel("HP",595,95,fill = "red",size = 20,bold = True )
            # if app.hpPK2 <=0:
            #     pass
            #     # self.end = True
            #     # app.hpPK2 = 100
            # else:
            drawRect(610,85,app.hpPK2H*2,20,fill = "green")
            # drawCircle(app.xPK1,app.yPK1,30,fill= "red")
            # drawCircle(app.xPK2,app.yPK2,30,fill = "blue")
            #draw pokemon Image
            drawImage(app.pk1S,app.xPK1H,app.yPK1H,width = 150,height = 150,opacity = app.opacityPK1H)
            drawImage(app.pk2H,app.xPK2H,app.yPK2H,width= 150,height = 150,opacity = app.opacityPK2H)
            #Narrative Box
            drawRect(450,660,320,100,fill = "gray",border = hpInnerBox,borderWidth = 5)
            if app.startH:
                drawLabel(f"{app.namePK1S} had used",610,700,size = 20,align = "center")
                drawLabel(f"{app.skillChosenH}!!",610,720,size = 20,align = "center") 

            if app.start2H == True:
                drawLabel(f"{app.namePK2H} had used",610,700,size = 20,align = "center")
                # print("this is pringint in lin 143")
                drawLabel(f"{app.oppontentSkillChosenH}!!",610,720,size = 20,align = "center") 

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

        if app.isGrowl1H == True:
            drawImage(app.growlImageH,200,400,width = 50,height = 50)
            drawImage(app.growlImageH,250,415,width = 50, height = 50 ,rotateAngle = 15)
            drawImage(app.growlImageH,290,450,width = 50, height = 50 ,rotateAngle = 30)
            #drawImage(app.growlImage,app.xPK2 +50,app.yPK2 -15,width = 50, height = 50,rotateAngle = -30)

        
        
        if app.isVineWhip1H == True:
            drawImage(app.vineWhipAniH,450,70,width = 120, height = 120,rotateAngle = app.vineWhipRoateH)

        
        if app.isLeechSeed1H == True:
            print("the image of leechseed is printing")
            drawImage(app.leechSeedAniH,app.leechSeedXH,app.leechSeedYH,width = 200,height = 200,rotateAngle = 20)
        if app.isScratch1H == True:
            print("the iamge of scartch is printing")
            drawImage(app.scratchAniH,app.scratchXH,app.scratchYH,width = 120, height = 120)

        if app.isSmallEmber1H == True:
            emberWidth, emberHeight = getImageSize(app.smallEmberH)
            drawImage(app.smallEmberH,app.smallEmberXH,app.smallEmberYH,width = emberWidth//5,height = emberHeight//5,rotateAngle = -20 )

        if app.isBigEmber1H == True:
            drawImage(app.bigEmberH,app.bigEmberXH,app.bigEmberYH)
        if app.isDragonBreath1H == True:
            dwWidth, dwHeight = getImageSize(app.smallEmberH)
            drawImage(app.dragonBreathH,35,340,width = dwWidth*0.8,height = dwHeight*0.8,rotateAngle = -40)

        if app.isTailWhip1H == True:
            drawImage(app.dizzyH,410,70)

        if app.isWaterGun1H == True:
            wgWidth, wgHeight = getImageSize(app.waterGunH)
            drawImage(app.waterGunH,160,240,width = wgWidth*0.8,height = wgHeight*0.8,rotateAngle = -240)
            
        if app.isBite1H == True:
            drawImage(app.biteHUpH,app.biteHUpXH,app.biteHUpYH)
            drawImage(app.biteHDownH,app.biteHUpXH+25,app.biteHDownYH,rotateAngle = 180)

        if app.isElectroBallH == True:
            drawImage(app.electroBallH,app.electroBallXH,app.electroBallYH)

        if app.isElectricityH == True:
            drawImage(app.electricityH,app.electricityXH,app.electricityYH)

        if app.isThunderBoltH == True:
            tbWidth, twHeight = getImageSize(app.thunderBoltH)
            drawImage(app.thunderBoltH,app.thunderBoltXH,app.thunderBoltYH,width = tbWidth*0.6,height = twHeight*0.6)

        if app.isScratch2H == True:
            drawImage(app.scratchAniH,app.scratchX2H,app.scratchY2H,width = 120, height = 120)

        if app.isBite2H == True:
            drawImage(app.biteHUpH,app.biteUpX2H,app.biteUpY2H)
            drawImage(app.biteHDownH,app.biteUpX2H+25,app.biteDownY2H,rotateAngle = 180)

        if app.isGrowl2H ==True:
            drawImage(app.growlImage,390,190,width = 50,height = 50)
            drawImage(app.growlImage,430,230,width = 50, height = 50 ,rotateAngle = -15)
            drawImage(app.growlImage,470,270,width = 50, height = 50 ,rotateAngle = -30)







    def onKeyPress(self,key):
        # if p. name == "Bulbasaur":
        #         p.pokemonChosen = p.Bulbasaur

        # if p.name =="Charmander":
        #     p.pokemonChosen = p.Charmander

        # if p.name =="Squirtle":
        #     p.pokemonChosen = p.Squirtle

        # if p.name =="Pikachu":
        #     p.pokemonChosen = p.Pikachu

        # if p.name =="Gyarados":
        #     p.pokemonChosen = p.Gyarados

        # if p.name == "Onix":
        #     p.pokemonChosen = p.Onix
        if key != None: 
            app.mouseCountHH +=1
            app.stepInfoHH = 0
            app.namePK1S = p.pokemonChosen.name
            app.pk1S = p.pokemonChosen.backPhoto
            app.myPKskillSetS = p.pokemonChosen.skill
            app.realStartHH = True 
            app.firstSkillS = app.myPKskillSetS[0]
            app.secondSkillS = app.myPKskillSetS[1]
            app.thirdSkillS = app.myPKskillSetS[2]
            app.forthSkillS = app.myPKskillSetS[3]
            print(app.namePK1S)

        if app.mouseCountHH ==2:
            app.keyScreenHH = False
            app.stepInfoHH = 0
            app.namePK1S = p.pokemonChosen.name
            app.pk1S = p.pokemonChosen.backPhoto
            app.myPKskillSetS = p.pokemonChosen.skill
            app.realStartHH = True 
            app.firstSkillS = app.myPKskillSetS[0]
            app.secondSkillS = app.myPKskillSetS[1]
            app.thirdSkillS = app.myPKskillSetS[2]
            app.forthSkillS = app.myPKskillSetS[3]
            # app.hpPK1 = p.health
            print(app.namePK1S)


    def pointInRect(self,x, y, rectX, rectY, rectWidth, rectHeight, skill):
        if rectX <=x <=rectX + rectWidth and rectY <=y <= rectY +rectHeight:
            app.skillChosenH = skill

    def onMousePress(self, x,y):
        if app.turnH ==0:
            app.startH = True 
            # if app.start2:
            #     app.start2 = False 
            # Check if the mouse click is within the first skill box
            self.pointInRect(x, y, 500, 380, 270, 60, app.firstSkillS)
            self.pointInRect(x, y, 500, 445, 270, 60, app.secondSkillS)
            self.pointInRect(x, y, 500, 510, 270, 60, app.thirdSkillS)
            self.pointInRect(x, y, 500, 575, 270, 60, app.forthSkillS)

            if app.skillChosenH == "Growl":
                app.isGrowl1H = True
                app.opacityPK2H = 70

            
            if app.skillChosenH == "Tackle":
                app.xPK1H += 230
                app.yPK1H -= 230
                app.yPK2H -= 30
                app.opacityPK2H =70
                app.isTackle1H = True 

            if app.skillChosenH == "Vine Whip":
                app.isVineWhip1H = True 

            if app.skillChosenH == "Leech Seed":
                app.isLeechSeed1H = True 

            if app.skillChosenH == "Scratch":
                app.isScratch1H = True 

            if app.skillChosenH == "Ember":
                app.isEmberH = True 
                app.isSmallEmber1H = True

            if app.skillChosenH == "Dragon Breath":
                app.isDragonBreath1H = True 

            if app.skillChosenH == "Tail Whip":
                app.isTailWhip1H = True

            if app.skillChosenH == "Water Gun":
                app.isWaterGun1H = True

            if app.skillChosenH == "Bite":
                app.isBite1H = True 

            if app.skillChosenH == "Electro Ball":
                app.isElectroBallH = True

            if app.skillChosenH == "ThunderBolt":
                app.isThunderBoltH = True

        if app.turnH ==0:
            app.turnH  = 0.5

    def onStep(self):

        if p.health <= 0:
            p.health = 1
        
        if app.hpPK2H <= 0:
            app.hpPK2H = 1
            print("app.hpK2S becoming 0 ")

        if app.keyScreenHH:
            app.stepInfoHH +=1
            if app.stepInfoHH %30==0:
                app.loadImageYHH +=5
            if app.stepInfoHH % 50 ==0:
                app.loadImageYHH -=5

        if p.health <= 1 or app.hpPK2H <=1:
            print("the game eneded")
            # make the end screen 

        if app.isTackle1H == True:
            # print("this is pringing in line 372 ")
            app.stepH +=1 
            if app.stepH %60 ==0:
                # print("this is running in 374")
                app.xPK1H -=230
                app.yPK1H +=230
                app.yPK2H += 30
                app.stepH = 0 
                app.opacityPK2H = 100
                app.isTackle1H = False 
                app.startH = False
                app.hpPK2H -= random.randint(10,20) 
                # print("thi si runnninh ")

        if app.isGrowl1H == True:
            app.stepH +=1
            if app.stepH %30 ==0:
                app.isGrowl1H = False 
                app.opacityPK2H =100
                app.stepH = 0 
                app.startH = False 
                app.hpPK2H -= random.randint(10,20)

        if app.isVineWhip1H == True:
            app.stepH +=1
            if app.stepH % 10==0:
                app.vineWhipRoateH = 30
                app.opacityPK2H =70
            if app.stepH %50 ==0:
                app.isVineWhip1H = False
                app.stepH = 0
                app.vineWhipRoateH = 0
                app.opacityPK2H =100
                app.startH = False 
                app.hpPK2H -= random.randint(10,20)

        if app.isLeechSeed1H == True:
            app.stepH +=1
            print("this is printing in line 410")
            if app.stepH %10 ==0:
                print("this is printing in line 412")
                app.leechSeedXH +=55
                app.leechSeedYH -=25
            if app.stepH %60 ==0:
                print("this is printing in line 416")
                app.opacityPK2H =70
                app.leechSeedXH = 190
                app.leechSeedYH = 310
            if app.stepH > 61:
                print("this is printing in line 421")
                app.stepH = 0
                app.opacityPK2H = 100
                app.isLeechSeed1H = False 
                app.startH = False
                app.hpPK2H -= random.randint(10,20)

        if app.isScratch1H ==True:
            app.stepH +=1 
            print("it is printing now in line 432")
            if app.stepH %5 ==0:
                app.scratchXH -= 5
                app.scratchYH +=5
            print("it is printing now in line 436")
            if app.stepH == app.stepsPerSecond * 0.5:
                app.opacityPK2H =70
            if app.stepH > 70:
                print("it is printing now in line 440")
                app.stepH = 0
                app.opacityPK2H = 100
                app.isScratch1H = False 
                app.scratchXH = 450
                app.scratchYH =100
                app.startH = False
                app.hpPK2H -= random.randint(10,20)

        if app.isSmallEmber1H == True:
            app.stepH+=1
            if app.stepH %10 ==0:
                app.smallEmberXH +=35
                app.smallEmberYH -=35
            if app.stepH == app.stepsPerSecond *2.3:
                app.smallEmberXH = 260
                app.smallEmberYH = 400
                app.isSmallEmber1H = False
                app.stepH = 0
                app.isBigEmberS = True
                app.hpPK2H -= random.randint(10,20)
                app.startH = False 


        if app.isDragonBreath1H == True:
            app.stepH +=1
            app.opacityPK2H = 70
            print("this is printing in line 470")
            if app.stepH % 5 == 0:  # Adjust the frequency of the shake
                    print("this is printing in line 472")
                    shake_amountS = 10  # Adjust the shake amount
                    app.xPK2H += random.uniform(-shake_amountS, shake_amountS)
            if app.stepH % 30 ==0:
                print("this is printing in line 476" , app.stepsPerSecond)
                app.isDragonBreath1H = False
                app.stepH = 0
                app.opacityPK2H =100
                app.xPK2H = 470
                app.startH = False 
                app.hpPK2H -= random.randint(10,20)


        if app.isTailWhip1H == True:
            app.stepH+=1
            if app.stepH % 5 == 0:  # Adjust the frequency of the shake
                    shake_amountS = 10  # Adjust the shake amount
                    app.xPK1H += random.uniform(-shake_amountS, shake_amountS)
                    app.yPK1H += random.uniform(-shake_amountS, shake_amountS)
                    app.opacityPK2H = 70
            if app.stepH  %30 ==0:
                app.isTailWhip1H = False
                app.stepH = 0
                app.opacityPK2H =100
                app.xPK1H = 100
                app.yPK1H = 450
                app.startH = False
                app.hpPK2H -= random.randint(10,20)


        if app.isWaterGun1H == True:
            app.stepH +=1
            app.opacityPK2H = 70
            if app.stepH  %30 ==0:
                app.isWaterGun1H = False 
                app.opacityPK2H =100
                app.stepH = 0 
                app.startH = False 
                app.hpPK2H -= random.randint(10,20)


        if app.isBite1H ==True:
            app.stepH +=1
            if app.stepH % 5 == 0:  # Adjust the frequency of the shake
                    shake_amountS = 5  # Adjust the shake amount
                    app.xPK2H += random.uniform(-shake_amountS, shake_amountS)
                    app.yPK2H += random.uniform(-shake_amountS, shake_amountS)
                    app.opacityPK2H = 70
            if app.stepH % 5==0:
                app.biteHUpYH +=5
                app.biteHDownYH -=5
            if app.stepH  %60 ==0:
                app.isBite1H = False 
                app.xPK2H = 440
                app.yPK2H = 100
                app.biteHUpXH = 430
                app.biteHUpYH = 60
                app.stepH = 0
                app.biteHDownYH =270
                app.opacityPK2H = 100
                app.startH = False 
                app.hpPK2H -= random.randint(10,20)

        if app.isElectroBallH == True:
            app.stepH+=1
            if app.stepH %10 ==0:
                app.electroBallXH +=35
                app.electroBallYH -=35
            if app.stepH  %(30*2.3) ==0:
                app.electroBallXH = 200
                app.electroBallYH = 420
                app.isElectroBallH = False
                app.stepH = 0
                app.isElectricityH = True
                app.startH = False 
                app.hpPK2H -= random.randint(10,20)


        if app.isElectricityH == True:
            app.stepH +=1
            app.opacityPK2H = 70
            if app.stepH % 5 == 0:  # Adjust the frequency of the shake
                    shake_amountS = 10  # Adjust the shake amount
                    app.electricityXH += random.uniform(-shake_amountS, shake_amountS)
            if app.stepH >  30*1.1:
                app.stepH = 0
                app.opacityPK2H= 100
                app.isElectricityH = False 
                app.electricityXH = 300
                app.electricityYH = 100
                app.xPK2H = 470
                app.startH = False 
                app.hpPK2H -= random.randint(10,20)



        if app.isThunderBoltH ==True:
            app.stepH+=1
            if app.stepH % 5 == 0:  # Adjust the frequency of the shake
                    shake_amountS = 10  # Adjust the shake amount
                    app.xPK1H += random.uniform(-shake_amountS, shake_amountS)
                    app.yPK1H += random.uniform(-shake_amountS, shake_amountS)
                    app.opacityPK2H = 70
                    app.startH = False 

            if app.stepH  %30 ==0:
                app.isThunderBoltH = False
                app.stepH = 0
                app.opacityPK2H =100
                app.xPK1H = 100
                app.yPK1H = 450
                app.hpPK2H -= random.randint(10,20)

        if app.turnH ==0.5:
            app.step2HH +=1
            #change 50 to 150
            if app.step2HH %100 ==0:
                app.turnH =1
                app.step2HH =0
                app.start2H = True
                # print("line 497" , app.start2H)

        # if app.turnH ==1:
        #     app.step2HH +=1
        #     #change 50 to 150
        #     if app.step2HH %100 ==0:
        #         app.turnH =1
        #         app.stepH =0
        #         app.start2H = True
                # print("line 497" , app.start2H)

        if app.turnH ==1:
            # print("this is working in line 588")
            app.turnH = 0
            skillRandom = random.randint(0,2)
            app.oppontentSkillChosenH = app.oppententPKSkillSetH[skillRandom]
            print(app.oppontentSkillChosenH)
            if app.oppontentSkillChosenH == "Scratch":
                print("Scratch is chosen for 2 ")
                app.isScratch2H = True
                app.turnH = 0

            if app.oppontentSkillChosenH == "Tackle":
                print("Tackle is chosen for 2 ")
                app.isTackle2H = True
                app.opacityPK1H = 70
                app.turnH = 0

            if app.oppontentSkillChosenH == "Bite":
                print("Bite is chosen for 2 ")
                app.isBite2H = True
                app.turnH = 0
            if app.oppontentSkillChosenH == "Growl":
                print("Dragon Breath is chosen for 2 ")
                app.isGrowl2H = True
                app.turnH = 0
        if app.isScratch2H==True:
            app.step2HH +=1 
            if app.step2HH %5 ==0:
                app.scratchX2H -= 10
                app.scratchY2H += 10
            if app.step2HH == app.stepsPerSecond * 0.5:
                app.opacityPK1H =70
            if app.step2HH > app.stepsPerSecond * 1.4:
                app.step2HH = 0
                app.opacityPK1H = 100
                app.isScratch2H = False 
                app.scratchX2H = 210
                app.scratchY2H =385
                app.start2H = False
                p.health -= random.randint(10,20)

            app.turnH = 0

        if app.isTackle2H == True:
            app.xPK2H = 250
            app.yPK2H = 415
            app.yPK1H = 440
            # app.tackleEnd = True 
            app.step2HH +=1 
            if app.step2HH ==app.stepsPerSecond:
                app.xPK2H = 440
                app.yPK2H = 100
                app.yPK1H = 450
                app.step2HH = 0 
                app.opacityPK1H = 100
                app.isTackle2H = False 
                app.start2H = False 
                # app.tackleEndH = False
                app.turnH =0
                p.health -= random.randint(10,20)

        if app.isBite2H ==True:
            app.step2HH +=1
            if app.step2HH % 5 == 0:  # Adjust the frequency of the shake
                    shake_amount = 5  # Adjust the shake amount
                    app.xPK1H += random.uniform(-shake_amount, shake_amount)
                    app.yPK1H += random.uniform(-shake_amount, shake_amount)
                    app.opacityPK1H = 70
            if app.step2HH % 5==0:
                app.biteUpY2H +=5
                app.biteDownY2H -=5
            if app.step2HH ==app.stepsPerSecond*2:
                app.isBite2H = False 
                app.xPK1H = 150
                app.yPK1H = 415
                app.biteUpX2H = 130
                app.biteUpY2H = 330
                app.biteDownY2H = 530
                app.step2HH = 0
                app.opacityPK1H = 100
                app.start2H = False 
                p.health -= random.randint(10,20)
                app.turnH = 0

        if app.isGrowl2H ==True:
            app.step2HH +=1
            if app.step2HH ==app.stepsPerSecond:
                app.isGrowl2H = False
                app.opacityPK1H =100
                app.step2HH = 0 
                app.start2H = False 
                app.turnH = 0
                p.health -= random.randint(10,20)


        # if app.isDragonBreath2S == True:
        #     app.step2HH +=1
        #     app.opacityPK1H = 70
        #     if app.step2HH % 5 == 0:  # Adjust the frequency of the shake
        #             shake_amount = 10  # Adjust the shake amount
        #             app.xPK1H += random.uniform(-shake_amount, shake_amount)
        #     if app.step2HH ==app.stepsPerSecond:
        #         app.isDragonBreath2S = False
        #         app.step2HH = 0
        #         app.opacityPK1H =100
        #         app.xPK1H = 140
        #         app.start2H = False 
        #         p.health -= random.randint(10,20)
        #         app.turnH = 0

        # if app.isWaterGun2S ==True:
        #     app.step2HH +=1
        #     app.opacityPK1H = 70
        #     if app.step2HH ==app.stepsPerSecond:
        #         app.isWaterGun2S = False 
        #         app.opacityPK1H =100
        #         app.step2HH = 0 
        #         app.start2H = False 
        #         p.health -= random.randint(10,20)
        #         app.turnH = 0

        # if app.isThunderBoltH2 == True: 
        #     app.step2HH +=1
        #     if app.step2HH % 5 == 0:  # Adjust the frequency of the shake
        #             shake_amountS = 10  # Adjust the shake amount
        #             app.xPK2H += random.uniform(-shake_amountS, shake_amountS)
        #             app.yPK2H += random.uniform(-shake_amountS, shake_amountS)
        #             app.opacityPK1H = 70
        #             # app.start2H = False
        #             # p.health -= random.randint(10,20)
        #             # app.turnH = 0 

        #     if app.step2HH  %30 ==0:
        #         app.isThunderBoltH2 = False
        #         app.step2HH = 0
        #         app.opacityPK1H =100
        #         app.xPK2H = 440
        #         app.yPK2H = 100
        #         app.turnH = 0
        #         app.start2H = False
        #         p.health  -= random.randint(10,20)

        if p.health <= 0:
            self.battleEndLoseH = True

        if app.hpPK2H <= 0:
            app.hpPK2H = 100
            self.battleEndWinH = True            
