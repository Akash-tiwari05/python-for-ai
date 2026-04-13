# Basic math
print(10 + 3)   # 13 - Addition
print(10 - 3)   # 7  - Subtraction
print(10 * 3)   # 30 - Multiplication
print(10 / 3)   # 3.333... - Division (always gives float)

# Special operators
print(10 // 3)  # 3  - Floor division (rounds down)
print(10 % 3)   # 1  - Modulo (remainder)
print(10 ** 3)  # 1000 - Exponent (power)


#Order of operations
result = 2 + 3 * 4      # 14 (not 20!)
result = (2 + 3) * 4    # 20 (parentheses first)

#LOGICAL OPERATORS
x = 5
print(x > 2 and x < 10)  # True
print(x < 2 or x > 3)    # True
print(not(x > 2))        # False

#ASSIGNMENT OPERATORS
x = 5
x += 3   # x = x + 3 → 8