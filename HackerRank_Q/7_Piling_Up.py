# There is a horizontal row of 1 cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j] ≥ side Length[i] When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

# Example

# blocks = |1, 2, 3, 8, 7]
# Result: No
# After choosing the rightmost element, 7, choose the leftmost element, 1. After than, the choices are 2 and 8. These are both larger than the top block of size 1.
# blocks = [1, 2, 3, 7, 8]

# Result: Yes
# Choose blocks from right to left in order to successfully stack the blocks.

# Input Format

# * The first line contains a single integer T, the number of test cases.
# * For each test case, there are 2 lines. 
# * The first line of each test case contains n, the number of cubes.
# * The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

# write a code using python.


from collections import deque

def can_stack_cubes(num_cubes, cube_sidelengths):
    cubes = deque(cube_sidelengths)
    prev = 0
    while cubes:
        leftmost = cubes[0]
        rightmost = cubes[-1]
        
        if prev != 0 and (leftmost > prev or rightmost > prev):
            return "No"
        
        if leftmost >= rightmost:
            prev = cubes.popleft()
        else:
            prev = cubes.pop()
    
    return "Yes"

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of cubes
    num_cubes = int(input())
    
    # Read the side lengths of the cubes
    cube_sidelengths = list(map(int, input().split()))
    
    # Check if it is possible to stack the cubes
    result = can_stack_cubes(num_cubes, cube_sidelengths)
    
    # Print the result
    print(result)


