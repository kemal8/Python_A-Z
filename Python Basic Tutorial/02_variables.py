# Creating Variables

x = 5
y = "Kemal"
print (x)
print (y)

a = 4       # x is of type int
b = "Sale"  # x is now of type str
print (a)



# Casting

c = str(3)    # c will be '3'
d = int(3)    # d will be 3
e = float(3)  # e will be 3.0
print (c)
print (d)
print (e)



# Get the Type

f = 5
l = 20
m = 20.5
n = 1j
g = "John"
k = ("apple", "banana", "cherry")
o = ["apple", "banana", "cherry"]
p = range(6)
q = {"name" : "John", "age" : 36}
r = {"apple", "banana", "cherry"}
s = frozenset({"apple", "banana", "cherry"})
t = True
u = b"Hello"
v = bytearray(5)
w = memoryview(bytes(5))
xx = None
print(type(f)) # Output is <class 'int'>
print(type(l)) # Output is <class 'int'>
print(type(m)) # Output is <class 'float'>
print(type(n)) # Output is <class 'complex'>
print(type(g)) # Output is <class 'str'>
print(type(k)) # Output is <class 'tuple'>
print(type(o)) # Output is <class 'list'>
print(type(p)) # Output is <class 'range'>
print(type(q)) # Output is <class 'dict'>
print(type(r)) # Output is <class 'set'>
print(type(s)) # Output is <class 'frozenset'>
print(type(t)) # Output is <class 'bool'>
print(type(u)) # Output is <class 'bytes'>
print(type(v)) # Output is <class 'bytearray'>
print(type(w)) # Output is <class 'memoryview'>
print(type(xx)) # Output is <class 'NoneType'>



# Single or Double Quotes?

h = "H1John"
print(h)       # Output is H1John
#double quotes are the same as single quotes:
h = 'H2John'
print(h)       # Output is H2John



# Case-Sensitive

j = 4
J = "Sally"
print(j)       # Output is 4
print(J)       # Output is Sally