import datetime
import os
from calendar import weekday
from os.path import exists
from pathlib import Path
from tkinter import Y

import xlsxwriter

#this is the values that the binary will be encoded into. make sure string on decoder is that same. 
charset = 'ABCDEFGHJKLMNPQRSTVWXYZ23456789#!'

#its now more efficient and it works
#functions to get data and change it into consistant form

#can handle up to 31 colors before another binary decimal is needed. 
def getColor():
    i=0
    while i == 0:
        j = 0
        while j == 0: 
            print(r"""
                1. White        4. Weathered Wood   7. Aruba Blue   10. Cardinal Red    13. Black

                -----------------------------------------------------------------------------------

                2. Yellow       5. Dark Grey        8. Turf Green   11. Patriot Blue    

                -----------------------------------------------------------------------------------
                
                3. Light Grey   6. Lime Green       9. Cherry Wood  12. Tudor Brown   
                """)        
            #ask for color input
            color = input('Input color number or ? for options: ')
            print('*')


    # print options if requested
          

            if color == '?':
                print("white, yellow, lt grey, weathered wood, dk grey, lime green, aruba blue, turf green, cherry wood, cardinal red, patriot blue, tudor brown, black")
                j=1

        # assign entered color to an integer 1 - 13
            if color == '1':
                colorNum = bin(int(color))
                colorName = 'White'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '2':
                colorNum =  bin(int(color))
                colorName = 'Yellow'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '3':
                colorNum = bin(int(color))
                colorName = 'Light Grey'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '4':
                colorNum = bin(int(color))
                colorName = 'Weathered Wood'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '5':
                colorNum = bin(int(color))
                colorName = 'Dark Grey'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '6':
                colorNum = bin(int(color))
                colorName = 'Lime Green'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '7':
                colorNum = bin(int(color))
                colorName = 'Aruba Blue'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '8':
                colorNum = bin(int(color))
                colorName = 'Turf Green'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '9':
                colorNum = bin(int(color))
                colorName = 'Cherry wood'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '10':
                colorNum = bin(int(color))
                colorName = 'Cardinal Red'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '11':
                colorNum = bin(int(color))
                colorName = 'Patriot Blue'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '12':
                colorNum = bin(int(color))
                colorName = 'Tudor Brown'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            elif color == '13':
                colorNum = bin(int(color))
                colorName = 'Black'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

        #quit if error
            else:
                print("Please enter a correct color")
                j = 0

        colorNum = str(colorNum)
        #remove 0b from front of string. result of binary conversion
        colorNum = colorNum[2:]
        colorNum = colorNum.zfill(5)
        i = 1
        return colorNum, colorName
        
#Can handle 31 board sizes until update needed again 
def getBoardSize():
    #create loop to run until correct values entered
    i = 0
    while i == 0:
        j = 0
        while j == 0:    
            #ask for board size
            #boardSize = input('Enter Board size or ? for options: ')
            print(r"""
                1. 1/2 x 8        4. 3/4 x 3-1/2    7. 1-1/8 x 3-1/2    10. 1-1/2 x 3-1/2   13. 2-1/2 x 2-1/2

                -----------------------------------------------------------------------------------

                2. 3/4 x 1-3/4    5. 3/4 x 5-1/2    8. 1-1/2 x 1-1/2    11. 1-1/2 x 5-1/2   14. 3-1/2 x 3-1/2

                -----------------------------------------------------------------------------------

                3. 3/4 x 2-5/8    6. 1 x 5-1/2      9. 1-1/2 x 2-1/2    12. 1-1/2 x 9-1/2   15. Bench Frame
                """)
            boardDim = input('Select the Board Size by typing 1-15: ')
            print('*')
            #convert string to integer for comparison
            boardDim = int(boardDim)
            #check that board is a actual choice, give default if not for loop
            if boardDim >= 16:
                boardDim = 100
            #convert int to string
            boardDim = str(boardDim)
            #create new variable so that boardDim can be called separatly 
            boardSize = boardDim
        
            #output the availible options for board size    
            if boardSize == '?':
                print("1/2x8, 3/4x1-3/4, 3/4x2-5/8, 3/4x3-1/2, 3/4x5-1/2, 1x5-1/2, 1-1/8x3-1/2, 1-1/2x1-1/2, 1-1/2x2-1/2, 1-1/2x3-1/2, 1-1/2x5-1/2, 1-1/2x9-1/2, 2-1/2x2-1/2, 3-1/2x3-1/2, Bench Frame")
            #assign entered board size a value   
            elif boardSize == '1':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '½ x 8'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '2':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '¾ x 1 ¾'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '3':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '¾ x 2 5/8'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '4':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '¾ x 3 ½'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '5':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '¾ x 5 ½'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '6':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '1 x 5 ½'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '7':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '1 1-8 x 3 ½' 
                print('The selected board size is 1 1/8 x 3 ½')
                j=1
                
            elif boardSize == '8':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '1 ½ x 1 ½'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '9':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '1 ½ x 2 ½'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '10':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '1 ½ x 3 ½'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '11':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '1 ½ x 5 ½'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '12':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '1 ½ x 9 ½'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '13':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '2 ½ x 2 ½'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '14':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = '3 ½ x 3 ½'
                print('The selected board size is ', boardSize)
                j=1
            
            elif boardSize == '15':
                boardNum = bin(int(boardSize))
                #Return number of choosen board size and verify size
                boardSize = 'Bench Frame'
                print('The selected board size is ', boardSize)
                j=1
                
            elif boardSize == '100100':
                print("Please enter a correct board size selection")

            else:
                print("Entered board selection does not match any produced boards")

        boardNum = str(boardNum)
        #remove 0b from front of string. result of binary conversion
        boardNum = boardNum[2:]
        boardNum = boardNum.zfill(5)
        #print(boardNum + ' ' + boardSize)
        i = 1
        return boardNum, boardSize

