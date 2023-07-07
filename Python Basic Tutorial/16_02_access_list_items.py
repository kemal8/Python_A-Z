# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print("***")

# Negative Indexing
"""Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc."""
thislist = ["apple", "banana", "cherry"]
print(thislist[2])
print(thislist[1])
print(thislist[0])
print(thislist[-1])
print(thislist[-2])
print("***")

# Range of Indexes
"""You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items."""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])    #   ['cherry', 'orange', 'kiwi']
print(thislist[1:6])    #   ['banana', 'cherry', 'orange', 'kiwi', 'melon']
print(thislist[0:3])    #   ['apple', 'banana', 'cherry']
print(thislist[:4])     #   ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:])     #   ['cherry', 'orange', 'kiwi', 'melon', 'mango']
# Range of Negative Indexes
print(thislist[-4:-1])
print(thislist[-3:-2])
print("***")

# Check if Item Exists
thislistB = ["apple", "banana", "cherry"]
if "apple" in thislistB:
  print("Yes, 'apple' is in the fruits list")