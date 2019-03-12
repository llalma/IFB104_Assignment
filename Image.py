from turtle import *
from math import *

#functions

#
#Function for drawing moon
#
def drawMoon(Orientation,coord):
    if Orientation == "Upright":
        Xmoon = coord-40
        Ymoon = 150
        XOnMoon = [Xmoon-30,Xmoon-20,Xmoon+30]
        YOnMoon = [Ymoon-10,Ymoon+15,Ymoon]
    else:
        Xmoon = coord-40
        Ymoon = -150
        XOnMoon = [Xmoon+30,Xmoon+20,Xmoon-30] 
        YOnMoon = [Ymoon+10,Ymoon-15,Ymoon] 

    goto(Xmoon,Ymoon)
    color("#FEFCD7")    #Draw cream circle
    dot(100)
    
    goto(XOnMoon[2],YOnMoon[2])
    color("black")  #Draw black circle to make moon look like crescent 
    dot(100)

#
#Function for drawing stars
#
def drawStars(Orientation,coord):
    xcor = [-60,-10,15,38,53,95,34]
    ycor = [64,59,185,84,27,184,250]
    if Orientation != "Upright":
        xcor = [-x for x in xcor]
        ycor = [-x for x in ycor]
    size = [10,16,13,11,10,13,12,12,17,12]

    color("white")
    for stars in range(len(xcor)):
        goto(coord-xcor[stars],ycor[stars])
        pendown()
        setheading(90)
        forward(size[stars])
        penup()
        goto(coord-xcor[stars]+(size[stars]/2),ycor[stars]+(size[stars]/2))
        setheading(180)
        pendown()
        forward(size[stars])
        penup()
        goto(coord-xcor[stars],ycor[stars]+(size[stars]/2))
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

#
#Function for drawing Trees
#
def drawTrees(Orientation,coord):
    trunkWidth = [5,6,12,6,7,9,11,12,15]  
    treeCorX = [2,0,58,-50,-80,-34,34,53,-63]
    treeCorY = [-70,-236,-90,-60,-233,-225,-124,-203,-157]
    if Orientation != "Upright":
        treeCorX = [-x for x in treeCorX]
        treeCorY = [-x for x in treeCorY]
    
    #Tree Trunk
    for trees in range(len(treeCorX)):
        if Orientation == "Upright":
           trunkAngle = 90
           horHeading = 0
           startingLeaves = [treeCorX[trees]+(-trunkWidth[trees]*2.5),treeCorY[trees]+(trunkWidth[trees]*2-1)]
        else:
           trunkAngle = 270
           horHeading = 180
           startingLeaves = [treeCorX[trees]+(trunkWidth[trees]*2.5),treeCorY[trees]-1]
        goto(treeCorX[trees],treeCorY[trees])
        color("saddlebrown")
        pendown()
        begin_fill()
        if Orientation == "Upright":
            setheading(0)
        else:
            setheading(180)
        for drawBase in range(2):
            forward(trunkWidth[trees])
            left(trunkAngle)
            forward(trunkWidth[trees]*2)
            left(trunkAngle)
        penup()
        end_fill()
       

        #Setup RHS
        diagonalLengths = [trunkWidth[trees]*3,trunkWidth[trees]*3,trunkWidth[trees]*2.5]
        horizontalLengths = [trunkWidth[trees]*1.5,trunkWidth[trees]]
        setheading(horHeading)
        color("green")
        begin_fill()

        #Up RHS
        goto(coord-startingLeaves[0],startingLeaves[1])
        if Orientation == "Upright":
            setheading(0)
        else:
            setheading(180)
        pendown()
        forward(trunkWidth[trees]*6)
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
#Function for drawing ground
#
def drawGround(Orientation,coord):
    xcor = coord-100
    ycor = -250
    heading = 0
    if Orientation != "Upright":
        xcor = 100
        ycor = 250
        heading = 180
    goto(xcor,ycor)
    setheading(heading)
    color("#663300")
    begin_fill()
    pendown()
    forward(200)
    left(90)
    forward(250)
    left(90)
    forward(200)
    left(90)
    forward(250)
    end_fill()

#
#Function for drawing black background
#
def drawBackground(coord):
    xcor = coord-150
    ycor = 250
    heading = 0
    color("#black")
    begin_fill()
    pendown()
    forward(200)
    right(90)
    forward(500)
    right(90)
    forward(200)
    right(90)
    forward(500)
    end_fill()

#
#Function for drawing panel one
#
def drawPanel1(Orientation,coord):
    drawMoon(Orientation,coord)
    drawStars(Orientation,coord)
    drawGround(Orientation,coord)
    drawTrees(Orientation,coord)
    drawBackground(0)

#
#Function for drawing RHS flame
#

def drawFlameRHS(Orientation,coord):

    #Setup
    if Orientation != "Upright":
        xcor = coord+100
        ycor = 30
    else:
        xcor = coord-100
        ycor = -30
    
    radius = 25
    radiusFlameOrange = [radius*2,radius*2,radius*-3.5,radius*-2,radius*6]
    stepsOrange = [90,35,50,50,21.2]
    radiusFlameRed = [radius,radius*2,radius*-3.5,radius*-2,radius*10]
    stepsRed = [90,35,50,50,8]

    #Orange Flame
    goto(xcor,ycor)
    if Orientation != "Upright":
        setheading(180)
    else:
        setheading(0)
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
    print(pos())

    #Red Flame
    goto(xcor,ycor)
    if Orientation != "Upright":
        setheading(180)
    else:
        setheading(0)
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
    print(pos())

#
#Function for drawing LHS flame
#

def drawFlameLHS(Orientation,coord):
    dot()
#image
setup(200,500)
speed(0)
bgcolor("black")
penup()

drawFlameRHS("Upright",0)
drawFlameLHS("Upright",0)
