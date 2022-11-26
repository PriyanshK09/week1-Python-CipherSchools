#Ask user to input 3 numbers and you have to print the average of these three numbers using String Formatting.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

avg=(a+b+c)/3
print("The average of %d, %d and %d is %f"%(a,b,c,avg))