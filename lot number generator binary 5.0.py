"""
This program is used to automatically generate lot numbers and profile lables for Green Fox Plastics and is property of Green Fox Plastics
Created by Xavier Angus

At this point, it is a frankenstien of the old program, thrown into a gui shell. 
"""
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime
from tkcalendar import DateEntry
from pathlib import Path
import xlsxwriter

#this is the values that the binary will be encoded into. make sure string on decoder is that same. 
charset = 'ABCDEFGHJKLMNPQRSTVWXYZ23456789#!'



##########################################################
#TKinterStuff
# Create the main window
root = tk.Tk()
root.title("GFP Lot Number Generator")
#set window size
root.geometry("360x400")
dateStr = tk.StringVar() #declare string variable for date

# Create a combo box with 13 options
combo_box1 = ttk.Combobox(root, values=["White", "Yellow", "Light_Grey", "Weathered_Wood", "Dark_Grey",
                                          "Lime_Green", "Aruba_Blue", "Turf_Green", "Cherry_Wood", "Cardinal_Red",
                                          "Patriot_Blue", "Tudor_Brown", "Black"])
combo_box2 = ttk.Combobox(root, values=["1/2 x 8", "3/4 x 1-3/4", "3/4 x 2-5/8", "3/4 x 3-1/2", "3/4 x 5-1/2",
                                          "1 x 5-1/2", "1-1/8 x 3-1/2", "1-1/2 x 1-1/2", "1-1/2 x 2-1/2", "1-1/2 x 3-1/2",
                                          "1-1/2 x 5-1/2", "1-1/2 x 9-1/2", "2-1/2 x 2-1/2", "3-1/2 x 3-1/2", "Bench Frame"])

# Set the default option to be "Option 1"
combo_box1.current(0)
combo_box1.config(font=("Helvetica", 12))
combo_box2.current(0)
combo_box2.config(font=("Helvetica", 12))


# Create labels for other objects
label1 = tk.Label(root, text="Select Color")
label1.config(font=("Helvetica", 12))
label2 = tk.Label(root, text="Select Profile")
label2.config(font=("Helvetica", 12))
label3 = tk.Label(root, text="Select Line Number")
label3.config(font=("Helvetica", 12))
label4 = tk.Label(root, text="Select Pallet Number")
label4.config(font=("Helvetica", 12))
label5 = tk.Label(root, text="Select Number of Pallets")
label5.config(font=("Helvetica", 12))
label6 = tk.Label(root, text="Select Date")
label6.config(font=("Helvetica", 12))

# Create a date picker widget
date_picker = DateEntry(root, date_pattern="yyyy-MM-dd",textvariable=dateStr)

# Set the default date to be the current date
date_picker.set_date(datetime.date.today())
date_picker.config(font=("Helvetica", 12))


# Create spinboxes
spinbox1 = Spinbox(root, from_=1, to=20, width=5)
spinbox1.config(font=("Helvetica", 12))
spinbox2 = Spinbox(root, from_=1, to=20, width=5)
spinbox2.config(font=("Helvetica", 12))
spinbox3 = Spinbox(root, from_=1, to=20, width=5)
spinbox3.config(font=("Helvetica", 12))

#Create labels that will show program outputs
output_label = tk.Label(root)
output_label.config(font=("Helvetica", 12))
lot_label = tk.Label(root)
lot_label.config(font=("Helvetica", 12))

###########################################################################
#Main program stuff

#take input color string and assign it a number
def assignColor(colorInput):
    color_to_number = {
    'White': 1,
    'Yellow': 2,
    'Light_Grey': 3,
    'Weathered_Wood': 4,
    'Dark_Grey': 5,
    'Lime_Green': 6,
    'Aruba_Blue': 7,
    'Turf_Green': 8,
    'Cherry_Wood': 9,
    'Cardinal_Red': 10,
    'Patriot_Blue': 11,
    'Tudor_Brown': 12,
    'Black': 13
    }
    assignedColor = color_to_number[colorInput]
    return assignedColor

#can handle up to 31 colors before another binary decimal is needed. 
#Turn numerical number into assigned binary
def getColor(color):
    j = 0
    while j == 0:
            color = str(color)
        # assign entered color to an integer 1 - 13
            if color == '1':
                colorNum = bin(int(color))
                colorName = 'White'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '2':
                colorNum =  bin(int(color))
                colorName = 'Yellow'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '3':
                colorNum = bin(int(color))
                colorName = 'Light Grey'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '4':
                colorNum = bin(int(color))
                colorName = 'Weathered Wood'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '5':
                colorNum = bin(int(color))
                colorName = 'Dark Grey'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '6':
                colorNum = bin(int(color))
                colorName = 'Lime Green'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '7':
                colorNum = bin(int(color))
                colorName = 'Aruba Blue'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '8':
                colorNum = bin(int(color))
                colorName = 'Turf Green'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '9':
                colorNum = bin(int(color))
                colorName = 'Cherry wood'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '10':
                colorNum = bin(int(color))
                colorName = 'Cardinal Red'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '11':
                colorNum = bin(int(color))
                colorName = 'Patriot Blue'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '12':
                colorNum = bin(int(color))
                colorName = 'Tudor Brown'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

            if color == '13':
                colorNum = bin(int(color))
                colorName = 'Black'
                #return color number to program and veify color
                print('The board color is set to ', colorName )
                j=1

    colorNum = str(colorNum)
    #remove 0b from front of string. result of binary conversion
    colorNum = colorNum[2:]
    colorNum = colorNum.zfill(5)
    return colorNum, colorName

