rawLotNum = input('Enter raw lot number: ')
rawLotInt = int(rawLotNum)
encodedLotNumber = hex(rawLotInt)
print(encodedLotNumber)