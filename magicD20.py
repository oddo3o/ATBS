# imported module random
import random

# creating a function 'getanswer'


def getAnswer(answerNumber):
    # If , Elif , Else are all used to return values for 'getanswer'
    if answerNumber == 1:
        return 'Fail_1'
    elif answerNumber == 2:
        return 'Fail_2'
    elif answerNumber == 3:
        return 'Fail_3'
    elif answerNumber == 4:
        return 'Fail_4'
    elif answerNumber == 5:
        return 'Fail_5'
    elif answerNumber == 6:
        return 'Fail_6'
    elif answerNumber == 7:
        return 'Fail_7'
    elif answerNumber == 8:
        return 'Fail_8'
    elif answerNumber == 9:
        return 'Fail_9'
    elif answerNumber == 10:
        return 'Fail_10'
    elif answerNumber == 11:
        return 'Fail_11'
    elif answerNumber == 12:
        return 'Fail_12'
    elif answerNumber == 13:
        return 'Fail_13'
    elif answerNumber == 14:
        return 'Fail_14'
    elif answerNumber == 15:
        return 'Fail_15'
    elif answerNumber == 16:
        return 'Fail_16'
    elif answerNumber == 17:
        return 'Fail_17'
    elif answerNumber == 18:
        return 'Fail_18'
    elif answerNumber == 19:
        return 'Fail_19'
    elif answerNumber == 20:
        return 'Success'


# r gives a random value between 1 - 9 based on the module random
# int is used to change given value to a integer to be used
r = random.randint(1, 20)

# Creating variable 'fortune' w/ function 'getAnswer' and 'r'
# Based on the random value given by r will run in 'getanswer'
fortune = getAnswer(r)

# Print out the result of variable 'fortune'
print(fortune)
