from gamelib import*

game = Game(960,540,"Snow Hell")

#Constant Objects----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#game parts
bk = Image("BK.png",game)
Moutain = Image("Moutain.png",game)
Skier1 = Image("Skier 1.png",game)
Skier2 = Image("Skier 2.png",game)
CSkier1 = Image("Skier 1.png",game)
CSkier2 = Image("Skier 2.png",game)
CSkierL1 = Image("SkierL 1.png",game)
CSkierL2 = Image("SkierL 2.png",game)
EP1 = Image("Finish.png",game)
EP2 = Image("Finish.png",game)
EP3 = Image("Finish.png",game)
T1 = Image("T1.png",game)
Blood = Image("Blood.png",game)
Explosion = Image("Explosion.png",game)
SExplo = Image("Snow Explosion.png",game)
VTS  = Image("VTS.png",game)
WS = Image("Win Screen.png",game)
CR = Image("Copyright.png",game)
CYC = Image("CYC.png",game)
CYCB = Image("CYCB.png",game)

#Game Title Screen Parts
title = Image("Logo.png",game)
tbk = Image("Title Screen.png",game)
start = Image("Start.png",game)
startL = Image("StartL.png",game)
howtoplay = Image("howtoplay.png",game)
howtoplayL = Image("howtoplayL.png",game)
HTWS = Image("HTWS.png",game)
PEX = Image("PEX.png",game)

#Sound
Crash = Sound("Crash.wav",1)
TBlast = Sound("TNT Blast.wav",2)
SBlast = Sound("Snow Blast.wav",3)
Click = Sound("Click.wav",4)
BKM = Sound("BKM.wav",5)

#Count Variables---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

M1 = 0#Make land ramp shape for Jump variable
osx = 0#1st Parameter
osy = 0#2nd Parameter
ga = 0#Game Over Count

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Changeable and Objects Setttings------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Constant Variable
s = 8#Speed of the Obstacles - Changeable
sb = 2.5#Speed Boost of the Obstacles each passing Level - Changeable
a = 64.21709517697867#Angle - Do Not Change!!!
m = 57/118#The Slope - Do Not Change!!!

#Font - Changeable - Not Recommend to Change
f = Font(white,50,red,"Roboto Mono")
fb = Font(white,30,red,"Roboto Mono")
flf = Font(magenta,50,white,"Roboto Mono")
flfb = Font(magenta,30,white,"Roboto Mono")
lf = Font(magenta,40,white,"Roboto Mono")
fsx = 385
fsx2 = 355
fsx3 = 390
fsx4 = 283
fsy = 260
fsy2 = 340
lsx = 12
lsy = 510

#Base of Y-intercepts - Do Not Change!!!
TreeB = [-5,145,330]
RockB = [30,180,340]
T1B = [30,180,340]
VT1A = [60,199,370]

#Variables for LVL 1 - Changeable
TNA = 7 # of Trees
RNA = 7 # of Rocks
RA1 = 2000#Starting Point of the Obstacles
RA2 = 10000#Ending Point of the Obstacles
REP1 = RA2+500#X-value of the Finsh Line - Do Not Change!
bksa = 3/4#Speed of Background LVL 1 Scroll

#Variables for LVL 2 - Changeable
TNB = 10 # of Trees
RNB = 10 # of Rocks
ENB = 10 # of TNT
RB1 = 2000#Starting Point of the Obstacles
RB2 = 20000#Ending Point of the Obstacles
REP2 = RB2+500#X-value of the Finsh Line - Do Not Change!
bksb = 1#Speed of Background LVL 2 Scroll

#Variables for LVL 3 - Changeable
TNC = 13 # of Trees
RNC = 13 # of Rocks
ENC = 13 # of TNT
BNA = 7# of Blind Traps
RC1 = 2000#Starting Point of the Obstacles
RC2 = 30000#Ending Point of the Obstacles
REP3 = RC2+500#X-value of the Finsh Line - Do Not Change!
bksc = 1.25#Speed of Background LVL 3 Scroll

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Starting Screen----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

