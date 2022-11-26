#Find and Replace in Python

#replace() method is used to replace a substring in a string with another substring.
#find() method is used to find a substring in a string.

string="She is beutiful and she is good dancer"
print(string.replace(" ", "_")) #Replacing Space
print(string.replace("is", "was")) #Replacing a Word/String from Senetence

print(string.find("is")) #Finding a Word/String from Senetence
is_pos1 = string.find("is") # is_pos1 ---> Number
is_pos2 = string.find("is", is_pos1+1)

print(is_pos2)