#After 15, will need to increase zfill and decimal size.
def getLineNumber():
    i=0
    while i==0:        
    #ask for line number
        lineNum = input('Enter line number the board extruded on or ? or options: ')
        print('*')
        lineNumInt = int(lineNum)
    # print options if asked for    
        if lineNum == '?':
            #update here for extra lines (1/2)
            print("1 - 15")
    #if equal to existing line, saVE. This needs some efficiency work  
    # update here for extra lines (2/2)   
        if (lineNumInt <= 15):
            i=1
            #lineNum  = int(lineNum)
            #return line number as int and verify line
            print("The board was extruded on line ", lineNum)
            #remove 0b from binary conversion
            lineNum = bin(lineNumInt)[2:].zfill(4)
            return lineNum
        else:
            print("Please enter a correct line number.")

#wont need update until 2100
def getProdDate():
    i=0
    while i==0:
    #ask for production date in month and year
        proDate = input('Enter month and year of production date in format mmddyy: ')
        print('*')
        howMany = input("How many more pallets of this type do you want to create? (1,2,3,4...):" )
        print('*')
    #check if string is 6 digits
        if len(proDate) == 6:
            #breakdown into parts
            month = proDate[0:2]
            proDateShred = proDate[2:]
            day = proDateShred[0:2]
            proDateShred = proDateShred[2:]
            year = proDateShred[0:2]
            #lazy nesting
            #check if under 32 days
            if int(day) <= 31:
                #check if under 13 months
                if int(month) <= 12:
                    #return production date as int and verify
                    print("The board was produced on ", proDate)
                    proDate = month + day
                    proDateInt = int(proDate)
                    #remove the 0x and make sure the string is 17 chaRACTERS
                    #splitting into seperate sections allows a 1 decimal saving (16) so leaving it.
                    proDate = bin(proDateInt)[2:].zfill(11)
                    return proDate, day, month, year, howMany
        else:
            print('Please enter the correct date format')

#if more than 9 pallets are made in a day, needs to update length. This is unlikely
def getPalletNum():
    i=0
    while i==0:
    #ask for the pallet number this month
        palletNum = input('Please enter the pallet number with 1. Example: 2 for the 2nd pallet of that day: ')
        print('*')
        #update here for more than 7 pallets (1/2)
        if len(palletNum) <= 1:
            i=1
            #return pallet number and confirm pallet number
            print("The pallet number is", palletNum)
            return(palletNum)
        else:
            print("Please enter the correct pallet number. Note that the number resets daily.")

#functions to modify and create new data. Appends all data to text file in Temp folder of C drive
def printToFile(color, size, line, prodDate, pallet, lot):
    #turn bin files back into usable data
    #line = '0b' + line
    line = int(line,2)
    #prodDate = '0b' + prodDate
    prodDate = int(prodDate,2)
    #pallet = '0b' + pallet
    #pallet = int(pallet,2)

    line = str(line)
    prodDate = str(prodDate)
    pallet = str(pallet)
    #get date
    today = datetime.date.today()
    timeString = today.strftime("%m_%d_%y")
    
    #create text to write
    lines = (color, " ", size, " Line: ", line, " Date Produced: ", prodDate, " Pallet Number: ", pallet, "\nLot Number is: ", lot)
    #create the text file
    fileName = "lot_numbers_" + timeString + ".txt"
    #create link to users documents folder
    #path = "/home"
    #loca = os.path.join(path, "User/Documents", fileName)
    loca = Path('C:\Temp\LotLog')
    fileStr = 'C:\TempLotLog' + fileName
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
            print('File: ', fileName, ' updated')
            return pallet, prodDate
    else:
        print('Directory does not exist')

