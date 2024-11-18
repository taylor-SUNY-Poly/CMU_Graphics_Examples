### Author: Mason Crain
### Date: Spring 2024

from cmu_graphics import *

# Background
app.background = 'black'

# Group for the player
player = Group(
    Line(200, 202, 200, 180, arrowEnd=True, fill='red',lineWidth=.6),
    Polygon(194.5, 188.5, 205, 189, 215, 202.5, 185, 202.5, fill=gradient('red',
        'White',start='top'),borderWidth = 2, border='Silver'),
    Polygon(211,196,211,190,213,188,215,190,215,201, fill = 'skyBlue',
        borderWidth = .6, border='red'),
    Polygon(189,196,189,190,187,188,185,190,185,201, fill = 'skyBlue',
        borderWidth = .6, border='red'),
    Circle(200,196,6,fill= gradient('skyBlue','skyBlue','red','skyBlue',
        'skyBlue','black'))
    )

# Groups of different stage #'s
StageOne = Group(
    Label('Stage #1',200,375,size=20,fill='red',borderWidth=1,border='white',
        bold=True)
    )
    
StageTwo = Group(
    Label('Stage #2',200,375,size=20,fill='green',borderWidth=1,border='white',
        bold=True)
    )
    
StageThree = Group(
    Label('Stage #3',200,375,size=20,fill='yellow',borderWidth=1,border='white',
        bold=True)
    )
    
StageFour = Group(
    Label('Stage #4',200,375,size=20,fill='purple',borderWidth=1,border='white',
        bold=True)
    )

BossStage = Group(
    Label('Boss Stage',200,375,size=25,fill=None,borderWidth=2,border='white',
        bold=True)
    )
    
# Setting Stage Title Visibilities as False
StageTwo.visible = False

StageThree.visible = False

StageFour.visible = False

BossStage.visible = False

# Making the Health bar and the art around the HP bar
healthBar = Group(
    Rect(0,10,200,15,fill='crimson')
    ) 
    
Rect(0,10,200,15,fill=None,border='silver')
Label('Health',25,17.5,bold = True)

# Making a counter to track the number of Enemies Killed
Label('Enemies Killed:', 340, 20, align='right', fill='White', bold = True)
numberKilled = Label(0, 350, 20, align='left', fill='White', bold = True)

# A seperate counter for time that's out of view, It's used for spwaning enemies
counter = Label(0, 350, -10)

# Making the player spin to follow the mouse
def onMouseMove(x, y):
    player.rotateAngle = angleTo(player.centerX, player.centerY, x, y)

# Making a bullet spawn with every mouse press
def onMousePress(x,y):
    spawnBullet(player.centerX, player.centerY)

# Making bullets into a group and spawning them in 
# Then making their angle the players angle
bullets = Group()

def spawnBullet(x, y):
    bullet = Circle(x, y, 4, fill= gradient('red','red','lightBlue','lightBlue',
        'lightBlue'))
    bullet.Angle = player.rotateAngle
    bullets.add(bullet)

# Making the 1st kind of enemies into a group
enemys = Group()

def spawnEnemy(x, y):
    enemy = Circle(x,y,10,fill='red',border='white',borderWidth=2)
    enemys.add(enemy)
    
# Making the 2nd kind of enemies into a group 
enemysGreen = Group()
    
def spawnEnemyGreen(x, y):
    enemyGreen = Circle(x,y,10,fill='Green',border='white',borderWidth=2)
    enemysGreen.add(enemyGreen)

# Making the 3rd kind of enemies into a group
enemysYellow = Group()
    
def spawnEnemyYellow(x, y):
    enemyYellow = Star(x,y,13,10,fill='Yellow',border='white',borderWidth=1)
    enemysYellow.add(enemyYellow)

# Making the 4th kind of enemies into a group
enemysPurple = Group()
    
def spawnEnemyPurple(x, y):
    enemyPurple = Star(x,y,13,10,fill='Purple',border='white',borderWidth=1)
    enemysPurple.add(enemyPurple)
    
# Making the Final Boss and putting him offscreen so it's like he isn't there
finalBoss = Star(450,200,30,100,fill=None,border='white',borderWidth=2)

# Making the place that 1st enemy spawns in be random/depending of # of kills    
def onStep():
    enemyX = randrange(0,400)
    if (numberKilled.value % 2 == 0): 
        enemyY = randrange(-5,0) 
    else:
        enemyY = randrange(400,405)

# Making the place that 2nd enemy spawns in be random/depending of # of kills    
    enemyGreenY = randrange(0,400)
    if (numberKilled.value % 2 == 0): 
        enemyGreenX = randrange(-5,0) 
    else:
        enemyGreenX = randrange(400,405)
    
