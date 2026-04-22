#Errors

x = 10  # global
def fun():
    print(x) #UnboundLocalError
    x = 20

#fun()

#global error
def fun2():
    global x
    print(x)
    x = 20

fun2()


#Non local variable
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()  # 20