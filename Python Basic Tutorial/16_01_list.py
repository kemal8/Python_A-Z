alist = ["apple", "banana", "cherry"]
print(alist)

# Allow Duplicates
blist = ["apple", "banana", "cherry", "apple", "cherry"]
print(blist)

# List Length
clist = ["as","gh","ay","hd"]
print(len(clist))

# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))
print("****")

# The list() Constructor
"""It is also possible to use the list() constructor when creating a new list."""
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""