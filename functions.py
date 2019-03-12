from turtle import *
from math import *


#
#Function for drawing moon
#

def drawMoon(Xcoords,Orientation):
    if Orientation == "Upright":
        Xmoon = Xcoords - 75
        Ymoon = 150
        XOnMoon = [Xmoon-30,Xmoon-20,Xmoon+30]
        YOnMoon = [Ymoon-10,Ymoon+15,Ymoon]
    else:
        Xmoon = 75
        Ymoon = -150
        XOnMoon = [Xmoon+30,Xmoon+20,Xmoon-30] 
        YOnMoon = [Ymoon+10,Ymoon-15,Ymoon] 

    goto(Xmoon,Ymoon)
    color("#FEFCD7")    #Draw cream circle
    dot(100)
    goto(XOnMoon[2],YOnMoon[2])
    color("black")                  #Draw black circle to make moon look like crescent 
    dot(100)
    
#
#Function for drawing stars
#

    
def drawStars(size,Orientation):
    if Orientation == "Upright":
        x = 0
        y = 0
    else:
       x = []
       y = []

    color("white")
    pendown()
    setheading(90)
    forward(size)
    penup()
    goto(x+(size/2),y+(size/2))
    setheading(180)
    pendown()
    forward(size)
    penup()
    goto(x,y+(size/2))
    setheading(45)
    forward(size/2)
    setheading(225)
    pendown()
    forward(size)
    penup()
    setheading(45)
    forward(size/2)
    setheading(-45)
    forward(size/2)
    setheading(135)
    pendown()
    forward(size)
    penup()

#
#Function for drawing trees
#

def drawTree(trunkWidth, Orientation):
    if Orientation == "Upright":
        trunkAngle = 90
        horHeading = 0
        startingLeaves = [-trunkWidth*2.5,trunkWidth*2-1]
    else:
        trunkAngle = 270
        horHeading = 180
        startingLeaves = [trunkWidth*3.5,-trunkWidth*2+1]
    
    #Tree Trunk   
    #goto(bottom left tree trunk)
    color("saddlebrown")
    pendown()
    begin_fill()
    for drawBase in range(2):
        forward(trunkWidth)
        left(trunkAngle)
        forward(trunkWidth*2)
        left(trunkAngle)
    end_fill()
    penup()

    #Setup RHS
    diagonalLengths = [trunkWidth*3,trunkWidth*3,trunkWidth*2.5]
    horizontalLengths = [trunkWidth*1.5,trunkWidth]
    setheading(horHeading)
    color("green")
    begin_fill()

    #Up RHS
    goto(startingLeaves[0],startingLeaves[1])
    pendown()
    forward(trunkWidth*6)
    for RHS in range(2):
        left(130)
        forward(diagonalLengths[RHS])
        setheading(horHeading)
        forward(horizontalLengths[RHS])
    left(130)
    forward(diagonalLengths[2])
    
    #Seup LHS
    diagonalLengths = list(reversed(diagonalLengths))
    horizontalLengths = list(reversed(horizontalLengths))

    #Down LHS
    left(100)
    for LHS in range(2):
        forward(diagonalLengths[LHS])
        setheading(horHeading)
        forward(horizontalLengths[LHS])
        right(130)
    forward(diagonalLengths[LHS])
    end_fill()
    penup()




#
#Function for drawing Mountains (not done)
#

def drawMountains(Orientation):
    color("grey")
    angles = [23,40,45,23,26,110]
    lengths = [50,43,12,16,35,123]
    capX = []
    capY = []
    if Orientation == "Upright":
        goto(-100,150)
        pendown()
        setheading(0)
        for mountains in range(len(angles)):
            if not(xcor() >= 150):
                left(angles[mountains])
                forward(lengths[mountains])
                capX = capX + [xcor()]
                capY = capY + [ycor()]
                right(angles[mountains]+10)
                forward(lengths[mountains])
    else:
        goto(100,-150)
        pendown()
        setheading(180)
        for mountains in range(len(angles)):
            if not(xcor() <= -150):
                left(angles[mountains])
                forward(lengths[mountains])
                capX = capX + [xcor()]
                capY = capY + [ycor()]
                right(angles[mountains]+10)
                forward(lengths[mountains])
    if Orientation == "Upright":
        setheading(270)
    else:
        setheading(90)
    forward((ycor()-150)+150)
    right(90)
    forward(200)
    right(90)
    forward(150)
    

#
#Function for drawing LHS fire
#

def drawFireLHS(Orientation):

    #goto(Position)
    length = 200
    width = 35
    height = 30

    if Orientation != "Upright":
        setheading(180)
    
    color("peru")
    pendown()
    fillcolor("saddlebrown")
    begin_fill()

    forwards = [length,height,length,height,width,length,width]
    headings = [120,60,120,-50,110,70,-80]

    left(30)
    for draw in range(len(forwards)):
        forward(forwards[draw])
        right(headings[draw])

    home()
    forwards = [width,height,width]
    headings = [140,130,50]

    if Orientation != "Upright":
        setheading(180)
    for draw in range(len(forwards)):
        left(headings[draw])
        forward(forwards[draw])
        
    end_fill()


#
#Function for drawing LHS flame
#

def drawFlameRHS(Orientation):

    #Setup
    radius = 50
    radiusFlameOrange = [radius*2,radius*2,radius*-3.5,radius*-2,radius*6]
    stepsOrange = [90,35,50,50,21.2]
    radiusFlameRed = [radius,radius*2,radius*-3.5,radius*-2,radius*10]
    stepsRed = [90,35,50,50,8]

    #Orange Flame
    color("orange")
    right(90)
    forward(160)
    left(90)
    fillcolor("orange")
    begin_fill()
    pendown()
    for flame in range(len(radiusFlameOrange)):
        circle(radiusFlameOrange[flame],stepsOrange[flame])
        if radiusFlameOrange[flame] == radius*-2:
            left(150)
    end_fill()

    #Red Flame
    home()
    right(90)
    forward(150)
    left(90)
    fillcolor("red")
    begin_fill()
    pendown()
    for flame in range(len(radiusFlameRed)):
        circle(radiusFlameRed[flame],stepsRed[flame])
        if radiusFlameRed[flame] == radius*-2:
            left(180)
    end_fill()

def drawStars1(Orientation):
    xcor = [0]
    ycor = [0]
    if Orientation != "Upright":
        xcor = [-x for x in xcor]
        ycor = [-x for x in ycor]
    size = [200]

    color("white")
    for stars in range(len(xcor)):
        goto(xcor[stars],ycor[stars])
        pendown()
        setheading(90)
        forward(size[stars])
        penup()
        goto(xcor[stars]+(size[stars]/2),ycor[stars]+(size[stars]/2))
        setheading(180)
        pendown()
        forward(size[stars])
        penup()
        goto(xcor[stars],ycor[stars]+(size[stars]/2))
        setheading(45)
        forward(size[stars]/2)
        setheading(225)
        pendown()
        forward(size[stars])
        penup()
        setheading(45)
        forward(size[stars]/2)
        setheading(315)
        forward(size[stars]/2)
        setheading(135)
        pendown()
        forward(size[stars])
        penup()
        goto(xcor[stars],ycor[stars])
        setheading(0)
        pendown()
        circle(size[stars]/2)
    


    
    

setup(200,500)
penup()
bgcolor("black")
drawStars1("Upright")

hideturtle()
done()