title.y -= 150
title.resizeBy(50)
start.resizeBy(-40)
startL.resizeBy(-40)
howtoplay.resizeBy(-40)
howtoplay.y += 100
howtoplayL.resizeBy(-40)
howtoplayL.y += 100
HTWS.visible = False
HTWS.resizeBy(-10)
PEX.visible = False
PEX.moveTo(760,470)
CR.resizeBy(-40)
CR.moveTo(800,520)

while not game.over:
    game.processInput()

    tbk.draw()
    title.draw()
    start.draw()
    startL.draw()  
    howtoplay.draw()
    howtoplayL.draw()
    HTWS.draw()
    PEX.draw()
    BKM.play()
    CR.draw()

    if start.collidedWith(mouse):
        startL.visible = True
    else:
        startL.visible = False
        
    if howtoplay.collidedWith(mouse):
        howtoplayL.visible = True
    else:
        howtoplayL.visible = False

    if howtoplayL.collidedWith(mouse) and mouse.LeftClick :
        Click.play()
        HTWS.visible = True
        PEX.visible = True
    if howtoplayL.collidedWith(mouse) and mouse.LeftClick :
        Click.play()
        HTWS.visible = True
        PEX.visible = True
    if PEX.collidedWith(mouse) and mouse.LeftClick:
        Click.play()
        HTWS.visible = False
        PEX.visible = False
    
    if start.collidedWith(mouse) and mouse.LeftClick:
        Click.play()
        game.over = True

    if startL.collidedWith(mouse) and mouse.LeftClick:
        Click.play()
        game.over = True
    
    game.update(60)

game.over = False

#Characters Choice--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CSkier1.resizeTo(258*0.75,278*0.75)
CSkierL1.resizeTo(258*0.75,278*0.75)
CSkier1.moveTo(320,270)
CSkier2.moveTo(640,270)
CSkierL1.moveTo(320,270)
CSkierL2.moveTo(640,270)
CYC.y -= 200
CYCB.y +=200

while not game.over:
    game.processInput()

    tbk.draw()
    CR.draw()
    CSkier1.draw()
    CSkier2.draw()
    CSkierL1.draw()
    CSkierL2.draw()
    CYC.draw()
    CYCB.draw()

    if CSkier1.collidedWith(mouse):
        CSkierL1.visible  = True
    else:
        CSkierL1.visible  = False

    if CSkier2.collidedWith(mouse):
        CSkierL2.visible  = True
    else:
        CSkierL2.visible  = False
        
    if CSkier1.collidedWith(mouse) and mouse.LeftClick:
        Skier = Skier1
        Skier.resizeBy(-20)
        Click.play()
        game.over = True

    if CSkier2.collidedWith(mouse) and mouse.LeftClick:
        Skier = Skier2
        Click.play()
        game.over = True
    
    game.update(60)

game.over = False

Skier.moveTo(950/2,270)
Skier.rotateTo(-25)
Skier.resizeBy(-45)

#Level 1 Game Loop---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Objects--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tree1 = []#empty list
for index in range(TNA):#use a loop to add items
    Tree1.append(Image("Tree.png",game))
for index in range(TNA):#use a loop to set the positions and speed
    x1 = randint(RA1,RA2)
    b1 = TreeB[randint(0,2)]
    y1 = m*x1+b1
    Tree1[index].moveTo(x1,y1)
    Tree1[index].setSpeed(s,a)
    Tree1[index].resizeBy(-60)

Rock1 = []#empty list
for index in range(RNA):#use a loop to add i6tems
    Rock1.append(Image("Rock.png",game))
for index in range(RNA):#use a loop to set the positions and speed
    x2 = randint(RA1,RA2)
    b2 = RockB[randint(0,2)]
    y2 = m*x2+b2
    Rock1[index].moveTo(x2,y2)
    Rock1[index].setSpeed(s,a)
    Rock1[index].resizeBy(-50)

xep1 = REP1
yep1 = m*xep1+90
EP1.moveTo(xep1,yep1)
EP1.setSpeed(s,a)
EP1.resizeTo(512,598)
game.setBackground(bk)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

