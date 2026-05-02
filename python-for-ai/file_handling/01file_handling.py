#Write operations
with open("sample.txt",'w') as f:
    f.write("""Welcome to Python File Handling practice.

    This file contains multiple lines.
    You can use it to test read(), readline(), and readlines().

    Topics to practice:
    1. Opening a file
    2. Reading content
    3. Writing new content
    4. Appending data
    5. File pointer (seek, tell)

    Keep practicing daily.
    Python is powerful!

    End of file.""")
print("File written succesfully...")


#Append operations
with open("sample.txt","a") as f:
    f.write("\n    Thankyou!...")

#Read Operations
with open("sample.txt","r") as f:
    read = f.read()
print("File content is as follows : ",read)

#Read line by line
with open("sample.txt","r") as f:
    for line in f:
        print("->",line.strip())