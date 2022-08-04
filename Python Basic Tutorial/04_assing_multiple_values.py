# Many Values to Multiple Variables

a,b,c = "go","to","temple"
print(a,b,c)



# One Value to Multiple Variables

d = e = f = "Orange"
print(d)
print(e)
print(f)



# Unpack a Collection

month = ["Jan","Feb","Mar"]
g,h,i = month
print(g)
print(h)
print(i)
print(g,h,i)


# You can also use the + operator to output multiple variables

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)



# In the print() function, when you try to combine a string and a number with the + operator, 
# Python will give you an error:

"""
x = 5
y = "John"
print(x + y)

"""



# The best way to output multiple variables in the print() function is to separate them with commas, 
# which even support different data types:

j = 5
k = "Kemal"
print(j,k)