# Making the place that 3rd enemy spawns in be random/depending of # of kills
    enemyYellowX = randrange(0,400)
    if (numberKilled.value % 2 == 0): 
        enemyYellowY = randrange(-5,0) 
    else:
        enemyYellowY = randrange(400,405)
        
# Making the place that 4th enemy spawns in be random/depending of # of kills
    enemyPurpleY = randrange(0,400)
    if (numberKilled.value % 2 == 0): 
        enemyPurpleX = randrange(-5,0) 
    else:
        enemyPurpleX = randrange(400,405)

# Making it so the player can't leave the area
    if (player.right > 400):
        player.right = 400
    elif (player.left < 0):
        player.left = 0
    elif (player.top < 0):
        player.top = 0
    elif (player.bottom > 400):
        player.bottom = 400

# Making the bullets movement
    for bullet in bullets.children:
        newX,newY = getPointInDir(bullet.centerX, bullet.centerY, bullet.Angle, 
            10)
        bullet.centerX = newX
        bullet.centerY = newY

# Making it so the time counter always goes up
    counter.value += 1

# Putting when and how often the 1st enemy spawns
    if (counter.value % 50 == 0):
        spawnEnemy(enemyX,enemyY)

# Putting when the 2nd wave starts and how often the and 2nd enemy spawns
    if numberKilled.value >= 15 and numberKilled.value <= 100:
        app.background = gradient('darkSlateGray','black','black',start=
            'top-right')
        StageTwo.visible = True
        StageOne.visible = False
        if (counter.value % 105 == 0):
            spawnEnemyGreen(enemyGreenX,enemyGreenY)

# Putting when the 3rd wave starts and how often the and 3rd enemy spawns
    if numberKilled.value >= 35 and numberKilled.value <= 100:
        app.background = gradient(rgb(0,85,85),'black','black','black',start=
            'left')
        StageThree.visible = True
        StageTwo.visible = False
        if (counter.value % 75 == 0):
            spawnEnemyYellow(enemyYellowX,enemyYellowY)

# Putting when the 4th wave starts and how often the and 4th enemy spawns
    if numberKilled.value >= 70 and numberKilled.value <= 100:
        app.background = gradient('black',rgb(60, 50, 0),'black','black',start=
            'bottom-right')
        StageFour.visible = True
        StageThree.visible = False
        if (counter.value % 120 == 0):
            spawnEnemyPurple(enemyPurpleX,enemyPurpleY)

# Starting the Boss Stage at >=100 kills and giving the boss movement
    if numberKilled.value >= 100:
        app.background = gradient(rgb(60,0,45),'black','black')
        BossStage.visible = True
        StageFour.visible = False
        if (player.centerY >= finalBoss.centerY):
            finalBoss.centerY += 3
        if (player.centerY < finalBoss.centerY):
            finalBoss.centerY -= 3
        if (player.centerX >= finalBoss.centerX):
            finalBoss.centerX += 3
        if (player.centerX < finalBoss.centerX):
            finalBoss.centerX -= 3
    
# Making the interaction between the bullets, 1st enemy type and kill count
    for bullet in bullets.children:
        for enemy in enemys.children:
            if (bullet.hitsShape(enemy) == True):
                bullets.remove(bullet)
                numberKilled.value += 1
                enemys.remove(enemy)
    
# Making 1st enemy move the healthbar over 50 to hurt the player if they touch
    for enemy in enemys.children:
            if (player.hitsShape(enemy) == True):
                healthBar.centerX -= 50
                enemys.remove(enemy)
                
# Making the interaction between the bullets, 2nd enemy type and kill count
    for bullet in bullets.children:
        for enemyGreen in enemysGreen.children:
            if (bullet.hitsShape(enemyGreen) == True):
                bullets.remove(bullet)
                numberKilled.value += 1
                enemysGreen.remove(enemyGreen)

# Making 2nd enemy move the healthbar over 50 to hurt the player if they touch
    for enemyGreen in enemysGreen.children:
            if (player.hitsShape(enemyGreen) == True):
                healthBar.centerX -= 50
                enemysGreen.remove(enemyGreen)
                
# Making the interaction between the bullets, 3rd enemy type and kill count
    for bullet in bullets.children:
        for enemyYellow in enemysYellow.children:
            if (bullet.hitsShape(enemyYellow) == True):
                if enemyYellow.points == 10:
                    enemyYellow.points -= 5
                    bullets.remove(bullet)
                # Making the bullets not kill it instantly to show more HP
                elif enemyYellow.points == 5:
                    numberKilled.value += 1
                    bullets.remove(bullet)
                    enemysYellow.remove(enemyYellow)

# Making 3rd enemy move the healthbar over 100 to hurt the player if they touch
    for enemyYellow in enemysYellow.children:
            if (player.hitsShape(enemyYellow) == True):
                healthBar.centerX -= 100
                enemysYellow.remove(enemyYellow)

