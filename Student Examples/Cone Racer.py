### Author: Jamie Dawson
### Date: Spring 2024

from cmu_graphics import *

app.background=gradient('moccasin','coral','coral', 'gold','lightSalmon' ,'tomato', start='bottom')
app.counter = 0
app.play = False
app.gameover = False
scoreLabel = Label(0,75,36, fill='white', size=18, bold=True)
Label('Score: ', 40, 35, fill='white', size=18, bold=True)


#Track
Rect(0,140, 400 ,310, fill='grey'),
Rect(0, 175, 400, 185, fill=rgb(47, 48, 53)),
topTrack=Group(
    Polygon(0, 175, 25, 175, 25, 180, 0, 180, fill='crimson'),
    Polygon(25, 175, 60, 175, 57, 180, 25, 180, fill='white'),
    Polygon(60, 175, 100, 175, 100, 180, 57, 180, fill='crimson'),
    Polygon(100, 175, 140, 175, 145, 180, 100, 180, fill='white'),
    Polygon(140, 175, 180, 175, 185, 180, 145, 180, fill='crimson'),
    Polygon(180, 175, 220, 175, 220, 180, 185, 180, fill='white'),
    Polygon(220, 175, 257, 175, 257, 180, 220, 180, fill='crimson'),
    Polygon(257, 175, 295, 175, 295, 180, 257, 180, fill='white'),
    Polygon(295, 175, 335, 175, 335, 180, 295, 180, fill='crimson'),
    Polygon(335, 175, 370, 175, 370, 180, 335, 180, fill='white'),
    Polygon(370, 175, 400, 175, 400, 180, 370, 180, fill='crimson'),
    
    Polygon(400, 175, 425, 175, 425, 180, 400, 180, fill='white'),
    Polygon(425, 175, 460, 175, 457, 180, 425, 180, fill='crimson'),
    Polygon(457, 180, 460, 175, 500, 175, 500, 180, fill='white'),
    Polygon(500, 180, 500, 175, 545, 175, 540, 180, fill='crimson'),
    Polygon(540, 180, 545, 175, 585, 175, 580, 180, fill='white'),
    Polygon(580, 180, 585, 175, 620, 175, 623, 180, fill='crimson'),
    Polygon(623, 180, 620, 175, 657, 175, 663, 180, fill='white'),
    Polygon(663, 180, 657, 175, 695, 175, 705, 180, fill='crimson'),
    Polygon(705, 180, 695, 175, 735, 175, 745, 180, fill='white'),
    Polygon(745, 180, 735, 175, 770, 175, 785, 180, fill='crimson'),
    Polygon(785, 180, 770, 175, 800, 175, 800, 180, fill='white'))
    
bottomTrack=Group(
    Polygon(0, 350, 0, 360, 40, 360, 55, 350, fill='crimson'),
    Polygon(40, 360, 55, 350, 115, 350, 105, 360, fill='white'),
    Polygon(105, 360, 115, 350, 173, 350, 170, 360, fill='crimson'),
    Polygon(170, 360, 173, 350, 230, 350, 235, 360, fill='white'),
    Polygon(235, 360, 230, 350, 290, 350, 293, 360, fill='crimson'),
    Polygon(293, 360, 290, 350, 345, 350, 360, 360, fill='white'),
    Polygon(360, 360, 345, 350, 400, 350, 400, 360, fill='crimson'),
    Polygon(400, 350, 400, 360, 440, 360, 455, 350, fill='white'),
    Polygon(440, 360, 455, 350, 515, 350, 505, 360, fill='crimson'),
    Polygon(505, 360, 515, 350, 573, 350, 570, 360, fill='white'),
    Polygon(570, 360, 573, 350, 630, 350, 635, 360, fill='crimson'),
    Polygon(635, 360, 630, 350, 690, 350, 693, 360, fill='white'),
    Polygon(693, 360, 690, 350, 745, 350, 760, 360, fill='crimson'),
    Polygon(760, 360, 745, 350, 800, 350, 800, 360, fill='white'))
    
#Middle road line group#
roadLines=Group()
roadLines.add(Line(50, 250, 110, 250, fill='White', lineWidth=5))
roadLines.add(Line(175, 250, 235, 250, fill='white', lineWidth=5))
roadLines.add(Line(300, 250, 360, 250, fill='white', lineWidth=5))
roadLines.add(Line(425, 250, 485, 250, fill='white', lineWidth=5))

