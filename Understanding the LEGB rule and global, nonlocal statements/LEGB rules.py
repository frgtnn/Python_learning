#LEGB - Local, Enclosing, Global, Built-In
#when i get:
# def test():       #global x
#     y = 'local y' ---->>> im changing it for x = 'local x' then i got local x and global x,
#     # print(y)
#     print(x)
# test()        #it printed out global x, even if we in def test(): function, cause it has it in global scope
#print(x)
# x = 'global x'
# import builtins
# print(dir(builtins)) #shows all of built-in functions in python

# def my_min():
#     pass
# m = min([5, 1, 4, 2, 3])
# print(m)


##ENCLSOING
x = 'global x'
def outer():
    x = 'outer x'       #local variable

    def inner():
        # nonlocal x          #affect on our 'outer x' so it gets overwritten
        x = 'inner x'       #local to our inner function
        print(x)            #local scope

    inner()
    print(x)                #it has a local variable 'outer x'

outer()
print(x)
