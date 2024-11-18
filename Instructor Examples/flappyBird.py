from cmu_graphics import *

### Gloabl Variable Set-up
app.gameStart = False
app.background = gradient('violet','black',start='left')
app.vertGap = 200
app.gameOver = False
app.win=False
app.endAnimationCount = 0
app.coinCoolDown = 0
app.bonus = 0
app.scoreAnimationComplete = False
app.scoreAnimationStarted = False
app.scoreAnimationCounter = 0
app.timeCounter = 0


### Shape Object Set-up
# gameBackground = Rect(0,0,10000,400,fill = gradient(rgb(255,204,203),rgb(255, 87, 51),'yellow','lightGreen','lightBlue',rgb(184, 174, 233),'violet',start='left'))
gameBackground = Image('https://iili.io/JINdN07.png', 0, 0)
gameBackgroundFilm = Rect(0,0,400,400,opacity=20)

birbBody = Circle(40,200,30,fill=gradient('white','aqua',start='left'),border='black',borderWidth=4)
birbBeak = RegularPolygon(70,200,10,3,rotateAngle=-25,fill='orange',border='black',borderWidth=2)
birbEye = Oval(55,185,22,27,border='black',fill='white',borderWidth=2,rotateAngle=320)
birdPupil = Circle(57,185,6)

downBirbWing = Polygon(10,200,15,240,20,220,25,260,30,220,35,240,40,200,
                        rotateAngle=20,fill=gradient('white','aqua',start='left'),
                        border='black',borderWidth=2,visible=True)
upBirbWing = Polygon(25,200,30,160,35,180,40,140,45,180,50,160,55,200,
                    rotateAngle=20,fill=gradient('white','aqua',start='left'),
                    border='black',borderWidth=2,visible=False)
                    
birbWingLineCover = Line(18,202,50,202,rotateAngle=20,fill=gradient('white','aqua',start='left'),lineWidth=10,visible=True)

birbBody.distance = 0
birbBody.counter = 0
birbBody.velocity = 9.8
birbBody.direction = 1 #1 is down, -1 is up
 
distanceLabel = Label(birbBody.distance,360,25,size=30,fill='white',bold=True)
bonusLabel = Label('+{}'.format(app.bonus),360,50,size=30,fill='white',bold=True,align='center')
finalScoreLabel = Label('Score: {}'.format(birbBody.distance),200,300,size=40,fill='white',bold=True,visible=False)
finalBonusLabel = Label('Bonus: {}'.format(birbBody.distance),200,250,size=40,fill='white',bold=True,visible=False)
pipeGroup = Group()
coinGroup = Group()
endScreen = Rect(200,250,300,200,fill='black',opacity=50,align='center',visible=False)


### Functional Definitions ###
def handleBirbMovement():
    if birbBody.distance % 17 == 0:
        app.vertGap -= 1
    
    if birbBody.counter > 0:
        birbBody.counter -= 2
        upBirbWing.visible = False #
        downBirbWing.visible = True #
    else:
        birbBody.direction = 1
        upBirbWing.visible = True #
        downBirbWing.visible = False #
        
    birbBody.centerY += birbBody.velocity * birbBody.direction
    birbEye.centerY += birbBody.velocity * birbBody.direction
    birbBeak.centerY += birbBody.velocity * birbBody.direction
    downBirbWing.centerY += birbBody.velocity * birbBody.direction
    upBirbWing.centerY += birbBody.velocity * birbBody.direction
    birbWingLineCover.centerY += birbBody.velocity * birbBody.direction
    birdPupil.centerY += birbBody.velocity * birbBody.direction
    
    birbBody.distance += 1


def drawPipeSet(xPosition):
    c1=rgb(randrange(0,256),randrange(0,256),randrange(0,256))
    c2=rgb(randrange(0,256),randrange(0,256),randrange(0,256))
    c3=rgb(randrange(0,256),randrange(0,256),randrange(0,256))
    c4=rgb(randrange(0,256),randrange(0,256),randrange(0,256))
    c5=rgb(randrange(0,256),randrange(0,256),randrange(0,256))
    c6=rgb(randrange(0,256),randrange(0,256),randrange(0,256))
    
    start1 = choice(['top','bottom','left','right','top-right','top-left'])
    start2 = choice(['top','bottom','left','right','top-right','top-left'])
    
    gradientTop = gradient(c1,c2,c2,start=start1)
    gradientBottom = gradient(c4,c5,c6,start=start2)
    
    #top pipe
    gap = app.vertGap                    
    seed = randrange(20, 240, 10)
    topPipe = Rect(xPosition,-2,60,seed,fill=gradientTop,border='white')
    bottomPipe = Rect(xPosition,seed + gap, 60,400-seed+gap,fill=gradientBottom,border='white')
    pipeGroup.add(topPipe)
    pipeGroup.add(bottomPipe)


def drawCoin(coinX):
    coin = Circle(coinX,randrange(20,380),20,fill='gold',border='black')
    coin.inPlay = True
    coinGroup.add(coin)


def drawGameOver(message):
    endScreen.visible = True 
    Label(message,200,200,size=40,fill='white',bold=True)
    finalScoreLabel.visible = True
    finalScoreLabel.value = 'Score: {}'.format(birbBody.distance)
    finalBonusLabel.visible = True
    finalBonusLabel.value = 'Bonus: {}'.format(app.bonus)
    finalBonusLabel.toFront()


def handlePipesAndCoins():
    for pipe in pipeGroup.children:
        if pipe.left < 0 - 60:
            pipeGroup.remove(pipe)
            
    for coin in coinGroup.children:
        if coin.centerX < 0 - 60:
            coinGroup.remove(coin)
    coinGroup.left -= 12
    pipeGroup.left -= 10
    
    if birbBody.distance % 25 == 20 and birbBody.distance < 960:
        drawPipeSet(400)
    
    if birbBody.distance % 15 == 14 and birbBody.distance < 960:
        drawCoin(420)
    
    if app.coinCoolDown > 0:
        app.coinCoolDown -= 1


def reorderShapes():
    pipeGroup.toFront()
    distanceLabel.toFront()
    bonusLabel.toFront()
    birbToFront()


def birbToFront():
    birbBody.toFront()
    birbBeak.toFront()
    birbEye.toFront()
    birdPupil.toFront()
    downBirbWing.toFront()
    upBirbWing.toFront()
    birbWingLineCover.toFront()


def handleGameOverAnimation():
    if app.win != True and birbBody.centerY < 440:
            handleBirdLoseAnimation()
    elif app.win == True and birbBody.centerX < 440:
            handleBirdWinAnimation()
    elif app.scoreAnimationComplete == False:
            handleEndScreenAnimation() 
    else:
        app.stop()


def handleBirdLoseAnimation():
    dropDist = 8
    birbBody.centerY += dropDist
    birbEye.centerY += dropDist
    birbBeak.centerY += dropDist
    downBirbWing.centerY += dropDist
    upBirbWing.centerY += dropDist
    birbWingLineCover.centerY += dropDist
    birdPupil.centerY += dropDist


def handleBirdWinAnimation():
    dropDist = 6
    birbBody.centerX += dropDist
    birbEye.centerX += dropDist
    birbBeak.centerX += dropDist
    downBirbWing.centerX += dropDist
    upBirbWing.centerX += dropDist
    birbWingLineCover.centerX += dropDist
    birdPupil.centerX += dropDist
    if app.endAnimationCount % 4 == 0:
        tempUpBirbWing = upBirbWing.visible
        upBirbWing.visible = downBirbWing.visible
        downBirbWing.visible = tempUpBirbWing
    app.endAnimationCount += 1


def handleEndScreenAnimation():
    if app.scoreAnimationStarted == False:
        app.scoreAnimationCounter = app.bonus
        app.scoreAnimationStarted = True
    elif app.scoreAnimationCounter > 0:
        if app.timeCounter % 2 == 0:
            birbBody.distance += 1
            app.bonus -= 1
            finalBonusLabel.value = 'Bonus: {}'.format(app.bonus)
            finalScoreLabel.value = 'Score: {}'.format(birbBody.distance)
            finalScoreLabel.toFront()
            app.scoreAnimationCounter -= 1
            if app.bonus == 0:
                finalBonusLabel.visible = False
                finalScoreLabel.fill='lawnGreen'
                finalScoreLabel.bold = True
                finalScoreLabel.top = finalBonusLabel.top
                endScreen.height=150
                app.scoreAnimationComplete = True
                endScreen.border='white'
                endScreen.borderWidth=4


def handleHitCoin():
    for coin in coinGroup.children:
        if app.coinCoolDown == 0:
            if coin.hitsShape(birbBody):
                coin.visible = False
                coin.inPlay = False
                line1 = Line(coin.centerX-15,coin.centerY,coin.centerX+15,coin.centerY,fill=gradient('black','gold'),dashes=False,lineWidth=4,rotateAngle=0)
                line2 = Line(coin.centerX-15,coin.centerY,coin.centerX+15,coin.centerY,fill=gradient('black','gold'),dashes=False,lineWidth=4,rotateAngle=45)
                line3 = Line(coin.centerX-15,coin.centerY,coin.centerX+15,coin.centerY,fill=gradient('black','gold'),dashes=False,lineWidth=4,rotateAngle=90)
                line4 = Line(coin.centerX-15,coin.centerY,coin.centerX+15,coin.centerY,fill=gradient('black','gold'),dashes=False,lineWidth=4,rotateAngle=135)
                coinGroup.add(line1)
                coinGroup.add(line2)
                coinGroup.add(line3)
                coinGroup.add(line4)
                app.coinCoolDown = 10
                app.bonus += 10
                bonusLabel.value ='+{}'.format(app.bonus)
                

def handleHitPipe():
    hitResultBack = pipeGroup.hitTest(birbBody.centerX-birbBody.radius, birbBody.centerY)
    hitResultFront = pipeGroup.hitTest(birbBody.centerX+birbBody.radius, birbBody.centerY)
    hitResultTop = pipeGroup.hitTest(birbBody.centerX, birbBody.centerY-birbBody.radius)
    hitResultBottom = pipeGroup.hitTest(birbBody.centerX, birbBody.centerY+birbBody.radius)
    
    if hitResultBack != None or hitResultFront != None or hitResultTop != None or hitResultBottom != None:
        drawGameOver('GAME OVER')
        app.gameOver=True
        
    if birbBody.centerY < -10 or birbBody.centerY > 410:
        drawGameOver('GAME OVER')
        app.gameOver=True
    
    if birbBody.distance == 1000:
        drawGameOver('YOU WIN!')
        app.win=True
        app.gameOver=True
                
                
def onKeyPress(key):
    if key =='space':
        app.gameStart = True
        birbBody.direction = -1
        birbBody.counter = 10
        

def onStep():
    app.timeCounter += 1
    if app.gameStart == True:
        if app.gameOver == False:
            handleBirbMovement()
            
            distanceLabel.value = birbBody.distance
            gameBackground.left -=3
            
            handlePipesAndCoins()
            handleHitCoin()
            reorderShapes()
            
            handleHitPipe()
            
        else:
            handleGameOverAnimation()


cmu_graphics.run()
