# Exercise - WATCH COCO
# Ask user's name and age
# If user name starts with "a" or "A" and age is above 10 then print "You can watch coco movie"
# Else print "You can't watch coco movie"

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

if (user_name[0] == "a" or user_name[0] == "A") and user_age > 10:
    print("You can watch coco movie")
    
else: 
    print("You can't watch coco movie")
    