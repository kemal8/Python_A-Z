# Built-in Data Types
"""
Text Type:	        str
Numeric Types:	    int, float, complex
Sequence Types:	    list, tuple, range
Mapping Type:	    dict
Set Types:	        set, frozenset
Boolean Type:	    bool
Binary Types:	    bytes, bytearray, memoryview
None Type:	        NoneType

"""



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
print(f)
print(type(l)) # Output is <class 'int'>
print(l)
print(type(m)) # Output is <class 'float'>
print(m)
print(type(n)) # Output is <class 'complex'>
print(n)
print(type(g)) # Output is <class 'str'>
print(g)
print(type(k)) # Output is <class 'tuple'>
print(k)
print(type(o)) # Output is <class 'list'>
print(o)
print(type(p)) # Output is <class 'range'>
print(p)
print(type(q)) # Output is <class 'dict'>
print(q)
print(type(r)) # Output is <class 'set'>
print(r)
print(type(s)) # Output is <class 'frozenset'>
print(s)
print(type(t)) # Output is <class 'bool'>
print(t)
print(type(u)) # Output is <class 'bytes'>
print(u)
print(type(v)) # Output is <class 'bytearray'>
print(v)
print(type(w)) # Output is <class 'memoryview'>
print(w)
print(type(xx)) # Output is <class 'NoneType'>
print(xx)

"""
<class 'int'>
5
<class 'int'>
20
<class 'float'>
20.5
<class 'complex'>
1j
<class 'str'>
John
<class 'tuple'>
('apple', 'banana', 'cherry')
<class 'list'>
['apple', 'banana', 'cherry']
<class 'range'>
range(0, 6)
<class 'dict'>
{'name': 'John', 'age': 36}
<class 'set'>
{'apple', 'banana', 'cherry'}
<class 'frozenset'>
frozenset({'apple', 'banana', 'cherry'})
<class 'bool'>
True
<class 'bytes'>
b'Hello'
<class 'bytearray'>
bytearray(b'\x00\x00\x00\x00\x00')
<class 'memoryview'>
<memory at 0x0000020ACD855E40>
<class 'NoneType'>
None
"""