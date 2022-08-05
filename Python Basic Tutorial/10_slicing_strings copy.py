# Slicing

b = "Hello, World!"
print(b[2:5]) #Get the characters from position 2 to position 5 (not included)
print(b[2:9]) ##Get the characters from position 2 to position 9 (not included)
print("***")



# Slice From the Start

c = "Hello, World!"
print(c[:5]) #Get the characters from the start to position 5 (not included)
print(c[:9]) #Get the characters from the start to position 9 (not included)
print("***")



# Slice To the End

d = "Hello, World!"
print(d[2:]) #Get the characters from position 2, and all the way to the end
print(d[4:]) #Get the characters from position 4, and all the way to the end
print("***")



# Negative Indexing

b = "Hello, World!"
print(b[-5:-2]) # From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2):
print(b[-9:-4]) # From: "o" in "World!" (position -9) To, but not included: "d" in "World!" (position -4):
print("***")

