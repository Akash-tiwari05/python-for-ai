# If-else statements

temperature = 25

if temperature > 30:
    print("It's hot!")
else:
   print("Nice weather!")


#f-elif-else chains

score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

#Multiple conditions
age = 25
has_license = True

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")


#Nested if statements
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")

#Ternary
age = 18
result = "Adult" if age >= 18 else "Minor"
print(result)