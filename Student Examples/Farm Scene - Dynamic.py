### Author: Victoria Vidulich
### Date: 2024

from cmu_graphics import *
### your code

## sky 
Rect(0,0,400,400, fill='lightSkyBlue')


## Windmill 
Rect(155,90,5,130, rotateAngle= 15,fill='darkGray')
Rect(190,90,5,152, rotateAngle=-15, fill='darkGray')
Rect(170,115,7,4, fill='darkGray')
Rect(160,145,25,4,fill='darkGray')
Rect(160,130,32,4,fill='darkGray',rotateAngle=55)
Rect(157,130,32,4,fill='darkGray',rotateAngle=-55)
Rect(145,200,60,4,fill='darkGray')
Rect(147,165,54,4,fill='darkGray',rotateAngle=55)
Rect(135,170,65,4,fill='darkGray',rotateAngle=-55)
line = Line(175,60,230,60,lineWidth=4, fill='darkGray')
mill = Polygon(230,60,235,50,255,50,245,60,255,70,235,70,fill='darkGray')
blades = Group(Circle(173,60,6, fill='darkGray'),
Circle(173,60,4, fill='white'),
Polygon(160,22,174,50,176,50,188,23,fill='white'),
Polygon(142,40,168,55,172,52,158,25,fill='white'),
Polygon(140,45,165,55,165,60,140,65,fill='white'),
Polygon(142,70,165,63,169,67,155,92,fill='white'),
Polygon(162,97,170,70,175,70,185,97,fill='white'),
Polygon(190,94,177,67,180,65,206,80,fill='white'),
Polygon(210,74,180,64,180,58,213,50,fill='white'),
Polygon(210,46,180,55,177,50,193,25,fill='white'))


##Bushes and trees in the back
Line(15,195,15,235,fill='saddleBrown')
Circle(5,185,10,fill='darkOliveGreen')
Circle(20,190,15,fill='darkOliveGreen')
Circle(30,180,15,fill='darkOliveGreen')
Circle(30,165,15,fill='darkOliveGreen')
Circle(20,155,12,fill='darkOliveGreen')
Circle(10,150,15,fill='darkOliveGreen')
Circle(5,165,15,fill='darkOliveGreen')
Line(75,190,75,220,fill='saddleBrown')
Circle(50,165,12,fill='yellowGreen')
Circle(54,180,10,fill='yellowGreen')
Circle(67,190,12,fill='yellowGreen')
Circle(82,190,12,fill='yellowGreen')
Circle(90,170,18,fill='yellowGreen')
Circle(80,155,12,fill='yellowGreen')
Circle(70,150,15,fill='yellowGreen')
Circle(67,167,15,fill='yellowGreen')
Circle(47,230,15,fill='oliveDrab')
Circle(67,222,17,fill='oliveDrab')
Circle(85,220,10,fill='oliveDrab')
Circle(5,225,15,fill='yellowGreen')
Circle(27,230,10,fill='yellowGreen')
Circle(157,215,17,fill='yellowGreen')
Circle(175,220,10,fill='yellowGreen')
Circle(135,215,10,fill='yellowGreen')
Circle(48,165,6,fill='lightSalmon')
Circle(55,180,6,fill='lightSalmon')
Circle(68,192,6,fill='lightSalmon')
Circle(86,190,6,fill='lightSalmon')
Circle(75,173,6,fill='lightSalmon')
Circle(65,160,6,fill='lightSalmon')
Circle(70,146,6,fill='lightSalmon')
Circle(84,157,6,fill='lightSalmon')
Circle(97,170,6,fill='lightSalmon')

##backround hills 
Polygon(0,240,10,235,20,230,35,225,55,220,70,218,80,216,105,215,120,215,155,220,
175,225,187,228,250,250,340,280,400,300,400,400,0,400, fill='oliveDrab')
Polygon(0,240,10,235,20,230,35,225,55,220,70,218,80,216,105,215,120,215,155,220,
175,225,187,228,35,400,0,400, fill='sienna')
Polygon(40,225,75,217,177,240,160,258,fill=rgb(130,80,52))
Polygon(0,240,10, 235,20,230,150,270,135,285, fill=rgb(130,80,52))
Polygon(0,255,33,270,0,267,fill=rgb(130,80,52))
Polygon(0,267,65,270,140,280,210,300,215,301,375,400,0,400, fill='darkOliveGreen')


## Barn
Polygon(185,195,205,145,240,110,305,120,325,165,335,225,310,280,190,260,fill='red')
Polygon(200,125,205,145,185,195,185,170,fill='white')
Polygon(200,125,235,100,240,110,205,145,fill='white')
Polygon(235,100,330,105,305,120,240,110,fill='white')
Polygon(305,120,325,165,375,145,330,105,fill='white')
Polygon(325,165,375,145,395,210,335,225,fill='white')
Polygon(335,225,310,280,360,290,395,210,fill='fireBrick')
Rect(240,130,55,40,rotateAngle=10,fill='maroon',border='white',borderWidth=5)
Rect(205,175,115,6,rotateAngle=10,fill='white')
Polygon(220,265,225,265,225,190,215,190,fill='white',rotateAngle=10)
Polygon(290,200,295,277,300,277,300,200,fill='white',rotateAngle=15)
Polygon(222,189,223,200,300,210,300,200, fill='white')
Polygon(218,265,218,260,288,270,288,276.5,fill='white')
Polygon(235,265,240,265,240,190,235,190,fill='white',rotateAngle=-10)
Polygon(235,265,240,265,240,190,235,190,fill='white',rotateAngle=25)
Polygon(250,195,260,195,260,265,250,268,fill='white',rotateAngle=10)
Polygon(270,195,275,195,285,275,280,275,fill='white',rotateAngle=-5)
Polygon(270,195,275,195,285,275,280,275,fill='white',rotateAngle=45)

