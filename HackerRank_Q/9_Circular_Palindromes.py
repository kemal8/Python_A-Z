# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'circularPalindromes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING s as parameter.
#

# def circularPalindromes(s):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     s = input()

#     result = circularPalindromes(s)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

def get_max_palindrome_length(N, S):
    # Helper function to check if a substring is palindrome
    def is_palindrome(substring):
        return substring == substring[::-1]

    # Iterate over each rotation
    for k in range(N):
        rotated_string = S[k:] + S[:k]  # Rotate the string

        max_length = 0
        # Check all possible substrings
        for i in range(N):
            for j in range(i + 1, N + 1):
                substring = rotated_string[i:j]
                if is_palindrome(substring) and len(substring) > max_length:
                    max_length = len(substring)

        print(max_length)  # Print the maximum palindrome length for this rotation

# Get input from the user
N = int(input())  # Length of the string
S = input()  # The string itself

# Call the function to find and print the maximum palindrome lengths
get_max_palindrome_length(N, S)
