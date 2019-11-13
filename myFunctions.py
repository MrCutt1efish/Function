# DRY Do not Repeat

# names = ['Scott', 'Billy', 'Susy', 'Jane']

# print('First Name: ' + names[0])
# print('First Name: ' + names[1])
# print('First Name: ' + names[2])
# print('First Name: ' + names[3])

# for name in names:
#     print('First Name is ' + name)

# Create a converter for units of length
# Convert inches to mm 25.4 mm in 1 in
# Convert mm to inches 1/25.4

# inchesToConvert = initial inches
# convertedMM = converted mm

def getUserInput():
    userInput = input('Please enter the length? ')
    return userInput

def convertINtoMM(inches):
    convertedMM = float(inchesToConvert) * 25.4
    return convertedMM

def convertedMMtoIn(mm):
    convertedIN = float(mmToConvert) / 25.4
    return convertedIN

a=1
while a == 1:
    userChoise = input ('Please select an option \n '
                        ' 1- mm to inches \n'
                        ' 2- inches to mm \n'
                        ' Press any other key to quit \n')
    if userChoise == '1':
        mmToConvert = getUserInput()
        convertedIN = convertedMMtoIn(mmToConvert)
        print(" The conversion = " + str(convertedIN) + "in")
    elif userChoise == '2':
        inchesToConvert = getUserInput()
        convertedMM = convertINtoMM(inchesToConvert)
        print(" The conversion = " + str(convertedMM) + "mm")
    else:
        a=2
        print('You have exited the converter')
