import random
import UserInput

# this function receives a min and max number and an operator, and uses them
# numbers are sorted before returning them
# the function is useful since we need to do this in two parts of the program
def generateNums(minNum, maxNum, operator):
    nums = [random.randint(minNum, maxNum), random.randint(minNum, maxNum)]

    if operator == '-':
        nums.sort()

    return nums



op = UserInput.inputChoice('Addition or subtraction test? [enter "+" or "-"]: ', ('+','-'))
challenge = UserInput.inputChoice('Make the final question a challenge? [enter "y" or "n"]: ', ('y', 'n'))
qty = UserInput.inputInt('How many tests should be generated?: ', minValue = 1)

file = open('output.txt', 'w')

for i in range(qty):
    if op == '+':
        print('\n\nAddition Test\n')
        file.write('\n\nAddition Test\n\n')
    elif op == '-':
        print('\n\nSubtraction Test\n')
        file.write('\n\nSubtraction Test\n\n')
        
    print('Name: __________\n\n')
    file.write('Name: __________\n\n\n')

    questions = []

    for i in range(10):
        if i == 9 and challenge == 'y':

            nums = generateNums(10, 20, op)

            print('Challenge question - do your best!')
            print(nums[1], op, nums[0], '= ____\n')
            file.write('Challenge question - do your best!\n')
            file.write(str(nums[1]) + ' ' + op + ' ' + str(nums[0]) + ' = ____\n\n')
        else:
            while True:
                nums = generateNums(0, 9, op)

                if nums not in questions:
                    questions.append(nums)
                    break

            print(nums[1], op, nums[0], '= ____\n')
            file.write(str(nums[1]) + ' ' + op + ' ' + str(nums[0]) + ' = ____\n\n')

file.close()
print('\nTests saved in output.txt file.')
