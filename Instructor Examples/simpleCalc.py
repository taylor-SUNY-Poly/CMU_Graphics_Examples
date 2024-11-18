from cmu_graphics import *

## Simple Calculator

app.background = 'black'
calcDisplayBackground = Rect(25,25,350,75,fill='white')
calcDisplayValue = Label(0,calcDisplayBackground.right - 25,63,align='right',size=40)
app.cachedValue = None
app.cachedOperator = None

def createNumericalButtons():
    buttonArray = []
    arrayIndex = 0
    currentLeft = 25
    currentTop = 125
    idleColor = 'pink'
    hoverColor = 'hotPink'
    for row in range(3):
        for col in range(3):
            newButton = Rect(currentLeft,currentTop,50,50,fill=idleColor)
            newButton.number = arrayIndex+1
            newButton.idleColor = idleColor
            newButton.hoverColor = hoverColor
            Label(newButton.number, currentLeft+25, currentTop+25, size=30)
            buttonArray.append(newButton)
            arrayIndex += 1
            currentLeft += 75
        currentLeft = 25
        currentTop += 68
    currentLeft += 75
    zeroButton = Rect(currentLeft,currentTop,50,50,fill=idleColor)
    zeroButton.number = 0
    zeroButton.idleColor = idleColor
    zeroButton.hoverColor = hoverColor
    Label(zeroButton.number, currentLeft+25, currentTop+25, size=30)
    buttonArray.append(zeroButton)
    return buttonArray

def createOperatorButtons():
    operatorSigns = ["+","-","×","÷"]
    operatorArray = []
    currentTop = 125
    currentLeft = 250
    currentIndex = 0
    idleColor = 'lightBlue'
    hoverColor = 'plum'
    for sign in operatorSigns:
        newOperator = Rect(currentLeft,currentTop,50,50,fill=idleColor)
        newOperator.operator = operatorSigns[currentIndex]
        newOperator.idleColor = idleColor
        newOperator.hoverColor = hoverColor
        Label(newOperator.operator,currentLeft+25, currentTop+25,size=30)
        operatorArray.append(newOperator)
        currentIndex += 1
        currentTop += 68
    currentTop = 125
    currentLeft += 75
    equalButton = Rect(currentLeft,currentTop,50,118,fill=idleColor)
    equalButton.operator = "="
    equalButton.idleColor = idleColor
    equalButton.hoverColor = hoverColor
    Label(equalButton.operator, currentLeft+25, currentTop+60,size=30)
    operatorArray.append(equalButton)
    clearButton = Rect(currentLeft,currentTop+136,50,118,fill=idleColor)
    clearButton.operator = "C"
    clearButton.idleColor = idleColor
    clearButton.hoverColor = hoverColor
    operatorArray.append(clearButton)
    Label(clearButton.operator, currentLeft+25, currentTop+196,size=30)
    return operatorArray

numberKeys = createNumericalButtons()
operatorKeys = createOperatorButtons()

def handleHover(keys,mouseX,mouseY):
    for button in keys:
        if button.hits(mouseX,mouseY):
            button.fill = button.hoverColor
        else:
            button.fill = button.idleColor

def handleNumberPress(keys,mouseX,mouseY):
    for key in keys:
        if key.hits(mouseX,mouseY):
            if calcDisplayValue != 0:
                currentVal = str(calcDisplayValue.value)
                currentVal += str(key.number)
                calcDisplayValue.value = int(currentVal)
                key.fill="yellow"
            else:
                calcDisplayValue.value = key.number
                key.fill="yellow"
    calcDisplayValue.right = calcDisplayBackground.right - 25
    
        
def handleOperatorPress(keys,mouseX,mouseY):
    for key in keys:
        if key.hits(mouseX,mouseY):
            if key.operator in ["+","-","×","÷"] and app.cachedOperator == None:
                app.cachedOperator = key.operator
                app.cachedValue = calcDisplayValue.value
                calcDisplayValue.value = 0
                calcDisplayValue.right = calcDisplayBackground.right - 25
            elif key.operator == "C":
                calcDisplayValue.value = 0
                calcDisplayValue.right = calcDisplayBackground.right - 25
                app.cachedValue = None
                app.cachedOperator = None
            elif key.operator == "=" and app.cachedOperator != None:
                calculation = completeCalculation(app.cachedOperator)
                calcDisplayValue.value = calculation
                calcDisplayValue.right = calcDisplayBackground.right - 25
                app.cachedValue = calculation
                app.cachedOperator = None
            key.fill="yellow"

def completeCalculation(operator):
    if operator == "+":
        return app.cachedValue + calcDisplayValue.value
    elif operator == "-":
        return app.cachedValue - calcDisplayValue.value
    elif operator == "×":
        return app.cachedValue * calcDisplayValue.value
    elif operator == "÷":
        return app.cachedValue // calcDisplayValue.value
    
def onMouseMove(mouseX, mouseY):
    handleHover(numberKeys,mouseX,mouseY)
    handleHover(operatorKeys,mouseX,mouseY)

def onMousePress(mouseX,mouseY):
    handleNumberPress(numberKeys,mouseX,mouseY)
    handleOperatorPress(operatorKeys, mouseX, mouseY)

cmu_graphics.run()