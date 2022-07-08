
#its not efficient but it works
def getColor(color):
    # assign entered color to an integer 1 - 13
        if color == '10':
            colorNum = 'white'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '20':
            colorNum = 'yellow'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '30':
            colorNum = 'lt grey'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '40':
            colorNum = 'weatherwood'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '50':
            colorNum = 'dk grey'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '60':
            colorNum = 'lime green'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '70':
            colorNum = 'aruba blue'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '80':
            colorNum = 'turf green'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '90':
            colorNum = 'cherrywood'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '11':
            colorNum = 'cardinal red'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '12':
            colorNum = 'patriot blue'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '13':
            colorNum = 'brown'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '14':
            colorNum = 'black'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
    #quit if error
        else:
            print("Number not listed as a color, check lot number")

def getBoardSize(boardSize):
  
        if boardSize == '50':
            boardNum = '1/2x8'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '51':
            boardNum = '3/4x1-3/4'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '52':
            boardNum = '3/4x2-5/8'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '53':
            boardNum = '3/4x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '54':
            boardNum = '3/4x5-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '55':
            boardNum = '1x5-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '56':
            boardNum = '1-1/8x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '57':
            boardNum = '1-1/2x1-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '58':
            boardNum = '1-1/2x2-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '59':
            boardNum = '1-1/2x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '60':
            boardNum = '1-1/2x5-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '61':
            boardNum = '1-1/2x9-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '62':
            boardNum = '2-1/2x2-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '63':
            boardNum = '3-1/2x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        else:
            print("The board number is incorrect, check lot number")

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

def getLotNum():
    i = 1
    while i == 1:
        lotNum = input("Please input lot number: ")
        #add 0x for hex 
        lotNumAdj = "0x" + lotNum
        #convert to integer
        lotNumInt = int(lotNumAdj, 16)
        #print(lotNumInt)  
#converts back to hex -disabled
        #lotHex = hex(lotNumInt)
        #print(lotHex)
        i = 0
        return lotNumInt

def getSplit(lotNum):
    if len(lotNum) == 12:
        string = lotNum
        #get first two numbers for color
        color = string[0:2]
        #remove color numbers (2) from string
        colorSize = string[2:]
        #get first two numbers for size
        size = colorSize[0:2]
        #remove size numbers (2) from string
        stringSize = colorSize[2:]
        #get line number (1) from string
        line = stringSize[0:1]
        #remove line number from string
        lineSize = stringSize[1:]
        #get date numbers (4) from string
        date = lineSize[0:4]
        #remove date numbers from string
        dateSize = lineSize[4:]
        #get pallet number (3) from string
        pallet = dateSize[0:3]

        #print(color, " ", size, " ", line, " ", date, " ", pallet )

        return color, size, line, date, pallet
    else:
        print("Lot number incorrect, please try again")
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
    #get decoded lot number as a string
    lotNum = str(getLotNum())
    splits = getSplit(lotNum)

#break tuple 'splits' into integers
    colorNum, sizeNum, lineNum, dateNum, palletNum = splits

    colorOut = getColor(colorNum)
    print('')
    boardOut = getBoardSize(sizeNum)
    print('')
    print('The line number is: ', lineNum)
    print('')
    print('The boards were made on the ', dateNum[0:2], 'th month of ', dateNum[-2:])
    print('')
    print('Pallet number of the month: ', palletNum)
    print('')

    #concatonate the strings into a single line
    #rawLotStr = colorNum + boardNum + lineNum + prodDateNum + palletNum
    #turn completed number into a integer
    #rawLotInt = int(rawLotStr)
    #convert integer into a hexidecimal
    #hexLot = hex(rawLotInt)
    #convert back into string to remove the 0x at beginning
    #hexLotStr = str(hexLot)
    #remove 0x
    #hexLotStr = hexLotStr[2:]

    #print(colorNum)
    #print(boardNum)
    #print(lineNum)
    #print(prodDateNum)
    #print(palletNum)

    #print("The full number is ", rawLotInt)
    #print('                 The Lot number is: ', hexLotStr)
    n = input("Press 1 to continue, anything else to exit: ")
    if n == "1":
        r = 1
    else:
        r = 0