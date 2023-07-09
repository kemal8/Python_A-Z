n = int (input("Enter Your Number : "))

new_array = []

i = 1
while i<=n:
    new_array.append(i)
    i = 1 + i

print(*new_array, sep="")


# numbers = [1, 2, 3, 4, 5]
# print(*numbers)