# EXERCISE , NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number.
# if user guessed correctly then print "You won!"
# if user guessed incorrectly then:
#     if user guessed lower than actual number then print "Too low!"
#    if user guessed higher than actual number then print "Too high!"

# google "how to generate random numbers in python" to generate a random number
# winning_number

winning_number = 27
user_input = int(input("Guess a number between 1 and 100 : "))
if user_input == winning_number:
    print("You won!")
else: #Nested IF-ELSE
    if user_input < winning_number:
        print("Too low!")
    else:
        print("Too high!")
        
#Nested Loop is a loop inside a loop
        