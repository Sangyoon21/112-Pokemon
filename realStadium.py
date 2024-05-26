from cmu_graphics import*

def onAppStart(app):
    app.ashBack = "ashBack2.png"
    app.brock = "brock.png"
    app.floor = "stadium_floor.png"
    app.stadiumBackGround = "stadiumBackGround.png"
    firstColor = rgb(110,213,192)
    secondColor = rgb(134,210,116)
    app.size = 80
    app.gradientColor = gradient(firstColor,secondColor,start = "top")
    app.background = app.gradientColor
    app.talk = 0
    app.choice = None # fight 


def redrawAll(app):
    drawImage(app.brock,app.size * 4,app.size * 0,width = app.size*2, height = app.size*2.5)
    drawImage(app.floor,app.size*4,app.size * 2.5,width = app.size *2, height = app.size*2)
    drawImage(app.ashBack,app.size*4,app.size*4.5,width = app.size *3, height = app.size*3)
    hpInnerBox = rgb(193,193,193)
    drawRect(100,600,600,180,fill = "gray",border = hpInnerBox,borderWidth = 5)
    if app.talk ==0:
        drawLabel("Brock: You Finally Came!!!!",400,670,size =25)
        drawLabel("Press space to continue",400,730,size = 15, fill = "white")

    if app.talk ==1:
        drawLabel("Brock: Do you want a to fight??!!",400,670,size =25)
        drawLabel("Press space to continue",400,730,size = 15, fill = "white")

    if app.talk ==2:
        drawLabel("Choose the option by typing the number",400,670,size =25)
        drawLabel("1. Fight      2. Run",400,730,size =25)

    if app.talk ==3 and app.choice ==0:
        drawLabel("Brock: Good!! Let's fight!!",400,670,size =25)
        drawLabel("Press space to continue",400,730,size = 15, fill = "white")
        #fighting scence comes in !! 

    if app.talk ==3 and app.choice ==1:
        drawLabel("Brock: Are you scared??",400,650,size =25)
        drawLabel("Be Bravce young player! I will ask you one last time",400,690,size =25)
        drawLabel("Press space to continue",400,730,size = 15, fill = "white")

    if app.talk ==4 and app.choice ==1:
        drawLabel("Choose the option by typing the number",400,670,size =25)
        drawLabel("1. Fight      2. Run",400,730,size =25)
    

    if app.talk ==5 and app.choice ==0:
        drawLabel("Brock: Good!! Let's fight!!",400,670,size =25)
        drawLabel("Press space to continue",400,730,size = 15, fill = "white")


    if app.talk ==5 and app.choice ==1:
        drawLabel("Brock: Okay Good Bye! See you again soon",400,670,size =25)
        drawLabel("Press space to continue",400,730,size = 15, fill = "white")
       

def onKeyPress(app,key):
    if app.talk ==0 and key == "space":
        app.talk =1

    if app.talk ==1 and key == "space":
        app.talk =2

    if app.talk==2 and key == "1":
        app.talk = 3 
        app.choice = 0 # fight 

    if app.talk==2 and key == "2":
        app.talk = 3 
        app.choice = 1 # Run

    if app.talk ==3 and app.choice == 0:
        print("this is the end")
        # here this part ends like add code that ends the game 
        pass

    if app.talk ==3 and app.choice ==1 and key == "space":
        app.talk =4

    if app.talk ==4 and app.choice == 1 and key == "1":
        app.talk = 5
        app.choice = 0

    if app.talk ==4 and app.choice == 1 and key == "2":
        app.talk = 5
        app.choice = 1

    if app.talk ==5 and app.choice == 0 and key == "space":
        print("this is another end ")
        # at this part we end again too --> go the fight scence  
        pass 
     
    




runApp(800,800)


