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


['X', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],


number = []

for number in range(4):
    sheet = data_sets[number][1][0]
    orientation = data_sets[number][1][2]

    if data_sets[number][1][1]=='Location 1':
        location = -300
    elif data_sets[number][1][1]=='Location 2':
        location = -100
    elif data_sets[number][1][1]=='Location 3':
        location = 100
    elif data_sets[number][1][1]=='Location 4':
        location = 300
        
    if sheet == "Sheet A":
        drawPanel1(orientation,location)
    elif sheet == "Sheet B":
        drawPanel2(orientation,location)
     elif sheet == "Sheet C":
        drawPanel3(orientation,location)
     elif sheet == "Sheet D":
        drawPanel4(orientation,location)
