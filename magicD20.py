# imported module random
import random

# creating a function 'getanswer'


def getAnswer(answerNumber):
    # If , Elif , Else are all used to return values for 'getanswer'
    if answerNumber == 1:
        return 'Fail'
    elif answerNumber == 2:
        return 'Fail'
    elif answerNumber == 3:
        return 'Fail'
    elif answerNumber == 4:
        return 'Fail'
    elif answerNumber == 5:
        return 'Fail'
    elif answerNumber == 6:
        return 'Fail'
    elif answerNumber == 7:
        return 'Fail'
    elif answerNumber == 8:
        return 'Fail'
    elif answerNumber == 9:
        return 'Fail'
    elif answerNumber == 10:
        return 'Fail'
    elif answerNumber == 11:
        return 'Fail'
    elif answerNumber == 12:
        return 'Fail'
    elif answerNumber == 13:
        return 'Fail'
    elif answerNumber == 14:
        return 'Fail'
    elif answerNumber == 15:
        return 'Fail'
    elif answerNumber == 16:
        return 'Fail'
    elif answerNumber == 17:
        return 'Fail'
    elif answerNumber == 18:
        return 'Fail'
    elif answerNumber == 19:
        return 'Fail'
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