def centerLineManager():
    for line in roadLines:
        if line.x2<0:
            greatestX=0
            for line2 in roadLines:
                if line2.x2>greatestX:
                    greatestX=line2.x2
            line.x1=greatestX+65
            line.x2=greatestX+125
            
##Racecars##
def buildCar(color,ratio):
    racecar=Group(
        Polygon(27, 255, 27, 265, 40, 265, 40, 255, fill='darkGrey'),
        Circle(120, 230, 15, fill='darkRed'),
        Polygon(135, 225, 125, 224, 123, 228, 128, 230, 135, 231, fill='lightBlue'),
        Polygon(20, 212, 50, 212, 50, 225, 45, 230, 45, 250, 30, 250, 20, 245, 
        fill=color),
        Polygon(55,238,95,215,105,212,115,212,115,230,48,250,fill=color),
        Polygon(55, 265, 140, 265, 160, 260, 185, 250, 225, 248, 230, 255, 223, 255, 
        223, 265, 258, 265, 255, 255, 245, 255, 242, 250, 253, 250, 245, 243, 245,  
        243, 230, 240, 215, 235, fill=color),
        Polygon(215, 235, 225, 248, 190, 235, 165, 235, 165, 233, 168, 233, 168, 230,
        158, 230, 158, 233, 160, 233, 160, 235, fill=color),
        Polygon(115,230,120,230,55,238,55,265,140,265,140,235,fill=color),
        Polygon(140, 235, 190, 235, 185, 250, 55, 265, fill=color),
        Polygon(190, 235, 185, 250, 225, 248, fill=color),
        Polygon(140, 265, 140, 260, 155, 255, 163, 255, 163, 265, fill='darkGrey'),
        Polygon(20, 212, 50, 212, 50, 225, 20, 225, fill='silver'),
        Rect(25, 215, 20, 8, fill=color),
        Circle(48, 250, 20, fill='black'),
        Circle(48, 250, 14, fill='white'),
        Circle(48, 250, 10, fill='grey'),
        Circle(48, 250, 4, fill='darkKhaki'),
        Circle(200, 250, 20, fill='black'),
        Circle(200, 250, 14, fill='white'),
        Circle(200, 250, 10, fill='grey'),
        Circle(200, 250, 4, fill='darkKhaki'))
    racecar.height/=ratio
    racecar.width/=ratio
    return racecar

car = buildCar('mediumBlue',1.5)
car.centerX-=20
car.centerY-=20
    
##OBSTICALES##
def newCone():
    cone = Group(Rect(418,218,19,10),
        Polygon(420,223,428,200,435,223,fill='orangeRed')
        )
    coneY=randrange(195,300)
    cone.centerY = coneY
    return cone

cones=Group(
    )
cones.add(newCone())
    
def coneManager():
    for cone in cones.children:
        if cone.left < 0-60:
            cones.remove(cone)
            cones.add(newCone())
    
##Moving Objects##
app.stepsPerSecond=9
def onStep():
    if app.play == True:
        app.counter += 1
        topTrack.centerX-=40
        bottomTrack.centerX-=40
        roadLines.centerX-=40   
        centerLineManager()
        cones.centerX-=50
        coneManager()
        
        if topTrack.centerX < 0:
            topTrack.centerX = 400
        if bottomTrack.centerX < 0:
            bottomTrack.centerX = 400
        
        if app.counter % 9 == 0:
            scoreLabel.value += 1
       
        if app.counter % 90 == 0:
            app.stepsPerSecond += 2
        for cone in cones.children:
            if car.hitsShape(cone):
                gameOverText.visible=True
                
        if gameOverText.visible==True:
            app.play = False
            app.gameover = True
            cones.clear()  
            


gameOverText = Group(
    Rect(200, 200, 300, 125, fill='aliceBlue', opacity=75, align='center'),
    Label('Game Over', 200, 175, fill='orangeRed', size=48, bold=True),
    Label('Press space to restart', 200, 225, fill='orangeRed', size=20)
    )
gameOverText.visible=False

def newGame():
    gameOverText.visible = False
    scoreLabel.value = 0

def onKeyPress(key):
    # When the game is over, starts the game again.
    if key == 'space':
        app.play = True
        newGame() 
        if app.gameover == True:
            app.gameover = False
            cones.add(newCone())

 
def onKeyHold(keys):
    if car.centerY>=180:
        if 'up' in keys:
            car.centerY-=15
        
    if car.bottom<=345:
         if 'down' in keys:
            car.centerY+=15
            
            




cmu_graphics.run()