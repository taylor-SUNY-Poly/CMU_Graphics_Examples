from cmu_graphics import *
'''Pong by Mr. Taylor'''

### global variables that hold state of critical application properties
app.stepsPerSecond=1000
app.ballMoving = False
app.gameOver = False
app.modeSelected = 0
app.counter = 0
app.counterDelay = 0
app.time = 0
app.ballStartSpeed = 1000 / app.stepsPerSecond
app.ballSpeedMultiplier = 1.1
app.paddleSpeed = app.stepsPerSecond * 1.2 / app.stepsPerSecond
app.background = "seaGreen"
app.objectColor = "whiteSmoke"

bumpSound = Sound("https://codeskulptor-demos.commondatastorage.googleapis.com/pang/pop.mp3")

### player1 and player2 paddles
player = Line(32,200,32,275, lineWidth=16,fill=app.objectColor)
player2 = Line(368,200,368,275, lineWidth=16,fill=app.objectColor)
player2.nextRotation = 0  ### used for cpu mode, random tilt angles go here
player2.cooldown = 0    ### used for cpu mode, ensures no wonky activiy

### socre boards
playerScore = Label(0,50,30,size=30,fill=app.objectColor)
player2Score = Label(0,350,30,size=30,fill=app.objectColor)
displayTime = Label(app.time,200,30, size=30,fill=app.objectColor)

gameOverScreen = Rect(2,2,394,394,opacity=80,visible=False,fill=app.objectColor)
gameOverMessage = Label('-',200,200,size=60,visible=False,fill=app.objectColor)

### boundary set up
topBoundary = Line(200,-198,200,202,lineWidth=8,rotateAngle = 90,fill=app.objectColor)
bottomBoundary = Line(200,200,200,596,lineWidth=8, rotateAngle = 90,fill=app.objectColor)

leftTopBoundary = Line(4,0,4,50,lineWidth=8,fill=app.objectColor)
leftBottomBoundary = Line(4,350,4,400,lineWidth=8,fill=app.objectColor)

rightTopBoundary = Line(396,0,396,50,lineWidth=8,fill=app.objectColor)
rightBottomBoundary = Line(396,350,396,400,lineWidth=8,fill=app.objectColor)
gameObjects = Group(player, player2, topBoundary, bottomBoundary, leftTopBoundary,
                    leftBottomBoundary, rightTopBoundary, rightBottomBoundary)

### start messages
gameOptions1 = Label ('Press "1" to play against CPU',200,100,size=25,fill=app.objectColor)
gameOptions2 = Label('Press "2" to play with a friend',200,140,size=25,fill=app.objectColor)
startMessage = Label('Press "SPACE" to start',200,100,size=30,visible=False,fill=app.objectColor)

### ideas for future features
# app.powerUpType = choice(['extraWide', 'extraOffender','smallOpponent'])
# app.powerUpTime = randrange(8,20)

### each object has a unique ID so that ID can be checked and double hits avoided
id = 0
for object in gameObjects:
    object.id = id
    id +=1

### set-up for game ball
ball = Circle(200,200,6,fill=app.objectColor,border="black")
ball.speed = app.ballStartSpeed
ball.angle = choice([randrange(50,130),randrange(220,310)])
ball.lastInteraction = None

app.counter = 0
app.ballMoving = False


def advanceBall():
    ball.oldX, ball.oldY = ball.centerX, ball.centerY 
    ball.centerX, ball.centerY = getPointInDir(ball.centerX,ball.centerY,ball.angle,ball.speed)
    for gameObject in gameObjects:
        if gameObject.hitsShape(ball):
            handleBounce(gameObject)
            if gameObject == player2:
                player2.nextRotation = randrange(-45,46)
                player2.cooldown = 100
            

def handleBounce(hitObject):
    bumpSound.play()
    if hitObject.id != ball.lastInteraction:
        inAng = angleTo(ball.oldX, ball.oldY, ball.centerX, ball.centerY)
        ball.angle = getBounceAngle(inAng, hitObject.rotateAngle)
        ball.lastInteraction = hitObject.id
    

def getBounceAngle(inAngle, surfaceRotation):
    outAng = (360 - (180 - 2 * ( 90 - (inAngle-180) ) ) /2)
    outAng = outAng + 2*(90 + (surfaceRotation) % 180)
    return outAng % 360