#take input profile and assign it to a number
def assignProfile(profileInput):
    profile_to_number = {
    '1/2 x 8': 1,
    '3/4 x 1-3/4': 2,
    '3/4 x 2-5/8': 3,
    '3/4 x 3-1/2': 4,
    '3/4 x 5-1/2': 5,
    '1 x 5-1/2': 6,
    '1-1/8 x 3-1/2': 7,
    '1-1/2 x 1-1/2': 8,
    '1-1/2 x 2-1/2': 9,
    '1-1/2 x 3-1/2': 10,
    '1-1/2 x 5-1/2': 11,
    '1-1/2 x 9-1/2': 12,
    '2-1/2 x 2-1/2': 13,
    '3-1/2 x 3-1/2': 14,
    'Bench Frame': 15
    }
    assignedProfile = profile_to_number[profileInput]
    return assignedProfile

 #Can handle 31 board sizes until update needed again 
def getBoardSize(assignedProfile):
    #create loop to run until correct values entered
    i = 0
    while i == 0:
        j = 0
        while j == 0:
            boardSize = str(assignedProfile)
            #assign entered board size a value   
            if boardSize == '1':
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
def getLineNumber(line_number):
    lineNumInt  = int(line_number)
    #return line number as int and verify line
    print("The board was extruded on line ", lineNumInt)
    #remove 0b from binary conversion
    lineNum = bin(lineNumInt)[2:].zfill(4)
    return lineNum

#wont need update until 2100
def getProdDate(dateString):
    proDate = dateString
    month = proDate[0:2]
    proDateShred = proDate[2:]
    day = proDateShred[0:2]
    proDateShred = proDateShred[2:]
    year = proDateShred[0:2]
    #return production date as int and verify
    print("The board was produced on ", proDate)
    proDate = month + day
    proDateInt = int(proDate)
    #remove the 0x and make sure the string is 17 chaRACTERS
    #splitting into seperate sections allows a 1 decimal saving (16) so leaving it.
    proDate = bin(proDateInt)[2:].zfill(11)
    return proDate, day, month, year

#if more than 9 pallets are made in a day, needs to update length. This is unlikely
def getPalletNum(pallet_number, num_of_pallets):
    palletNum = pallet_number
    howMany = num_of_pallets
    print("The pallet number is", palletNum)
    return(palletNum, howMany)

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

#used to increment date by 1 while chacking for a weekend
#comment out noted section if friday has production
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
    #check if = to 5, meaning saturday, move forward by two
    if weekdayNum == 5:
        dateL += datetime.timedelta(days=2)
    #check if = to 6, meaning sunday, move forward one
    elif weekdayNum == 6:
        dateL += datetime.timedelta(days=1)
    #check if = to 4, meaning friday, move forward three
    #comment this out if producing on friday
    elif weekdayNum == 4:
        dateL += datetime.timedelta(days=3)

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

###########################################################################
# Create a button to display the selected options
def push_the_button():
    # Declare the variables as global
    global colorInput, profileInput, selected_date, line_number, pallet_number, num_of_pallets, dateString

    # Save the selected options as variables 
    colorInput = combo_box1.get()
    profileInput = combo_box2.get()

    # Save the selected date as a variable
    selected_date = date_picker.get_date()

    # Save the spinbox values as variables
    line_number = spinbox1.get()
    pallet_number = spinbox2.get()
    num_of_pallets = spinbox3.get()

    #make a variable with the date as a string
    dateString = selected_date.strftime("%m%d%y")

    # make an output string to double check
    input_properties = "Color : " + colorInput + "  || Profile: " + profileInput + "\n" + " Date: " + dateString +  "  || Line: " + line_number
    output_label["text"] = input_properties
    output_label.config(font=("Helvetica", 12))
    #########################################################################
    assignedColor = assignColor(colorInput)
    colorBin, colorString = getColor(assignedColor)
    print('')
    assignedProfile = assignProfile(profileInput)
    boardBin, boardString = getBoardSize(assignedProfile)
    print('')
    lineBin = getLineNumber(line_number)
    print('')
    prodDateBin, day, month, year = getProdDate(dateString)
    print('')
    palletNum, howMany = getPalletNum(pallet_number, num_of_pallets)
    print('')

        #parse the data together and loop to make iterations
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

    lot_out = "File located at C:/Temp/"
    lot_label["text"] = lot_out

button = tk.Button(root, text="Generate Lot Number", command=push_the_button)
button.config(font=("Helvetica", 12))

# Place the widgets in the main window
label1.pack()
combo_box1.pack()
label2.pack()
combo_box2.pack()
label3.pack()
spinbox1.pack()
label4.pack()
spinbox2.pack()
label5.pack()
spinbox3.pack()
label6.pack()
date_picker.pack()
button.pack()
output_label.pack()
lot_label.pack()

# Start the main event loop
root.mainloop()