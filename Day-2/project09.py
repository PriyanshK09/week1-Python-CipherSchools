#Summary of Chapter 2

#strings
name = "Priyansh"

#String Indexing
print(name[0]) #P

#String Slicing 
print(name[0:3]) #Pri

#Take User input
age=int(input("Enter your age: "))
print(age)

#Take 2 user inputs
user_name, age = input("Enter your name and age: ").split(",")
print(user_name)
print(age)

#len function
print(len(name))

#lower, upper, title method
print(name.title())
print(name.lower())
print(name.upper())

#find, replace, center method
r_pos = name.find("r")
r_pos2 = name.find("r", r_pos+1)
print(r_pos2)

#**name** -> **Priyansh**
print(name.center(12, "*"))

#strings are immutable