while not game.over:
    game.processInput()
    
    game.scrollBackground("left",bksa)
    Moutain.draw()
    game.drawText("Level : 1",lsx,lsy,lf)
    Skier.draw()
    EP1.draw()
    EP1.move()

    for index in range(TNA):#the loop will go through the list of Tree
        Tree1[index].move()#each Tree will move
        if Tree1[index].collidedWith(Skier):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    for index in range(RNA):#the loop will go through the list of Tree
        Rock1[index].move()#each Tree will move
        if Rock1[index].collidedWith(Skier):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
    
    if keys.Pressed[K_RIGHT] and osy >-45:
        Skier.x +=10
        Skier.y -=5
        M1 -=5
        osx +=10
        osy -=5
    if keys.Pressed[K_LEFT] and osy <160:
        Skier.x -=10
        Skier.y +=5
        M1 +=5
        osx -=10
        osy +=5

    if EP1.isOffScreen("left"):
        game.drawText("You've Made It",fsx2,fsy,flf)
        game.drawText("Press Space to Continue to the Next Level",fsx4,fsy2,flfb)
        game.update()
        game.wait(K_SPACE)
        game.over = True
        
    CR.draw()
    
    game.update(60)

game.over = False

#Level 2 Game Loop------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Objects---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

s +=sb

Tree2 = []#empty list
for index in range(TNB):#use a loop to add items
    Tree2.append(Image("Tree.png",game))
for index in range(TNB):#use a loop to set the positions and speed
    x1 = randint(RB1,RB2)
    b1 = TreeB[randint(0,2)]
    y1 = m*x1+b1
    Tree2[index].moveTo(x1,y1)
    Tree2[index].setSpeed(s,a)
    Tree2[index].resizeBy(-60)

Rock2 = []#empty list
for index in range(RNB):#use a loop to add items
    Rock2.append(Image("Rock.png",game))
for index in range(RNB):#use a loop to set the positions and speed
    x2 = randint(RB1,RB2)
    b2 = RockB[randint(0,2)]
    y2 = m*x2+b2
    Rock2[index].moveTo(x2,y2)
    Rock2[index].setSpeed(s,a)
    Rock2[index].resizeBy(-50)

T1 = []#empty list
for index in range(ENB):#use a loop to add items
    T1.append(Image("T1.png",game))
for index in range(ENB):#use a loop to set the positions and speed
    x3 = randint(RB1,RB2)
    b3 = T1B[randint(0,2)]
    y3 = m*x3+b3
    T1[index].moveTo(x3,y3)
    T1[index].setSpeed(s,a)
    T1[index].resizeBy(-75)

xep2 = REP2
yep2 = m*xep2+90
EP2.moveTo(xep2,yep2)
EP2.setSpeed(s,a)
EP2.resizeTo(512,598)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while not game.over:
    game.processInput()
    
    game.scrollBackground("left",bksb)
    Moutain.draw()
    game.drawText("Level : 2",lsx,lsy,lf)
    Skier.draw()
    EP2.draw()
    EP2.move()

    for index in range(TNB):#the loop will go through the list of Tree
        Tree2[index].move()#each Tree will move
        if Tree2[index].collidedWith(Skier):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    for index in range(RNB):#the loop will go through the list of Tree
        Rock2[index].move()#each Tree will move
        if Rock2[index].collidedWith(Skier):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    for index in range(ENB):#the loop will go through the list of Tree
        T1[index].move()#each Tree will move
        if T1[index].collidedWith(Skier):
            TBlast.play()
            Explosion.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True

    if keys.Pressed[K_RIGHT] and osy >-45:
        Skier.x +=10
        Skier.y -=5
        M1 -=5
        osx +=10
        osy -=5
        
    if keys.Pressed[K_LEFT] and osy <160:
        Skier.x -=10
        Skier.y +=5
        M1 +=5
        osx -=10
        osy +=5

    if ga >0:
        game.over = True
        
    if EP2.isOffScreen("left"):
        game.drawText("You've Made It",fsx2,fsy,flf)
        game.drawText("Press Space to Continue to the Next Level",fsx4,fsy2,flfb) 
        game.update()
        game.wait(K_SPACE)
        game.over = True
        
    CR.draw()
    
    game.update(60)

