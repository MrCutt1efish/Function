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

# inchesToConvert = getUserInput()
# convertedMM = float(inchesToConvert) * 25.4
# print(" The conversion = " + str(convertedMM))
# # mmToConvert = initial mm
# # convertedIN = converted in

# mmToConvert = getUserInput()
# convertedIN = float(mmToConvert) / 25.4
# print(" The conversion = " + str(convertedIN))

while True:
    userChoise = input ('Please select an option \n '
                        ' 1- mm to inches \n'
                        ' 2- inches to mm \n')
    if userChoise == 1: