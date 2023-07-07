# complete this task using Python.
# Given an integer, n, perform the following conditional actions:
# *If n is odd, "print Weird"
# *If n is even and in the inclusive range of 2 to 5, print "Not Weird"
# *If it is even and in the inclusive range of 6 to 20, print "Weird"
# *If n is even and greater than 20, print "Not Weird"
# *Input Format is A single line containing a positive integer, n.
# all inputs are included with this range 1 < n < 100
# Output Format is Printed "Weird" if the number is Weird. Otherwise, print "Not Weird".

n = int(input("Enter Your Number"))

if 1 <= n <= 100:
    if (n % 2) == 1:
        print ("Weird")
    else:
        # print("Not Weird") 
        if 2 < n < 5:
            print("Not Weird")
        elif 6 < n <= 20:
            print("Weird") 
        elif n > 20:
            print("Not Weird")
        else:
            print("Not Weird")
else:
    print("Exceed the rang re enter your Number !")
 