#Integer vs float division

# Regular division (always float)
result = 10 / 3    # 3.333...
print(result)

# Integer division (rounds down)
result = 10 // 3   # 3
print(result)


#Common mistakes
# Even when dividing evenly
result = 10 / 2
print(result)       # 5.0 (not 5)
print(type(result)) # <class 'float'>

# Use // for integer result
result = 10 // 2    # 5
print(result)       
print(type(result))