from datetime import date
from os.path import exists
from pathlib import Path
import os
from tkinter import Y
import xlsxwriter

charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ01234'

#its not efficient but it works
#functions to get data and change it into consistant form
def getColor():
    i=0
    while i == 0:
        #ask for color input
        color = input('Input color or ? for options: ')
        color = color.lower()
    # print options if requested
        if color == '?':
            print("white, yellow, lt grey, weathered wood, dk grey, lime green, aruba blue, turf green, cherry wood, cardinal red, patriot blue, tudor brown, black")

    # assign entered color to an integer 1 - 13
        if color == 'white':
            colorNum = '0001'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
        elif color == 'yellow':
            colorNum =  '0010'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
        elif color == 'lt grey':
            colorNum = '0011'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            color = 'Light Grey'
            return colorNum, color
        elif color == 'weathered wood':
            colorNum = '0100'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
        elif color == 'dk grey':
            colorNum = '0101'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            color = 'Dark Grey'
            return colorNum, color
        elif color == 'lime green':
            colorNum = '0110'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
        elif color == 'aruba blue':
            colorNum = '0111'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
        elif color == 'turf green':
            colorNum = '1000'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
        elif color == 'cherrywood':
            colorNum = '1001'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
        elif color == 'cardinal red':
            colorNum = '1010'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
        elif color == 'patriot blue':
            colorNum = '1011'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
        elif color == 'tudor brown':
            colorNum = '1100'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
        elif color == 'black':
            colorNum = '1101'
            #return color number to program and veify color
            print('The board color is set to ', color )
            i=1
            return colorNum, color
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
            boardNum = '0001'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '½ x 8'
            return boardNum, boardSize
        elif boardSize == '3/4x1-3/4':
            boardNum = '0010'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '¾ x 1 ¾'
            return boardNum, boardSize
        elif boardSize == '3/4x2-5/8':
            boardNum = '0011'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '¾ x 2 5/8'
            return boardNum, boardSize
        elif boardSize == '3/4x3-1/2':
            boardNum = '0100'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '¾ x 3 ½'
            return boardNum, boardSize
        elif boardSize == '3/4x5-1/2':
            boardNum = '0101'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '¾ x 5 ½'
            return boardNum, boardSize
        elif boardSize == '1x5-1/2':
            boardNum = '0110'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '1 x 5 ½'
            return boardNum, boardSize
        elif boardSize == '1-1/8x3-1/2':
            boardNum = '0111'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '1 ⅛ x 3 ½' 
            return boardNum, boardSize
        elif boardSize == '1-1/2x1-1/2':
            boardNum = '1000'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '1 ½ x 1 ½'
            return boardNum, boardSize
        elif boardSize == '1-1/2x2-1/2':
            boardNum = '1001'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i = 1
            boardSize = '1 ½ x 2 ½'
            return boardNum, boardSize
        elif boardSize == '1-1/2x3-1/2':
            boardNum = '1010'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '1 ½ x 3 ½'
            return boardNum, boardSize
        elif boardSize == '1-1/2x5-1/2':
            boardNum = '1011'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '1 ½ x 5 ½'
            return boardNum, boardSize
        elif boardSize == '1-1/2x9-1/2':
            boardNum = '1100'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '1 ½ x 9 ½'
            return boardNum, boardSize
        elif boardSize == '2-1/2x2-1/2':
            boardNum = '1101'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '2 ½ x 2 ½'
            return boardNum, boardSize
        elif boardSize == '3-1/2x3-1/2':
            boardNum = '1110'
            #Return number of choosen board size and verify size
            print('The selected board size is ', boardSize)
            i=1
            boardSize = '3 ½ x 3 ½'
            return boardNum, boardSize
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
            lineNum = bin(lineNumInt)[2:].zfill(3)
            return lineNum
        else:
            print("Please enter a correct line number.")

def getProdDate():
    i=0
    while i==0:
    #ask for production date in month and year
        proDate = input('Enter month and year of production date in format mmddyy: ')
    #check if string is 6 digits
        if len(proDate) == 6:
            #breakdown into parts
            month = proDate[0:2]
            proDateShred = proDate[2:]
            day = proDateShred[0:2]
            proDateShred = proDateShred[2:]
            year = proDateShred[0:2]
            #lazy nesting
            if int(day) <= 31:
                if int(month) <= 12:
                    #return production date as int and verify
                    print("The board was produced on ", proDate)
                    proDate = month + year
                    proDateInt = int(proDate)
                    proDate = bin(proDateInt)[2:].zfill(11)
                    return proDate, day, month, year
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
            palletNumInt = int(palletNum)
            palletNum = bin(palletNumInt)[2:].zfill(8)
            return(palletNum)
        else:
            print("Please enter the correct pallet number in 3 digits")

#functions to modify and create new data
def printToFile(color, size, line, prodDate, pallet, lot):
    #turn bin files back into usable data
    #line = '0b' + line
    line = int(line,2)
    #prodDate = '0b' + prodDate
    prodDate = int(prodDate,2)
    #pallet = '0b' + pallet
    pallet = int(pallet,2)

    line = str(line)
    prodDate = str(prodDate)
    pallet = str(pallet)
    #get date
    today = date.today()
    timeString = today.strftime("%m_%d_%y")
    
    #create text to write
    lines = (color, " ", size, " Line: ", line, " Date Produced: ", prodDate, " Pallet Number: ", pallet, "\nLot Number is: ", lot)
    #create the text file
    fileName = "lot_numbers_" + timeString + ".txt"
    #create link to users documents folder
    #path = "/home"
    #loca = os.path.join(path, "User/Documents", fileName)
    loca = Path('C:\Temp')
    fileStr = 'C:\Temp' + fileName
    fileLoca = Path(fileStr)
    #print(fileLoca)
    #loca = Path('~/Documents')
    #print(loca)
    #check if direcctory exists
    if loca.is_dir():
        if os.path.exists(fileLoca) is True:
            #if exists, append new information
            with open (loca.joinpath(fileName), 'a') as f:
                f.write("\n")
                f.writelines(lines)
                f.write("\n")
            print('File appended')
            return pallet, prodDate
        if os.path.exists(fileLoca) is False:
            #if does not exist, create the file
            with open (loca.joinpath(fileName), 'a') as f:
                f.write("\n")
                f.writelines(lines)
                f.write("\n")
            print('File: ', fileName, ' created')
            return pallet, prodDate
    else:
        print('Directory does not exist')

