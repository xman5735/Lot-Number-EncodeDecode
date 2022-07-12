charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ01234'

#its not efficient but it works
def getColor(color):
    # assign entered color to an integer 1 - 13
        if color == '0001':
            colorNum = 'white'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '0010':
            colorNum = 'yellow'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '0011':
            colorNum = 'lt grey'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '0100':
            colorNum = 'weatherwood'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '0101':
            colorNum = 'dk grey'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '0110':
            colorNum = 'lime green'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '0111':
            colorNum = 'aruba blue'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '1000':
            colorNum = 'turf green'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '1001':
            colorNum = 'cherrywood'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '1010':
            colorNum = 'cardinal red'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '1011':
            colorNum = 'patriot blue'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '1100':
            colorNum = 'brown'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '1101':
            colorNum = 'black'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
    #quit if error
        else:
            print("Number not listed as a color, check lot number")

def getBoardSize(boardSize):
  
        if boardSize == '0001':
            boardNum = '1/2x8'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '0010':
            boardNum = '3/4x1-3/4'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '0011':
            boardNum = '3/4x2-5/8'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '0100':
            boardNum = '3/4x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '0101':
            boardNum = '3/4x5-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '0110':
            boardNum = '1x5-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '0111':
            boardNum = '1-1/8x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '1000':
            boardNum = '1-1/2x1-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '1001':
            boardNum = '1-1/2x2-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '1010':
            boardNum = '1-1/2x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '1011':
            boardNum = '1-1/2x5-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '1100':
            boardNum = '1-1/2x9-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '1101':
            boardNum = '2-1/2x2-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '1110':
            boardNum = '3-1/2x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        else:
            print("The board number is incorrect, check lot number")

def getLotNum():
    i = 1
    while i == 1:
        lotNumBin = input("Please input lot number: ")
        i = 0
        return lotNumBin

def getSplit(lotNum):
    if len(lotNum) == 30:
        string = lotNum
        #get first 4 numbers for color
        color = string[0:4]
        #remove color numbers (4) from string
        colorSize = string[4:]
        #get first 4 numbers for size
        size = colorSize[0:4]
        #remove size numbers (4) from string
        stringSize = colorSize[4:]
        #get line number (3) from string
        line = stringSize[0:3]
        #remove line number from string
        lineSize = stringSize[3:]
        #get date numbers (11) from string
        date = lineSize[0:11]
        #remove date numbers from string
        dateSize = lineSize[11:]
        #get pallet number (8) from string
        pallet = dateSize[0:8]

        #print(color, " ", size, " ", line, " ", date, " ", pallet )

        return color, size, line, date, pallet
    else:
        print("Lot number incorrect, please try again")

def decode(ascii_string):
    # Convert each character to a decimal using its index in the charset.
    decimals = [charset.index(char) for char in ascii_string]
    # Take last decimal which is the final chunk length, and the second to last
    # decimal which is the final chunk, and keep them for later to be padded
    # appropriately and appended.
    last_chunk_length, last_decimal = decimals.pop(-1), decimals.pop(-1)
    # Take each decimal, convert it to a binary string (removing the 0b from the
    # beginning, and pad it to 6 digits long.
    bin_string = ''.join([bin(decimal)[2:].zfill(5) for decimal in decimals])
    # Add the last decimal converted to binary padded to the appropriate length
    bin_string += bin(last_decimal)[2:].zfill(last_chunk_length)

    return bin_string

#main loop
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
    #get decoded lot number
    lotNumBin = getLotNum()
    #convert back to binary
    lotNum = decode(lotNumBin)
    #print(lotNum)
    #shred binary into individual parts
    splits = getSplit(lotNum)

#break tuple 'splits' into integers
    colorNum, sizeNum, lineNum, dateNum, palletNum = splits

    #turn bin into decimal string
    dateNum = int(dateNum,2)
    dateNum = str(dateNum)
    if len(dateNum) != 4:
        dateNum = '0' + dateNum
    palletNum = int(palletNum, 2)
    palletNum = str(palletNum)

    #put month into proper format

    colorOut = getColor(colorNum)
    print('')
    boardOut = getBoardSize(sizeNum)
    print('')
    print('The line number is: ', int(lineNum,2))
    print('')
    print('The boards were made on the ', dateNum[0:2], 'th month of', dateNum[-2:])
    print('')
    print('Pallet number of the month: ', palletNum)
    print('')

    #ask to continue
    n = input("Press 1 to continue, anything else to exit: ")
    if n == "1":
        r = 1
    else:
        r = 0