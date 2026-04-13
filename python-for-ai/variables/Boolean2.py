#BOOLEAN TYPE CASTING
bool(0)     # False
bool(1)     # True
bool("")    # False
bool("Hi")  # True

#SHORT-CIRCUIT EVALUATION
False and print("Hello")  # Not executed
True or print("Hello")    # Not executed

#DENTITY vs EQUALITY (IMPORTANT 🔥)
a = [1,2]
b = [1,2]

print(a == b)  # True (value same)
print(a is b)  # False (different memory)
print()

#BOOLEAN FUNCTIONS
all([True, True, False])  # False
any([False, False, True]) # True