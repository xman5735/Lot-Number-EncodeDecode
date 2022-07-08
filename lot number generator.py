
#its not efficient but it works
def getColor():
    i=0
    while i == 0:
        #ask for color input
        color = input('Input color or ? for options: ')
    # print options if requested
        if color == '?': 
            print("white, yellow, lt grey, weatherwood, dk grey, lime green, aruba blue, turf green, cherrywood, cardinal red, patriot blue, brown, black")

    # assign entered color to an integer 1 - 13
        if color == 'white':
            colorNum = 10
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'yellow':
            colorNum = 20
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'lt grey':
            colorNum = 30
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'weatherwood':
            colorNum = 40
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'dk grey':
            colorNum = 50
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'lime green':
            colorNum = 60
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'aruba blue':
            colorNum = 70
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'turf green':
            colorNum = 80
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'cherrywood':
            colorNum = 90
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'cardinal red':
            colorNum = 11
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'patriot blue':
            colorNum = 12
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'brown':
            colorNum = 13
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
        elif color == 'black':
            colorNum = 14
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum
    #quit if error
        else:
            print("Please enter a correct color")

def getBoardSize():
    i = 0
    while i == 0:
            
        #ask for board size
        boardSize = input('Enter Board size or ? for options: ')
        #output the availible options for board size    
        if boardSize == '?':
            print("1/2x8, 3/4x1-3/4, 3/4x2-5/8, 3/4x3-1/2, 3/4x5-1/2, 1x5-1/2, 1-1/8x3-1/2, 1-1/2x1-1/2, 1-1/2x2-1/2, 1-1/2x3-1/2, 1-1/2x5-1/2, 1-1/2x9-1/2, 2-1/2x2-1/2, 3-1/2x3-1/2")
        #assign entered board size a value over 50. previous numbers are for color    
        elif boardSize == '1/2x8':
            boardNum = 50
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '3/4x1-3/4':
            boardNum = 51
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '3/4x2-5/8':
            boardNum = 52
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '3/4x3-1/2':
            boardNum = 53
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '3/4x5-1/2':
            boardNum = 54
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '1x5-1/2':
            boardNum = 55
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '1-1/8x3-1/2':
            boardNum = 56
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '1-1/2x1-1/2':
            boardNum = 57
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '1-1/2x2-1/2':
            boardNum = 58
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            return boardNum
            i=1
        elif boardSize == '1-1/2x3-1/2':
            boardNum = 59
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '1-1/2x5-1/2':
            boardNum = 60
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '1-1/2x9-1/2':
            boardNum = 61
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '2-1/2x2-1/2':
            boardNum = 62
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        elif boardSize == '3-1/2x3-1/2':
            boardNum = 63
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            return boardNum
        else:
            print("Please enter a correct board size")

def getLineNumber():
    i=0
    while i==0:        
    #ask for line number
        lineNum = input('Enter line number the board extruded on or ? or options: ')
        lineNumInt = int(lineNum)
    # print options if asked for    
        if lineNum == '?':
            print("1, 2, 3, 4, 5, 6")
    #if equal to existing line, saVE. This needs some efficiency work    
        if (lineNumInt <= 6):
            i=1
            #lineNum  = int(lineNum)
            #return line number as int and verify line
            print("The board was extruded on line ", lineNum)
            return lineNum
        else:
            print("Please enter a correct line number.")

def getProdDate():
    i=0
    while i==0:
    #ask for production date in month and year
        proDate = input('Enter month and year of production date in format mmyy: ')
    #check if string is 4 digits
        if len(proDate) == 4:
            i=1
            #return production date as int and verify
            print("The board was produced on ", proDate)
            return proDate
        else:
            print('Please enter the correct date format')


def getPalletNum():
    i=0
    while i==0:
    #ask for the pallet number this month
        palletNum = input('Please enter the pallet number in three digits. Note that the number rolls over each month: ')
        if len(palletNum) <= 3:
            i=1
            #return pallet number and confirm pallet number
            print("THe pallet number is", palletNum)
            return(palletNum)
        else:
            print("Please enter the correct pallet number in 3 digits")

r=1
while r == 1:
    #ensure the values are in strong so they cannot be added
    print(r"""
               ___                       ___             ___ _           _   _          
              / _ \_ __ ___  ___ _ __   / __\____  __   / _ \ | __ _ ___| |_(_) ___ ___ 
             / /_\/ '__/ _ \/ _ \ '_ \ / _\/ _ \ \/ /  / /_)/ |/ _` / __| __| |/ __/ __|
            / /_\\| | |  __/  __/ | | / / | (_) >  <  / ___/| | (_| \__ \ |_| | (__\__ \
            \____/|_|  \___|\___|_| |_\/   \___/_/\_\ \/    |_|\__,_|___/\__|_|\___|___/
                """)
    colorNum = str(getColor())
    print('')
    boardNum = str(getBoardSize())
    print('')
    lineNum = str(getLineNumber())
    print('')
    prodDateNum = str(getProdDate())
    print('')
    palletNum = str(getPalletNum())
    print('')

    #concatonate the strings into a single line
    rawLotStr = colorNum + boardNum + lineNum + prodDateNum + palletNum
    #turn completed number into a integer
    rawLotInt = int(rawLotStr)
    #convert integer into a hexidecimal
    hexLot = hex(rawLotInt)
    #convert back into string to remove the 0x at beginning
    hexLotStr = str(hexLot)
    #remove 0x
    hexLotStr = hexLotStr[2:]

    #print(colorNum)
    #print(boardNum)
    #print(lineNum)
    #print(prodDateNum)
    #print(palletNum)

    print("The full number is ", rawLotInt)
    print('                 The Lot number is: ', hexLotStr)
    n = input("Press 1 to continue, anything else to exit: ")
    if n == "1":
        r = 1
    else:
        r = 0