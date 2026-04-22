username = "Akash" #Global Scoopes

def fun():
    username = "Harshit" #Local scopes
    print(username) ## Looks in local scope first
    


fun()
print(username)# Falls back to global scope


#Lexial Scoping
password = "ajksf133"

def passw():
    print(password) # Follows laxial scoping

passw()


x = 99
def fun2(y):
    #x = 90
    z = x+y
    return z

result = fun2(1)
print(result)


"""a = 77
def fun3():
    global a ## bad practice
    a = 88

fun3()
print("a:",a) output = 88"""


#Enclosed Scoping

def f1():
    x = 22
    def f2():
        print("f2",x)
    return f2

myResult = f1()
myResult()


def chai(num):
    def actual(n):
        return n**num
    return actual

f = chai(2)
g = chai(3)

print(f)
print(g)

print(f(3))
print(g(3))
