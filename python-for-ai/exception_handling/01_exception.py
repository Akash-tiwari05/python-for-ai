#Exception Handling

#Basic Syntax
try:
    x = 10/0
except ZeroDivisionError:
    print("Error occurred")

#Handling Specific Exceptions
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")


#Using else
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", x)

##File not found error
try:
    file = open("test.txt",'r')
    c = file.read()
    print(c)
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")
