
charset = 'ABCDEFGHJKLMNPQRSTVWXYZ23456789#!'

#its not efficient but it works
#should be updated to modular style
def getColor(color):
    # assign entered color to an integer 1 - 13
        if color == '00001':
            colorNum = 'White'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '00010':
            colorNum = 'Yellow'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '00011':
            colorNum = 'Light Grey'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '00100':
            colorNum = 'Weathered Wood'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '00101':
            colorNum = 'Dark Grey'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '00110':
            colorNum = 'Lime Green'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '00111':
            colorNum = 'Aruba Blue'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '01000':
            colorNum = 'Turf Green'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '01001':
            colorNum = 'Cherry Wood'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '01010':
            colorNum = 'Cardinal Red'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '01011':
            colorNum = 'Patriot Blue'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '01100':
            colorNum = 'Brown'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
        elif color == '01101':
            colorNum = 'Black'
            #return color number to program and veify color
            print('The board color is ', colorNum )
            i=1
            return colorNum
    #quit if error
        else:
            print("Number not listed as a color, check lot number")

#should be updated to modular design
def getBoardSize(boardSize):
  
        if boardSize == '00001':
            boardNum = '1/2x8'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '00010':
            boardNum = '3/4x1-3/4'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '00011':
            boardNum = '3/4x2-5/8'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '00100':
            boardNum = '3/4x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '00101':
            boardNum = '3/4x5-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '00110':
            boardNum = '1x5-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '00111':
            boardNum = '1-1/8x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '01000':
            boardNum = '1-1/2x1-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '01001':
            boardNum = '1-1/2x2-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '01010':
            boardNum = '1-1/2x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '01011':
            boardNum = '1-1/2x5-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '01100':
            boardNum = '1-1/2x9-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '01101':
            boardNum = '2-1/2x2-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '01110':
            boardNum = '3-1/2x3-1/2'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        elif boardSize == '01111':
            boardNum = 'Bench Frame'
            #Return number of choosen board size and verify size
            print('The board size is ', boardNum)
            i=1
            return boardNum
        else:
            print("The board number is incorrect, check lot number")

#if length of lot number changes (excluding -x) then update here
def getLotNum():
    i = 1
    while i == 1:
        lotNumBin = input("Please input lot number: ")
        #removes -x from lot number
        palletNum = lotNumBin[-1:]
        lotNumBin = lotNumBin[:-2]
        #update here
        if len(lotNumBin) == 5:
            i = 0
            return lotNumBin, palletNum
        else:
            print("Please enter a correct lot number.")

#if decimal amount changes, update here (and then the affected 'get')
def getSplit(lotNum):
    if len(lotNum) == 25:
        string = lotNum
        #get first 4 numbers for color
        color = string[0:5]
        #remove color numbers (4) from string
        colorSize = string[5:]
        #get first 4 numbers for size
        size = colorSize[0:5]
        #remove size numbers (4) from string
        stringSize = colorSize[5:]
        #get line number (3) from string
        line = stringSize[0:4]
        #remove line number from string
        lineSize = stringSize[4:]
        #get date numbers (11) from string
        date = lineSize[0:11]
        #remove date numbers from string
        dateSize = lineSize[11:]

        #print(color, " ", size, " ", line, " ", date, " ", pallet )

        return color, size, line, date
    else:
        print("Lot number incorrect, please try again")

#uncomment ## lines if binary string grows. it is maxed. Lot will increase by 3 digits
def decode(ascii_string):
    ascii_string = ascii_string.upper()
    # Convert each character to a decimal using its index in the charset.
    decimals = [charset.index(char) for char in ascii_string]
    # Take last decimal which is the final chunk length, and the second to last
    # decimal which is the final chunk, and keep them for later to be padded
    # appropriately and appended.
    ##last_chunk_length, last_decimal = decimals.pop(-1), decimals.pop(-1)
    # Take each decimal, convert it to a binary string (removing the 0b from the
    # beginning, and pad it to 6 digits long.
    bin_string = ''.join([bin(decimal)[2:].zfill(5) for decimal in decimals])
    # Add the last decimal converted to binary padded to the appropriate length
    ##bin_string += bin(last_decimal)[2:].zfill(last_chunk_length)
    print(bin_string)
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
    lotNumBin, palletEnd = getLotNum()
    #convert back to binary
    lotNum = decode(lotNumBin)
    #print(lotNum)
    #shred binary into individual parts
    splits = getSplit(lotNum)

#break tuple 'splits' into integers
    colorNum, sizeNum, lineNum, dateNum = splits

    #turn bin into decimal string
    dateNum = int(dateNum,2)
    dateNum = str(dateNum)
    #increase to 6 if full date is to be included
    if len(dateNum) != 4:
        dateNum = '0' + dateNum
    #palletNum = int(palletNum, 2)
    #palletNum = str(palletNum)

    #put month into proper format

    colorOut = getColor(colorNum)
    print('')
    boardOut = getBoardSize(sizeNum)
    print('')
    print('The line number is: ', int(lineNum,2))
    print('')
    print('The boards were made on the month: ', dateNum[0:2], ' and the day', dateNum[-2:])
    print('Exact year created will be on label and records')
    print('')
    print('Pallet number: ', palletEnd)
    print('')

    #ask to continue
    n = input("Press 1 to continue, anything else to exit: ")
    if n == "1":
        r = 1
    else:
        r = 0