# Making the interaction between the bullets, 3rd enemy type and kill count
    for bullet in bullets.children:
        for enemyPurple in enemysPurple.children:
            if (bullet.hitsShape(enemyPurple) == True):
                if enemyPurple.points == 10:
                    enemyPurple.points -= 3
                    bullets.remove(bullet)
                elif enemyPurple.points == 7:
                    enemyPurple.points -= 3
                    bullets.remove(bullet)
                # Making the bullets not kill it instantly to show more HP
                elif enemyPurple.points == 4:
                    numberKilled.value += 1
                    bullets.remove(bullet)
                    enemysPurple.remove(enemyPurple)

# Making 4th enemy move the healthbar over 100 to hurt the player if they touch
    for enemyPurple in enemysPurple.children:
            if (player.hitsShape(enemyPurple) == True):
                healthBar.centerX -= 100
                enemysPurple.remove(enemyPurple)

# Making the interaction between the bullets and the boss
    for bullet in bullets.children:
            if (bullet.hitsShape(finalBoss) == True):
                finalBoss.points -= 1
                bullets.remove(bullet)
                if finalBoss.points <= 3:
                    finalBoss.centerX = 10000000
                    finalBoss.centerX -= 20
                    player.centerX = 1000000000
                    winScreen.visible = True
    
# Making boss move the healthbar over to trigger a lose if they touch player
    if (player.hitsShape(finalBoss) == True):
        healthBar.centerX -= 200

# Making the bullets be removed if they leave the area
    for bullet in bullets.children:
        if bullet.centerX <= 0:
            bullets.remove(bullet)
        if bullet.centerX >= 400:
            bullets.remove(bullet)
        if bullet.centerY >= 400:
            bullets.remove(bullet)
        if bullet.centerY <= 0:
            bullets.remove(bullet)

# Making the health bar being 0 causing the lose screen
    if healthBar.centerX <= -99:
        loseScreen.visible = True
        player.centerX = 1000000000
    
# Making the movement for the 1st enemy
    for enemy in enemys.children:
        if (player.centerY >= enemy.centerY):
            enemy.centerY += 1
        if (player.centerY < enemy.centerY):
            enemy.centerY -= 1
        if (player.centerX >= enemy.centerX):
            enemy.centerX += 1
        if (player.centerX < enemy.centerX):
            enemy.centerX -= 1
         
# Making the movement for the 2nd enemy   
    for enemyGreen in enemysGreen.children:
        if (player.centerY >= enemyGreen.centerY):
            enemyGreen.centerY += 3
        if (player.centerY < enemyGreen.centerY):
            enemyGreen.centerY -= 3
        if (player.centerX >= enemyGreen.centerX):
            enemyGreen.centerX += 3
        if (player.centerX < enemyGreen.centerX):
            enemyGreen.centerX -= 3
        
# Making the movement for the 3rd enemy
    for enemyYellow in enemysYellow.children:
        if (player.centerY >= enemyYellow.centerY):
            enemyYellow.centerY += 2
        if (player.centerY < enemyYellow.centerY):
            enemyYellow.centerY -= 2
        if (player.centerX >= enemyYellow.centerX):
            enemyYellow.centerX += 2
        if (player.centerX < enemyYellow.centerX):
            enemyYellow.centerX -= 2

# Making the movement for the 4th enemy
    for enemyPurple in enemysPurple.children:
        if (player.centerY >= enemyPurple.centerY):
            enemyPurple.centerY += 3.5
        if (player.centerY < enemyPurple.centerY):
            enemyPurple.centerY -= 3.5
        if (player.centerX >= enemyPurple.centerX):
            enemyPurple.centerX += 3.5
        if (player.centerX < enemyPurple.centerX):
            enemyPurple.centerX -= 3.5

# Making the movement for the player
def onKeyHold(keys):
    if ('w' in keys):
        player.centerY -= 5
    if ('a' in keys):
        player.centerX -= 5 
    if ('s' in keys):
        player.centerY += 5
    if ('d' in keys):
        player.centerX += 5

# Making the lose screen and making it invisible so it's not seen until needed
loseScreen = Group(
    Rect(0,0,400,400,fill=gradient('red','black','red','black','red',start=
        'top-left')),
    Label('You Lose!',200,150,size=80,fill='white'),
    Label('click "run" to try again',200,300,size=30,fill='white')
    )
loseScreen.visible = False

# Making the win screen and making it invisible so it's not seen until needed
winScreen = Group(
    Rect(0,0,400,400,fill=gradient('silver','gold','white','gold','silver',
        start='top-left')),
    Label('You Win!!',200,150,size=80,fill='black'),
    Label('Please give us an A+!  X3',200,300,size=30,fill='black', bold=True)
    )
winScreen.visible = False



cmu_graphics.run()