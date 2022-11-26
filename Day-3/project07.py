# if elif else statement

# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = int(input("Enter your age: "))
if age == 0 or age < 0:
    print("Invalid age")
elif age >= 1 and age <= 3:
    print("Ticket is free")
elif age >= 4 and age <= 10:
    print("Ticket price is 150")
elif age >= 11 and age <= 60:
    print("Ticket price is 250")
else:
    print("Ticket price is 200")
