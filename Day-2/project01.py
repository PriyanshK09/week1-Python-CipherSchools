#Take two comma seperated inputs from user
#1.) user's name e.g. "Priyansh"
#2.) a single character e.g. "a"

#output should be:
#1.) user's name length
#2.) count the character the user inputed (bonus: case insensitive count)

name, char = input("Enter your name and a character seperated by comma: ").split(",")
print(f"Length of your name is {len(name)}")
print(f"Count of {char} is {name.count(char)}") #case sensitive
print(f"Count of {char} is {name.lower().count(char.lower())}") #case insensitive

