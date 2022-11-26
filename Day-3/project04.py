# EXERCISE , NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number.
# if user guessed correctly then print "You won!"
# if user guessed incorrectly then:
#     if user guessed lower than actual number then print "Too low!"
#    if user guessed higher than actual number then print "Too high!"

# google "how to generate random numbers in python" to generate a random number
# winning_number

import random

num = random.randint(0, 10)
print('Number:',num)
attempt = 4 
msg = 'You Lost!'   

while attempt > 0:
    user_input = int(input('Enter Number: '))

    if user_input == num:
        msg = 'You Won!'
        break
    else:
        print(f'Try again! {attempt} attempt left.')
        attempt -= 1
        continue

print(msg)