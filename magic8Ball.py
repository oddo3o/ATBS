# imported module random
import random

# creating a function 'getanswer'


def getAnswer(answerNumber):
    # If , Elif , Else are all used to return values for 'getanswer'
    if answerNumber == 1:
        return 'It is certian'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Try Again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'No'
    elif answerNumber == 8:
        return 'Outlook is not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


# r gives a random value between 1 - 9 based on the module random
# int is used to change given value to a integer to be used
r = random.randint(1, 9)

# Creating variable 'fortune' w/ function 'getAnswer' and 'r'
# Based on the random value given by r will run in 'getanswer'
fortune = getAnswer(r)

# Print out the result of variable 'fortune'
print(fortune)
