# loops in python - for loop and while loop 

# While loop are used to execute a block of code repeatedly until a given condition is satisfied and becomes false.
# For loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# printing "hello world" 5 times using while loop
i = 1  # initialising the variable 
while i <= 5:  # condition
    print("hello world")  # code to be executed
    i += 1  # incrementing the variable
    
# printing "hello world" 5 times using for loop
for i in range(5):  # range() function is used to generate a sequence of numbers
    print("hello world")
    