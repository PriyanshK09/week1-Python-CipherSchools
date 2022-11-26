name="     Priyansh     "
dots="..................."

#Removing Left Side Spaces
lstrip_name=name.lstrip()
print(f"{dots}Removing Left Side Spaces{dots}")
print(name.lstrip()+dots)

#Removing Right Side Spaces
rstrip_name=name.rstrip()
print(f"{dots}Removing Right Side Spaces{dots}")
print(name.rstrip()+dots)

#Removing Both Side Spaces
strip_name=name.strip()
print(f"{dots}Removing Both Side Spaces{dots}")
print(name.strip()+dots)

#For a string with Spaces between words
print(name.replace(" ","")+dots)

