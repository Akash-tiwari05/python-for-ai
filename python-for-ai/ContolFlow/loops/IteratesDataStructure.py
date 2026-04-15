#ITERATING OVER DATA STRUCTURES

#List
nums = [1,2,3]

for i in nums:
    print(i)


#String
for i in "akash":
    print(i)

#Dictionary
d = {"a": 1, "b": 2}

for key, value in d.items():
    print(key, value)

#LIST COMPREHENSION
squares = [x*x for x in range(5)]
print(squares)
#with conditions
evens = [x for x in range(10) if x %2 == 0]
print(evens)