def resetBall():
    ball.centerX = 200
    ball.centerY = 200
    ball.speed = app.ballStartSpeed
    ball.angle = choice([randrange(50,130),randrange(220,310)])
    app.counter = 0
    app.ballMoving = False
    ball.lastInteraction = None
    startMessage.visible = True


def handleplayer2Movement():
    if ball.centerY - player2.centerY > 30 and player2.bottom < 360:
        player2.centerY += app.paddleSpeed
    elif ball.centerY - player2.centerY < -30 and player2.top > 40:
        player2.centerY -= app.paddleSpeed
    
    dist = distance(player2.centerX,player2.centerY,ball.centerX,ball.centerY)
    if dist < 100 and player2.cooldown == 0:
        if player2.nextRotation < player2.rotateAngle:
            player2.rotateAngle -= 1
        elif player2.nextRotation > player2.rotateAngle:
            player2.rotateAngle += 1
    else:
        if player2.rotateAngle > 0:
            player2.rotateAngle -= 1
        elif player2.rotateAngle < 0:
            player2.rotateAngle += 1
    if player2.cooldown > 0:
        player2.cooldown -= 1
    

def checkGameStatus():
    if ball.centerX >= 400:
        playerScore.value += 1 
        resetBall()
    elif ball.centerX <= 0:
        player2Score.value += 1
        resetBall()
    if playerScore.value == 3 or player2Score.value == 3:
        app.gameOver = True


def displayResult():
    # gameOverScreen.visible = True
    gameOverScreen.toFront()
    gameOverMessage.visible = True
    gameOverMessage.toFront()
    startMessage.visible = False
    ball.visible = False
    if playerScore.value == 3:
        gameOverMessage.value = 'Left Wins!'
    else:
        gameOverMessage.value = 'Right Wins!'


def movePaddle(move,paddle):
    if move == 'up' and paddle.top > 40:
        paddle.centerY -= app.paddleSpeed
    elif move == 'down' and paddle.bottom < 360:
        paddle.centerY += app.paddleSpeed


def rotatePaddle(rotation, paddle):
    if rotation == 'clockwise' and paddle.rotateAngle < 45:
        paddle.rotateAngle += app.paddleSpeed
    if rotation == 'counter clockwise' and paddle.rotateAngle > -45:
        paddle.rotateAngle -= app.paddleSpeed


def onStep():
    if app.gameOver == False:
        if app.ballMoving == True:
            advanceBall()
            if app.modeSelected == 1:
                handleplayer2Movement()
            checkGameStatus()
            app.time += 1
            displayTime.value = app.time // 200
            if app.time % app.stepsPerSecond == 0:
                app.counter += 1
                if app.counter != app.counterDelay:
                    ball.speed *= app.ballSpeedMultiplier
                    app.counter == app.counterDelay
    else:
        displayResult()
    
    
def onKeyPress(key):
    if key == 'space' and app.modeSelected != 0:
        app.ballMoving = True
        startMessage.visible = False
    
    if key == "1" or key == "2":
        if app.modeSelected == False:
            app.modeSelected = int(key)
            gameOptions1.visible = False
            gameOptions2.visible = False
            startMessage.visible = True


def onKeyHold(keys):
    if app.modeSelected == 1:
        if 'up' in keys:
            movePaddle('up',player)
        elif 'down' in keys:
            movePaddle('down',player)
        if 'right' in keys:
            rotatePaddle('clockwise', player)
        elif 'left' in keys:
            rotatePaddle('counter clockwise', player)
    
    if app.modeSelected == 2:
        if 'w' in keys:
            movePaddle('up',player)
        elif 's' in keys:
            movePaddle('down',player)
        if 'd' in keys:
            rotatePaddle('clockwise', player)
        elif 'a' in keys:
            rotatePaddle('counter clockwise', player)
            
        if 'up' in keys:
            movePaddle('up',player2)
        elif 'down' in keys:
            movePaddle('down',player2)
        if 'right' in keys:
            rotatePaddle('clockwise', player2)
        elif 'left' in keys:
            rotatePaddle('counter clockwise', player2)

cmu_graphics.run()