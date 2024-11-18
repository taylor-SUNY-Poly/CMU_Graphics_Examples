from cmu_graphics import *


app.background=gradient('black','slateGrey',start='top-left')

### background neons
Circle(200,200,50,fill=None,border=rgb(77,238,234),borderWidth=2)
Circle(200,200,100,fill=None,border=rgb(116,238,21),borderWidth=4)
Circle(200,200,150,fill=None,border=rgb(255,231,0),borderWidth=6)
Circle(200,200,200,fill=None,border=rgb(240,0,255),borderWidth=8)
Circle(200,200,250,fill=None,border=rgb(100,30,255),borderWidth=10)

### OPM Title
#variable that is used for gradient in image title
opmGradient = gradient(rgb(232,192,94),rgb(156,60,55),rgb(232,192,94))
#image title
Label('ONE',130,50, fill=opmGradient, size=60, font='cinzel', bold=True, 
    border='white', borderWidth=1)
Label('PUNCH',130,110, fill=opmGradient, size=60, font='cinzel', bold=True,
    border='white', borderWidth=1)
Label('MAN',130,170, fill=opmGradient, size=60, font='cinzel', bold=True,
    border='white', borderWidth=1)

### left ear
Polygon(180,195,    173,200,    168,210,    166,225,    166,226,    168,235,
        fill=rgb(228,188,162), border='black', borderWidth=1)

### head
Polygon(202,150,    210,140,    220,132,    230,125,    250,115,
        270,111,    290,111,    310,115,    330,126,    340,135,
        350,150,    358,167,    362,184,    362,200,    358,217,
        350,240,    303,310,    290,320,    275,330,    250,339,
        222,342,    211,342,    200,339,    193,336,    181,325,
        173,312,    170,300,    167,284,    165,260,    167,232,
        178,200,    188,175,
        fill=rgb(228,188,162), border='black',borderWidth=1)

### upper head features
# bald shine
Oval(232,138,30,11,fill='white',opacity=60,rotateAngle=146)
# left brow
Line(200,172,    205,171, lineWidth=0.5)
Line(205,171,    215,172, lineWidth=0.5)
Line(215,172,    220,172, lineWidth=0.5)
Line(220,172,    225,173, lineWidth=0.5)
Line(225,173,    230,174, lineWidth=0.5)
Line(230,174,    235,175, lineWidth=0.5)
# right brow
Line(268,180,    270,180, lineWidth=0.5)
Line(270,180,    275,181, lineWidth=0.5)
Line(275,181,    280,182, lineWidth=0.5)
Line(280,182,    285,183, lineWidth=0.5)
Line(285,183,    290,185, lineWidth=0.5)
Line(290,185,    295,187, lineWidth=0.5)
Line(295,187,    300,190, lineWidth=0.5)
Line(300,190,    305,193, lineWidth=0.5)
Line(305,193,    310,196, lineWidth=0.5)
Line(310,196,    315,200, lineWidth=0.5)

### eyes
# left eye white
Polygon(195,200,    196,195,    200,192,    205,192,    210,192,
        215,193,    220,194,    225,197,    229,200,    229,203,
        228,205,    225,208,    222,210,    220,211,    215,212,    
        210,212,
        205,211,    202,209,    200,208,    197,205,
        fill='white', border='black', borderWidth=1)
# left eye pupil
Circle(211,200,2)

# right eye white
Polygon(270,205,    275,206,    280,208,    285,210,    290,212,
        297,216,    299,220,    299,222,    297,225,    295,228,
        290,230,    285,231,    280,231,    275,230,    270,228,
        266,225,    265,223,    263,220,    262,215,    262,210,
        265,206, fill='white',border='black', borderWidth=1)
# right eye pupil
Circle(277,216,2)

### nose
# lower nose triangle
Polygon(215,250,212,239,214,236)
# nostril
Circle(220,248,1)
# nose tip top
Polygon(212,239,    214,236,    220,230)
# nose bridge
Line(214,236,   220,230, lineWidth=1)
Line(220,230,   227,220, lineWidth=1)
Line(227,220,    233,210, lineWidth=1)
Line(233,210,    238,198, lineWidth=1)
Line(238,198,    238,194, lineWidth=1)

### right ear
# outer lobe edge
Polygon(335,250,    340,248,    345,246,    350,248,    352,250,
        353,255,    354,260,    353,265,    350,270,    349,275,
        346,280,    345,282,    344,285,    340,290,    335,295,
        330,300,    325,304,    320,306,    315,309,    310,310,
        305,309,    302,308,    300,305, 
        fill=rgb(228,188,162), border='black',borderWidth=1) 
# coverup of right edge of polygon above
Line(300,305,   335,250, fill=rgb(228,188,162), lineWidth=4)
# ear canal
Polygon(315,291,    318,284,    320,285,    324,280,    325,275,
        327,271,    330,275,    328,280,    325,285,    320,290,
        316,291, fill=rgb(175,121,101), border='black', borderWidth=0.65)
# inner lobe edge
Line(327,271,    325,275, lineWidth=1)
Line(327,271,    330,268, lineWidth=1)
Line(330,268,    333,265, lineWidth=1)
Line(333,265,    335,264, lineWidth=1)
Line(335,264,    340,260, lineWidth=1)
Line(340,260,    345,258, lineWidth=1)
Line(345,258,    346,259, lineWidth=1)
Line(346,259,    347,263, lineWidth=1)
Line(347,263,    345,268, lineWidth=1)
# inner lobe detail
Line(342,260,   338,265, lineWidth=1)
Line(338,265,   335,270, lineWidth=1)
# outer lobe detail
Line(345,260,    343,265,lineWidth=1)
Line(343,265,    343,270,lineWidth=1)
Line(343,270,    340,275,lineWidth=1)
Line(340,275,    338,279,lineWidth=1)
Line(338,279,    334,283,lineWidth=1)
# low lobe detail
Line(307,299,    310,297, lineWidth=1)
Line(310,297,    315,298, lineWidth=1)
Line(315,298,    320,298, lineWidth=1)
Line(320,298,    325,296, lineWidth=1)
Line(325,296,    328,294, lineWidth=1)

### mouth
# inner mouth
Rect(200,270,45,16,fill=rgb(87,55,48))
# tongue
Oval(227,282,41,15,fill=rgb(180,124,109))
# upper mouth
Polygon(200,270,    210,274,    220,277,    240,279,    250,280,
        250,260,fill=rgb(228,190,167))
# lower mouth
Polygon(200,270,    201,274,    202,277,    210,285,    215,286, 
        220,287,    225,287,    230,287,    240,284,    250,280,
        250,300,    200,300,    190,280,    fill=rgb(228,190,167))
# upper mouth outline
Line(200,270,    210,274, lineWidth=1)
Line(210,274,    220,277, lineWidth=1)
Line(220,277,    240,279, lineWidth=1)
Line(240,279,    250,280, lineWidth=1)
#lower mouth outline
Line(200,270,    201,274, lineWidth=1)
Line(201,274,    202,277, lineWidth=1)
Line(202,277,    210,285, lineWidth=1)
Line(210,285,    215,286, lineWidth=1)
Line(215,286,    220,287, lineWidth=1)
Line(220,287,    230,287, lineWidth=1)
Line(230,287,    240,284, lineWidth=1)
Line(240,284,    250,280, lineWidth=1)

### total planning and development time ~ 5 hours
'''
Note: This block of time includes brainstorming ideas, creating grid tools
to assist in determining plot positions, determining plot positions, plotting 
shapes, trouble shooting, iteration on design, and refactoring code for
readability.
'''

cmu_graphics.run()