game.over = False

#Level 3 Game Loop-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Objects--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

s +=sb

Tree3 = []#empty list
for index in range(TNC):#use a loop to add items
    Tree3.append(Image("Tree.png",game))
for index in range(TNC):#use a loop to set the positions and speed
    x1 = randint(RB1,RB2)
    b1 = TreeB[randint(0,2)]
    y1 = m*x1+b1
    Tree3[index].moveTo(x1,y1)
    Tree3[index].setSpeed(s,a)
    Tree3[index].resizeBy(-60)

Rock3 = []#empty list
for index in range(RNC):#use a loop to add items
    Rock3.append(Image("Rock.png",game))
for index in range(RNC):#use a loop to set the positions and speed
    x2 = randint(RB1,RB2)
    b2 = RockB[randint(0,2)]
    y2 = m*x2+b2
    Rock3[index].moveTo(x2,y2)
    Rock3[index].setSpeed(s,a)
    Rock3[index].resizeBy(-50)

T2 = []#empty list
for index in range(ENC):#use a loop to add items
    T2.append(Image("T1.png",game))
for index in range(ENC):#use a loop to set the positions and speed
    x3 = randint(RB1,RB2)
    b3 = T1B[randint(0,2)]
    y3 = m*x3+b3
    T2[index].moveTo(x3,y3)
    T2[index].setSpeed(s,a)
    T2[index].resizeBy(-75)

VT1 = []#empty list
for index in range(BNA):#use a loop to add items
    VT1.append(Image("VT1.png",game))
for index in range(BNA):#use a loop to set the positions and speed
    x4 = randint(RB1,RB2)
    b4 = VT1A[randint(0,2)]
    y4 = m*x4+b4
    VT1[index].moveTo(x4,y4)
    VT1[index].setSpeed(s,a)
    VT1[index].resizeBy(-40)

xep2 = REP2
yep2 = m*xep2+90
EP2.moveTo(xep2,yep2)
EP2.setSpeed(s,a)
EP2.resizeTo(512,598)
VTS.moveTo(2000,2000)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while not game.over:
    game.processInput()
    
    game.scrollBackground("left",bksc)
    Moutain.draw()
    game.drawText("Level : 3",lsx,lsy,lf)
    Skier.draw()
    EP2.draw()
    EP2.move()

    for index in range(TNC):#the loop will go through the list of Tree
        Tree3[index].move()#each Tree will move
        if Tree3[index].collidedWith(Skier):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    for index in range(RNC):#the loop will go through the list of Tree
        Rock3[index].move()#each Tree will move
        if Rock3[index].collidedWith(Skier):
            Crash.play()
            Blood.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
            
    for index in range(ENC):#the loop will go through the list of Tree
        T2[index].move()#each Tree will move
        if T2[index].collidedWith(Skier):
            TBlast.play()
            Explosion.draw()
            game.drawText("You've Died",fsx,fsy,f)
            game.drawText("Press Space to Exit",fsx3,fsy2,fb)
            game.update()
            game.wait(K_SPACE)
            ga+=1
            game.over = True
    
    for index in range(BNA):
        VT1[index].move()
        if VT1[index].collidedWith(Skier):
            SBlast.play()
            SExplo.visible = True
            SExplo.draw()
            VTS.moveTo(940/2,540/2)
            VTS.setSpeed(0,0)
            game.time=3
    
    VTS.draw()
    
    if game.time<1:
        VTS.setSpeed(5,180)
        VTS.move()
        SExplo.visible = False
        
    if keys.Pressed[K_RIGHT] and osy >-45:
        Skier.x +=10
        Skier.y -=5
        M1 -=5
        osx +=10
        osy -=5
        
    if keys.Pressed[K_LEFT] and osy <160:
        Skier.x -=10
        Skier.y +=5
        M1 +=5
        osx -=10
        osy +=5

    if ga >0:
        game.over = True
    
    if EP2.isOffScreen("left"):
        WS.draw()
        game.update()
        game.wait(K_SPACE)
        game.over = True

    CR.draw()
    
    game.update(60)

game.over = False

game.quit() 

