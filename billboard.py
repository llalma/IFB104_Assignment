
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N9960392
#    Student name: Liam Hulsman-Benson
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BILLBOARD
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "paste_up".
#  You are required to complete this function so that when the
#  program is run it produces an image of an advertising billboard
#  whose arrangement is determined by data stored in a list which
#  specifies how individual paper sheets are to be pasted onto the
#  backing.  See the instruction sheet accompanying this file for
#  full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

sheet_width = 200 # pixels
sheet_height = 500 # pixels
backing_margin = 20 # pixels
backing_width = sheet_width * 4 + backing_margin * 2
backing_height = sheet_height + backing_margin * 2
canvas_top_and_bottom_border = 150 # pixels
canvas_left_and_right_border = 300 # pixels
canvas_width = (backing_width + canvas_left_and_right_border)
canvas_height = (backing_height + canvas_top_and_bottom_border)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(mark_centre_points = True):

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 5 # pixels
    grass_height = 100 # pixels
    penup()
    goto(-(canvas_width // 2 + overlap),
         -(canvas_height // 2 + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_height + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_height + overlap)
    end_fill()

    # Draw a nice warm sun peeking into the image
    penup()
    goto(-canvas_width // 2, canvas_height // 2)
    color('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height // 3)
    color('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Draw the billboard's wooden backing as four frames
    # and some highlighted coordinates
    #
    # Outer rectangle
    goto(- backing_width // 2, - backing_height // 2) # bottom left
    pencolor('sienna'); fillcolor('tan'); width(3)
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height)
    right(90) # face east
    forward(backing_width)
    right(90) # face south
    forward(backing_height)
    right(90) # face west
    forward(backing_width)
    end_fill()

    # Inner rectangle
    penup()
    goto(- backing_width // 2 + backing_margin,
         - backing_height // 2 + backing_margin) # bottom left
    fillcolor('gainsboro')
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height - backing_margin * 2)
    right(90) # face east
    forward(backing_width - backing_margin * 2)
    right(90) # face south
    forward(backing_height - backing_margin * 2)
    right(90) # face west
    forward(backing_width - backing_margin * 2)
    end_fill()

    # Draw lines separating the locations where the sheets go
    width(1); pencolor('dim grey')
    for horizontal in [-sheet_width, 0, sheet_width]:
        penup()
        goto(horizontal, sheet_height // 2)
        pendown()
        setheading(270) # point south
        forward(sheet_height)
         
    # Mark the centre points of each sheet's location, if desired
    if mark_centre_points:
        penup()
        points = [[[round(-sheet_width * 1.5), 0], 'Location 1'],
                  [[round(-sheet_width * 0.5), 0], 'Location 2'],
                  [[round(sheet_width * 0.5), 0], 'Location 3'],
                  [[round(sheet_width * 1.5), 0], 'Location 4']]
        for centre_point, label in points:
            goto(centre_point)
            dot(4)
            write('  ' + label + '\n  (' + str(centre_point[0]) + ', 0)',
                  font = ('Arial', 12, 'normal'))
     
    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)


# End the program by hiding the cursor and releasing the canvas
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data------------------------------------------------------#
#
# The list in this section contains the data sets you will use to
# test your code.  Each of the data sets is a list specifying the
# way in which sheets are pasted onto the billboard:
#
# 1. The name of the sheet, from 'Sheet A' to 'Sheet D'
# 2. The location to paste the sheet, from 'Location 1' to
#    'Location 4'
# 3. The sheet's orientation, either 'Upright' or 'Upside down'
#
# Each data set does not necessarily mention all four sheets.
#
# In addition there is an extra value, either 'X' or 'O' at the
# start of each data set.  The purpose of this value will be
# revealed only in Part B of the assignment.  You should ignore it
# while completing Part A.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Note that your solution must work for all the data sets below
# AND ANY OTHER DATA SETS IN THE SAME FORMAT!
#

data_sets = [
    # These two initial data sets don't put any sheets on the billboard
    # Data sets 0 - 1
    ['O'],
    ['X'],
    # These data sets put Sheet A in all possible locations and orientations
    # Data sets 2 - 9
    ['O', ['Sheet A', 'Location 1', 'Upright']],
    ['O', ['Sheet A', 'Location 2', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright']],
    ['O', ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 2', 'Upside down']],
    ['O', ['Sheet A', 'Location 3', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down']],
    # These data sets put Sheet B in all possible locations and orientations
    # Data sets 10 - 17
    ['O', ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet B', 'Location 2', 'Upright']],
    ['O', ['Sheet B', 'Location 3', 'Upright']],
    ['O', ['Sheet B', 'Location 4', 'Upright']],
    ['O', ['Sheet B', 'Location 1', 'Upside down']],
    ['O', ['Sheet B', 'Location 2', 'Upside down']],
    ['O', ['Sheet B', 'Location 3', 'Upside down']],
    ['O', ['Sheet B', 'Location 4', 'Upside down']],
    # These data sets put Sheet C in all possible locations and orientations
    # Data sets 18 - 25
    ['O', ['Sheet C', 'Location 1', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 3', 'Upright']],
    ['O', ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upside down']],
    ['O', ['Sheet C', 'Location 3', 'Upside down']],
    ['O', ['Sheet C', 'Location 4', 'Upside down']],
    # These data sets put Sheet D in all possible locations and orientations
    # Data sets 26 - 33
    ['O', ['Sheet D', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 2', 'Upright']],
    ['O', ['Sheet D', 'Location 3', 'Upright']],
    ['O', ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet D', 'Location 2', 'Upside down']],
    ['O', ['Sheet D', 'Location 3', 'Upside down']],
    ['O', ['Sheet D', 'Location 4', 'Upside down']],
    # These data sets place two sheets in various locations and orientations
    # Data sets 34 - 38
    ['O', ['Sheet D', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    # These data sets place three sheets in various locations and orientations
    # Data sets 39 - 43
    ['O', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']], 
    ['O', ['Sheet B', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 2', 'Upside down'],
          ['Sheet C', 'Location 1', 'Upside down']], 
    ['X', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upright']],
    # These data sets place four sheets in various locations and orientations
    # Data sets 44 - 48
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],     
    # These data sets draw the entire image upside down
    # Data sets 49 - 50
    ['X', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    # These are the final, 'correct' arrangements of sheets
    # Data sets 51 - 52
    ['X', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']]
    ]

#
#--------------------------------------------------------------------#

#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "paste_up" function.
#

#Created Functions

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
        Xmoon = coord+40
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
def drawStars(Orientation,coord,xcor,ycor):
    if Orientation != "Upright":
        xcor = [-x for x in xcor]       #If upside down make x and y cords negative
        ycor = [-x-30 for x in ycor]
    size = [10,16,13,11,10,13,12,12,17,12]      #Size of stars

    color("white")

    #Draw Stars
    for stars in range(len(xcor)):
        penup()
        goto(coord+xcor[stars],ycor[stars])
        pendown()
        setheading(90)
        forward(size[stars])
        penup()
        goto(coord+xcor[stars]+(size[stars]/2),ycor[stars]+(size[stars]/2))
        setheading(180)
        pendown()
        forward(size[stars])
        penup()
        goto(coord+xcor[stars],ycor[stars]+(size[stars]/2))
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
def drawTrees(Orientation,coord,treeCorX,treeCorY):
    trunkWidth = [5,6,12,6,7,9,11,12,15]    #Size of trees
    if Orientation != "Upright":
        treeCorX = [-x for x in treeCorX]       #If upside down make x and y cords negative
        treeCorY = [-x -30 for x in treeCorY]
    
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
        goto(coord+treeCorX[trees],treeCorY[trees])
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
       

        #Setup for the RHS of the tree 
        diagonalLengths = [trunkWidth[trees]*3,trunkWidth[trees]*3,trunkWidth[trees]*2.5]
        horizontalLengths = [trunkWidth[trees]*1.5,trunkWidth[trees]]
        setheading(horHeading)
        color("green")
        begin_fill()

        #Draw the RHS of the tree
        goto(coord+startingLeaves[0],startingLeaves[1])
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
        
        #Setup for the LHS of the tree 
        diagonalLengths = list(reversed(diagonalLengths))
        horizontalLengths = list(reversed(horizontalLengths))

        #Draw the LHS of the tree
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
#Function for drawing the ground
#
def drawGround(Orientation,coord):
    xcor = coord-100
    ycor = -250
    heading = 0
    if Orientation != "Upright":        #If upside down alter x and y coordinates.
        xcor = coord+100
        ycor = 250
        heading = 180
    goto(xcor,ycor)
    setheading(heading)
    color("#663300")        #set colour to a different brown than the tree stumps

    #Draw the shape then fill
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
    penup()

#
#Function for drawing black background
#
def drawBackground(coord):
    xcor = coord-100
    ycor = 250
    goto(xcor,ycor)
    setheading(0)
    color("black")

    #Draw Shape and fill
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
    penup()

#
#Function for drawing RHS flame
#

def drawFlameRHS(Orientation,coord):

    #Setup
    if Orientation != "Upright":    #Get correct x and y coords depending on the orientation
        xcor = coord+101
        ycor = 25
    else:
        xcor = coord-100
        ycor = -30
    
    radius = 12.5       #All values for the flame are from this value.
    radiusFlameOrange = [radius*2,radius*2,radius*-3.5,radius*-2,radius*6]  #Alter radius for each cicle in the flame.
    stepsOrange = [90,35,50,50,21.2]    #How much of each circle is drawn for the orange flame
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
    forward(160)        #Move to correct starting location
    left(90)
    fillcolor("orange")

    #Draw Flame
    begin_fill()
    pendown()
    for flame in range(len(radiusFlameOrange)):
        circle(radiusFlameOrange[flame],stepsOrange[flame])     #For each radius in the radiusFlameOrange array, draw a circle with corrosponding radius and steps
        if radiusFlameOrange[flame] == radius*-2:   #Top of the flame
            left(150)
    end_fill()
    penup()

    #Red Flame -  draw the smaller flame inside the larger one, same method as large flame
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
    penup()

#
#Function for drawing LHS flame - Same as RHS of flame but with different values
#

def drawFlameLHS(Orientation,coord):

    #Setup
    if Orientation != "Upright":
        xcor = coord-100
        ycor = 185
    else:
        xcor = coord+100
        ycor = -190
    
    radius = -12.5
    radiusFlameOrange = [radius*2,radius*5]
    stepsOrange = [70,76]
    radiusFlameRed = [radius*1.5,radius*10]
    stepsRed = [98,25]

    #Orange Flame
    goto(xcor,ycor)
    if Orientation != "Upright":
        setheading(0)
    else:
        setheading(180)
    color("orange")
    fillcolor("orange")
    begin_fill()
    pendown()
    for flame in range(len(radiusFlameOrange)):
        circle(radiusFlameOrange[flame],stepsOrange[flame])
    end_fill()
    penup()

    #Red Flame
    if Orientation != "Upright":
        xcor = coord-100
        ycor = 180
    else:
        xcor = coord+100
        ycor = -180
        
    goto(xcor,ycor)
    if Orientation != "Upright":
        setheading(0)
    else:
        setheading(180)
    fillcolor("red")
    begin_fill()
    pendown()
    for flame in range(len(radiusFlameRed)):
        circle(radiusFlameRed[flame],stepsRed[flame])
    end_fill()
    penup()

#
#Function for drawing log at bottom of flame (LHS)
#

def drawLogfireRHS(Orientation,coord):
    #Setup
    if Orientation != "Upright":
        heading = 180
        xcor = coord+101
        ycor = 170
    else:
        heading = 0
        xcor = coord -100
        ycor = -175

    goto(xcor,ycor)
    setheading(heading)
    fillcolor('saddlebrown')
    color('saddlebrown')
    begin_fill()
    pendown()
    forward(50)
    right(90)
    forward(20)
    right(90)
    forward(50)
    right(90)
    forward(20)
    penup()
    end_fill()

#
#Function for drawing log at bottom of flame RHS
#

def drawLogfireLHS(Orientation,coord):
    #Setup
    if Orientation != "Upright":
        heading = 180
        xcor = coord-50
        ycor = 170
    else:
        heading = 0
        xcor = coord +50
        ycor = -175

    goto(xcor,ycor)
    setheading(heading)
    fillcolor('saddlebrown')
    color('saddlebrown')
    begin_fill()
    pendown()
    forward(50)
    right(90)
    forward(20)
    right(90)
    forward(50)
    right(90)
    forward(20)
    penup()
    end_fill()

def drawPanel1(Orientation,coord):  #Function for drawing panel 1, Gives coordinates for stars and trees.
    drawBackground(coord)
    drawMoon(Orientation,coord)
    drawStars(Orientation,coord,[-60,-10,15,38,53,92,34],[64,59,185,84,27,184,200])
    drawGround(Orientation,coord)
    drawTrees(Orientation,coord,[2,0,58,-50,-80,-34,34,53,-59],[-70,-236,-90,-60,-233,-225,-124,-203,-157])

def drawPanel2(Orientation,coord):  #Function for drawing panel 2, Gives coordinates for stars and trees.
    drawBackground(coord)
    drawGround(Orientation,coord)
    drawStars(Orientation,coord,[-92,8,-76,45,7,63,89,-69,50,74],[10,132,179,65,208,211,139,109,86,200,220])
    drawTrees(Orientation,coord,[68,-57,48,-73,0,-39,-8,-10,-50],[-22,-153,-154,-43,-114,-56,-28,-190,-240])
    drawFlameLHS(Orientation,coord)
    drawLogfireLHS(Orientation,coord)

def drawPanel3(Orientation,coord):  #Function for drawing panel 3, Gives coordinates for stars and trees.
    drawBackground(coord)
    drawGround(Orientation,coord)
    drawStars(Orientation,coord,[51,-45,62,-65,-87,6,48,79,-70,-36],[142,189,48,179,120,168,183,46,47,99])
    drawTrees(Orientation,coord,[8,46,40,-69,11,-68,-25,-23,-33],[-102,-49,-157,-162,-187,-82,-42,-160,-243])
    drawFlameRHS(Orientation,coord)
    drawLogfireRHS(Orientation,coord)

def drawPanel4(Orientation,coord):  #Function for drawing panel 4, Gives coordinates for stars and trees.
    drawBackground(coord)
    drawGround(Orientation,coord)
    drawStars(Orientation,coord,[-9245,87,-11,-28,-37,43,-54,-67,23],[10,165,187,110,85,143,87,199,199])
    drawTrees(Orientation,coord,[78,34,57,74,-12,-54,-65,-67,23],[-219,-92,-23,-132,-155,-177,-102,-223,-210,-250])

def PasteUp(DataSet):
    for number in range(2,6):
        sheet = data_sets[DataSet][number-1][0] #Determine which sheet is selected
        orientation = data_sets[DataSet][number-1][2]   #Determine the intended orientation of the pasted sheet
        
        #Centred X coordinates for each location
        if data_sets[DataSet][number-1][1]=='Location 1':
            location = -300
        elif data_sets[DataSet][number-1][1]=='Location 2':
            location = -100
        elif data_sets[DataSet][number-1][1]=='Location 3':
            location = 100
        elif data_sets[DataSet][number-1][1]=='Location 4':
            location = 300
            
        #Pasteup the corresponding panel for the sheet value.
        if sheet == "Sheet A":
            drawPanel1(orientation,location)
        elif sheet == "Sheet B":
            drawPanel2(orientation,location)
        elif sheet == "Sheet C":
            drawPanel3(orientation,location)
        elif sheet == "Sheet D":
            drawPanel4(orientation,location)

    #Part B - Graffiti
    if data_sets[DataSet][0] == "X":

        #Setup
        pensize(30)
        color("cyan")
        setheading(0)

        #L
        goto(-250,100)
        pendown()
        goto(-240,-100)
        left(3)
        forward(125)
        penup()

        #H
        goto(-50,130)
        pendown()
        goto(-50,-120)
        penup()
        goto(50,127)
        pendown()
        goto(50,-112)
        goto(50,20)
        setheading(192)
        forward(140)
        penup()

        #B
        goto(200,118)
        pendown()
        goto(187,-118)
        setheading(0)
        circle(70,130)
        setheading(0)
        circle(50,180)
   
# Paste the sheets onto the billboard as per the provided data set


#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your billboard.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the centre points of each sheet on the backing
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with one that describes the image
# ***** displayed on your billboard when the sheets are pasted
# ***** correctly
title("Night in a Forest")

### Call the student's function to display the billboard
### ***** Change the number in the argument to this function
### ***** to test your code with a different data set

PasteUp(47)     #Specifiy data_set and will paste parts in correct location and orientation

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#

