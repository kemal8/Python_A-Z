# String Format
"""
age = 36
txt = "My name is John, I am " + age
print(txt)

**error**
"""

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
print("***")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
print("***")

quantity1 = 3
itemno1 = 567
price1 = 49.95
myorder1 = "I want to pay {2} dollars for {0} pieces of item {1}."
myorder2 = "I want to pay {1} dollars for {2} pieces of item {0}."
print(myorder1.format(quantity1, itemno1, price1))
print(myorder2.format(quantity1, itemno1, price1))
print("***")