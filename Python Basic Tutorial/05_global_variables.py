# Global Variables

a = "kemal"
def myfunc1():
    print(a + " is a python developer")

myfunc1()



# Create a variable inside a function, with the same name as the global variable

b = "kemal"
def myfunc2():
    b = "Subhashana"
    print(b + " is a python developer")     # Output is, Subhashana is a python developer

myfunc2()

print(b + " is a python developer")         # Output is, kemal is a python developer



# The global Keyword
# If you use the global keyword, the variable belongs to the global scope:

c = "kemal"
def myfunc3():
    global c
    c = "Subhashana"
    print(c + " is a python developer")     # Output is, Subhashana is a python developer

myfunc3()

print(c + " is a python developer")         # Output is, Subhashana is a python developer
