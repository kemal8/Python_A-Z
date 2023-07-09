# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25
# days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:
# * The year can be evenly divided by 4, is a leap year, unless:
# * The year can be evenly divided by 100, it is NOT a leap year, unless:
# * The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are NOT leap years. Source
# Complete this Task using Python.
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, Otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    if year % 4 == 0:                     # Check if the year is evenly divisible by 4
        if year % 100 == 0:               # Check if the year is also divisible by 100
            if year % 400 == 0:           # Check if the year is divisible by 400
                return True               # If divisible by 400, it is a leap year
            else:
                return False              # If divisible by 100 but not by 400, it is not a leap year
        else:
            return True                   # If divisible by 4 but not by 100, it is a leap year
    else:
        return False                      # If not divisible by 4, it is not a leap year

year = int(input())
print(is_leap(year))



# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")



# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")



# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil") # Not run



# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")



# def my_function(child3, child2, child1):
#   print("The youngest child is " + child1)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")