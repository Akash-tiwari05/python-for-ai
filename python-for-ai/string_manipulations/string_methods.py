#Case Methods in python
text = "Python programng"
print(text.lower()) #lower case
print(text.upper()) #All UpperCase
print(text.title()) #Title
print(text.capitalize()) #First Capitals
print(text.casefold()) 


#Slicing
print(text[2:]) #Slice upto 2 op = thon programng
print(text[1:6]) #return sbstring from start to end op = ython
print(text[::-1]) #revrse


#Search and check
print(text.find('y')) #return index
print(text.index('y'))
print(text.count('o')) #count
print(text.startswith('p')) #return true/false
print(text.endswith('g')) #return true/false


#Replace & split
print(text.replace('o','t'))
print(text.split(" "))
print("-".join(text))

#Remove Spaces
print(text.strip())
print(text.lstrip())
print(text.rstrip())


#Check Methods
print(text.isalpha())
print(text.isalnum())
print(text.isdigit())
print(text.isspace())