def encode(bin_string):
    # Split the string of 1s and 0s into lengths of 5.
    chunks = [bin_string[i:i+5] for i in range(0, len(bin_string), 5)]
    # Store the length of the last chunk so that we can add that as the last bit
    # of data so that we know how much to pad the last chunk when decoding.
    last_chunk_length = len(chunks[-1])
    # Convert each chunk from binary into a decimal
    decimals = [int(chunk, 2) for chunk in chunks]
    # Add the length of our last chunk to our list of decimals.
    decimals.append(last_chunk_length)
    # Produce an ascii string by using each decimal as an index of our charset.
    ascii_string = ''.join([charset[i] for i in decimals])

    return ascii_string 

#create excel mile to print
def printOut(colorString, palletNum, boardString, encodedLot, day, month, year):
    colorString = colorString.upper()
    #create workbook
    workbookName = colorString + "_" + palletNum + ".xlsx"
    workbookPath = 'C:/Temp/' + workbookName
    workbook = xlsxwriter.Workbook(workbookPath)
    #save workbook in specific location
    worksheet = workbook.add_worksheet()
    worksheet.set_margins(left=0.25, right=0.25)
    worksheet.set_column(0, 0, 42)
    worksheet.set_column(1, 1, 10)
    worksheet.set_column(2, 2, 42)
    worksheet.set_row(0, 105)
    worksheet.set_row(1, 140)
    worksheet.set_row(2, 85)
     # Add a bold format to use to highlight cells.
    
    size1 = workbook.add_format()
    size2 = workbook.add_format()
    size3 = workbook.add_format()
    size4 = workbook.add_format()
    size1.set_font_size(80)
    if colorString == 'WEATHERED WOOD':
        size2.set_font_size(65)
    if colorString != 'WEATHERWOOD':
        size2.set_font_size(90)
    size3.set_font_size(36)
    size4.set_font_size(36)
    size3.set_underline(1)
    size4.set_underline(1)
    size1.set_align('center')
    size1.set_align('vcenter')
    size2.set_align('center')
    size2.set_align('vcenter')
    size3.set_align('left')
    size4.set_align('right')
    #size1.set_bold()
    size3.set_bold()
    size4.set_bold()

    #copy a second time
    worksheet.set_row(3, 40)
    worksheet.set_row(4, 105)
    worksheet.set_row(5, 140)
    worksheet.set_row(6, 85)

    #format dimensiions line
    dims = "____ - " + boardString
    #format Color
    color = colorString
    #format date
    date = "Date: " + str(month) + '/' + str(day) + "/" + str(year)  
    #format Skid lot
    lot = "Lot #: " + encodedLot
    worksheet.write('B1', dims, size1)
    worksheet.write('B2', color, size2)
    worksheet.write('A3', date, size3)
    worksheet.write('C3', lot, size4)
    worksheet.write('B5', dims, size1)
    worksheet.write('B6', color, size2)
    worksheet.write('A7', date, size3)
    worksheet.write('C7', lot, size4)

    workbook.close()
#Main loop
r=1
while r == 1:
    print(r"""
               ___                       ___             ___ _           _   _          
              / _ \_ __ ___  ___ _ __   / __\____  __   / _ \ | __ _ ___| |_(_) ___ ___ 
             / /_\/ '__/ _ \/ _ \ '_ \ / _\/ _ \ \/ /  / /_)/ |/ _` / __| __| |/ __/ __|
            / /_\\| | |  __/  __/ | | / / | (_) >  <  / ___/| | (_| \__ \ |_| | (__\__ \
            \____/|_|  \___|\___|_| |_\/   \___/_/\_\ \/    |_|\__,_|___/\__|_|\___|___/
                """)
   #get data
    colorBin, colorString = getColor()
    print('')
    boardBin, boardString = getBoardSize()
    print('')
    lineBin = getLineNumber()
    print('')
    prodDateBin, day, month, year = getProdDate()
    print('')
    palletBin = getPalletNum()
    print('')
    
    
    #concatonate the strings into a single line
    rawLotStr = colorBin + boardBin + lineBin + prodDateBin + palletBin
    #print(rawLotStr)
    #make sure it is 31 digits
    #rawLotStr.rjust(31, '0')
    #encode
    encodedLot = encode(rawLotStr)
    print('Lot Number: ' + encodedLot)



    #print results to file
    palletNum, prodDateS = printToFile(colorString, boardString, lineBin, prodDateBin, palletBin, encodedLot)
    
    #print?
    printQuestion = input("Do you want to print label? Y/N: ")
    printQuestion = printQuestion.lower()
    if printQuestion == 'y':
        printOut(colorString, palletNum, boardString, encodedLot, day, month, year)
        print("File located at C:/Temp/" )
    #Ask to contiue or quit
    n = input("Press 1 to continue, anything else to exit: ")
    if n == "1":
        r = 1
    else:
        r = 0
