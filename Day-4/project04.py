# problem
# ask user to input a number containing more than one digit
# example 1256
# calculate 1+2+5+6 and print

# algorithm
# ask user to input in string, i.e don't change string to input
# example  "1256"
# pick string character one by one and change to int

 # solution
number= input("Enter a number: ")
total = 0
i=0
while i < len(number):
    total+= int(number[i])
    i += 1
print(total)