#clouds
cloud1 = Group(Circle(90,85,20, fill='white'),
Circle(65,90,10,fill='white'),
Circle(115,95,10,fill='white'),
Oval(90,100,110,15,fill='white'))
cloud2 = Group(Circle(325,35,20,fill='white'),
Circle(305,40,12,fill='white'),
Circle(345,42,12,fill='white'),
Oval(325,47,120,17,fill='white'))

##Bushes and Tree in the front
Line(380,325,380,400,fill='saddleBrown')
Circle(400,290,40,fill='darkOliveGreen')
Circle(368,270,30,fill='darkOliveGreen')
Circle(345,290,15,fill='darkOliveGreen')
Circle(355,310,20,fill='darkOliveGreen')
Circle(380,320,25,fill='darkOliveGreen')
Circle(335,390,12,fill=rgb(65,90,60))
Circle(360,390,20,fill=rgb(65,90,60))
Circle(390,390,25,fill=rgb(65,90,60))
Circle(400,328,7,fill='coral')
Circle(378,326,5,fill='coral')
Circle(351,315,6,fill='coral')
Circle(345,288,7,fill='coral')
Circle(383,302,6.5,fill='coral')
Circle(368,285,6,fill='coral')
Circle(402,290,6,fill='coral')
Circle(386,265,6,fill='coral')
Circle(373,250,5,fill='coral')
Circle(356,260,6,fill='coral')

##fence,bush, and tulips 
Rect(0,330,195,15,fill='white')
Rect(0,290,15,210,fill='white')
Rect(30,290,15,210,fill='white')
Rect(60,290,15,210,fill='white')
Rect(90,290,15,210,fill='white')
Rect(120,290,15,210,fill='white')
Rect(150,290,15,210,fill='white')
Rect(180,290,15,210,fill='white')
Polygon(0,290,7.5,284,15,290,fill='white')
Polygon(30,290,37.5,284,45,290,fill='white')
Polygon(60,290,67.5,284,75,290,fill='white')
Polygon(90,290,97.5,284,105,290,fill='white')
Polygon(120,290,127.5,284,135,290,fill='white')
Polygon(150,290,157.5,284,165,290,fill='white')
Polygon(180,290,187.5,284,195,290,fill='white')
Circle(250,395,25,fill=rgb(65,90,60))
Circle(210,390,35,fill=rgb(65,90,60))
Circle(180,358,12,fill=rgb(65,90,60))
Circle(180,390,25,fill=rgb(65,90,60))
Circle(0,360,7,fill='lightCoral')
Polygon(-3,360,5,345,7,360,fill='lightCoral')
Oval(20,385,15,70,fill='oliveDrab',rotateAngle=-15)
Oval(0,385,5,50,fill='yellowGreen',rotateAngle=45)
Circle(32,352,7,fill='lightCoral')
Polygon(25,352,23,337,32,345,39,337,39,353,fill='lightCoral')
Circle(43,383,7,fill='lightCoral')
Polygon(36,385,32,370,40,375,44,363,50,385,fill='lightCoral')
Circle(74,346,7,fill='lightCoral')
Polygon(67,347,61,338,70,338,75,330,80,344,fill='lightCoral')
Circle(105,365,7,fill='lightCoral')
Polygon(98,365,98,350,104,356,108,350,112,365,fill='lightCoral')
Circle(124,356,7,fill='lightCoral')
Polygon(117,356,117,343,124,349,131,343,131,356,fill='lightCoral')
Circle(157,360,7,fill='lightCoral')
Polygon(150,360,150,340,157,350,164,340,164,360,fill='lightCoral')
Oval(185,400,15,110,fill='oliveDrab',rotateAngle=-10)
Circle(182,345,7,fill='lightCoral')
Polygon(175,345,175,331,182,335,189,331,189,345,fill='lightCoral')
Oval(205,400,15,110,fill='oliveDrab',rotateAngle=10)
Circle(205,375,7,fill='lightCoral')
Polygon(199,380,195,365,203,368,207,360,212,374,fill='lightCoral')
Oval(35,400,10,40,fill='yellowGreen',rotateAngle=40)
Oval(65,380,15,70,fill='yellowGreen',rotateAngle=-10)
Oval(95,390,13,92,fill='oliveDrab',rotateAngle=-17)
Oval(86,377,10,25,fill='yellowGreen',rotateAngle=25)
Oval(115,400,12,50,fill='yellowGreen')
Oval(135,400,2,87,fill='yellowGreen',rotateAngle=-20)
Oval(160,400,15,70,fill='oliveDrab')
Oval(147,400,20,90,fill='yellowGreen',rotateAngle=-15)
Oval(170,400,20,90,fill='yellowGreen',rotateAngle=15)


blades.totalSteps = 0
blades.sumSteps = 0

def debugAvgCenter():
    blades.totalSteps += 1
    blades.sumSteps += blades.centerX

def onStep():
    blades.rotateAngle += 2
    line.x1 = blades.centerX
    line.y1 = blades.centerY
    line.x2 += 175.915 - blades.centerX
    mill.centerX += 175.915 - blades.centerX
    cloud1.centerX += 0.75
    cloud2.centerX += 1
    if cloud1.left >= 400:
        cloud1.right = 0
    if cloud2.left >= 400:
        cloud2.right = 0
    # debugAvgCenter()
    # print(blades.sumSteps / blades.totalSteps)



cmu_graphics.run()