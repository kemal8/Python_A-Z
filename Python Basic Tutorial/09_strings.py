print("Hello")
print('Hello')
print("***")



# Assign String to a Variable
a = "Hello"
print(a)
print("***")



# Multiline Strings
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)
print("***")

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)
print("***")



# Strings are Arrays
d = "Hello, World!"
print(d[0])
print(d[1])
print(d[2])
print("***")



# Looping Through a String
for x in "banana":
  print(x)
print("***")



# String Length
a = "Hello, World!"
print(len(a))
print("***")



# Check String

txt1 = "The best things in life are free!"
print("free" in txt1)
print("a" in txt1)
print("z" in txt1)
print("***")

txt2 = "The best things in life are free!"
if "free" in txt2:
  print("Yes, 'free' is present.")
print("***")



# Check if NOT
txt3 = "The best things in life are free!"
print("expensive" not in txt3)
print("***")

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
print("***")