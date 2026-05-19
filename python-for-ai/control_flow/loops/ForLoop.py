#For loop

for i in range(5):
    print(i) # print in range of 0 - 4

print("-"*40)
#Multiple range cases

for i in range(1,5):
    print(i) #print in range 1 - 4

print("-"*40)

for i in range(1,4,2):
    print(i) # print from 1 to 7 in every 2 step

print("-"*40)
#Print reverse order
for i in range(5,-1, -1):
    print(i)

print("-"*40)

#Loop through text
name = "Python"
for letter in name:
    print(letter)



#While loop
i = 0
while i < 5:
    print(i)
    i += 1