#5 = 31 digits. 6 = 63 digits for charset 
#if the amount of decimals increases, uncomment ## items
def encode(bin_string):
    # Split the string of 1s and 0s into lengths of 5.
    chunks = [bin_string[i:i+5] for i in range(0, len(bin_string), 5)]
    # Store the length of the last chunk so that we can add that as the last bit
    # of data so that we know how much to pad the last chunk when decoding.
    ##last_chunk_length = len(chunks[-1])
    # Convert each chunk from binary into a decimal
    decimals = [int(chunk, 2) for chunk in chunks]
    # Add the length of our last chunk to our list of decimals.
    ##decimals.append(last_chunk_length)
    # Produce an ascii string by using each decimal as an index of our charset.
    ascii_string = ''.join([charset[i] for i in decimals])

    return ascii_string 

#create excel file to print label
#poorly commented, follow xlsxwriter documentation
def printOut(colorString, palletNum, boardString, encodedLot, makeDate):
    colorString = colorString.upper()
    #create workbook
    if boardString == '¾ x 2 5/8':
        workbookName = colorString + '_¾ x 2 5-8_' + palletNum + ".xlsx"
    else:
        workbookName = colorString + "_" + boardString + '_' + palletNum + ".xlsx"
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
    #modify to make text smaller for lengths that are too long to print to one page
    if colorString == 'WEATHERED WOOD':
        size2.set_font_size(65)
    elif colorString == 'TUDOR BROWN':
        size2.set_font_size(65)
    elif colorString == 'CHERRY WOOD':
        size2.set_font_size(70)
    else:
        size2.set_font_size(90)
        #print('else')
    if boardString == '1 1-8 x 3 ½':
        size1.set_font_size(65)
    
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
    date = "Date: " + makeDate
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

#used to increment date while chacking for a weekend
def dateInc(day, month, year):
    #define the date into datetime format
    yearS = int(year) + 2000
    monthS = int(month)
    dayS = int(day)
    dateL = datetime.date(yearS, monthS, dayS)

    #add one day to datetime
    dateL += datetime.timedelta(days=1)
    #define new date as 0-6
    weekdayNum = dateL.weekday()
    #check if = to 5, meaning saturday, move forward by 2
    if weekdayNum == 5:
        dateL += datetime.timedelta(days=2)
    #check if = to 6, meaning sunday, m ove forward one
    elif weekdayNum == 6:
        dateL += datetime.timedelta(days=1)
    #convert back into string
    day = dateL.strftime("%d")
    month = dateL.strftime("%m")
    year = dateL.strftime("%y")
    print(month, day, year)

    return day, month, year

#used to update the date without going through getProdDate() again
def setDate(day, month, year):
    makeDate = month + day
    makeDateInt = int(makeDate)
    makeDateBin = bin(makeDateInt)[2:].zfill(11)
    #returned makeDate to string for printOut() with correct formating. Since is also updated with the loop.
    makeDate = month + "/" + day + "/" + year
    return makeDate, makeDateBin

#Main loop
#Angus
print(r"""
           ___                       ___             ___ _           _   _          
          / _ \_ __ ___  ___ _ __   / __\____  __   / _ \ | __ _ ___| |_(_) ___ ___ 
         / /_\/ '__/ _ \/ _ \ '_ \ / _\/ _ \ \/ /  / /_)/ |/ _` / __| __| |/ __/ __|
        / /_\\| | |  __/  __/ | | / / | (_) >  <  / ___/| | (_| \__ \ |_| | (__\__ \
        \____/|_|  \___|\___|_| |_\/   \___/_/\_\ \/    |_|\__,_|___/\__|_|\___|___/
        ----------------------------------------------------------------------------
        """)
#collect raw data and process it individually
colorBin, colorString = getColor()
print('')
boardBin, boardString = getBoardSize()
print('')
lineBin = getLineNumber()
print('')
prodDateBin, day, month, year, howMany = getProdDate()
print('')
palletNum = getPalletNum()
print('')


#parse the data together
i = 1
while i <= int(howMany):
    j = 0
    #runs the loop twice for each day, since two pallets can be made per day, on average
    while j <= 1 and i <= int(howMany):
        #call setDate to update the date for each day
        makeDate, makeDateBin = setDate(day, month, year) 

        #create lot number
        rawLotStr = colorBin + boardBin + lineBin + makeDateBin
        encodedLot = encode(rawLotStr)

        #create, palletnumber and append it to lotNum
        palletSig = '-' + palletNum 
        lotNum = encodedLot + palletSig

        #prints to text file for reference
        printToFile(colorString, boardString, lineBin, makeDateBin, palletNum, lotNum)
        #create label to print out
        printOut(colorString, palletNum, boardString, lotNum, makeDate)

        #iterate pallet number in loop
        palletNum = int(palletNum) + 1
        palletNum = str(palletNum)

        j = j + 1
        i = i + 1
    #update date to next day, excluding weekends 
    day, month, year = dateInc(day, month, year)

    

print("File located at C:/Temp/" )
#Ask to contiue or quit
n = input("Press 1 to continue, anything else to exit: ")
if n == "1":
    r = 1
else:
    r = 0
