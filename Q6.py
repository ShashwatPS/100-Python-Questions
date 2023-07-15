# Write a program that calculates and prints the value according to the given formula:
#
# Q = Square root of [(2 _ C _ D)/H]
#
# Following are the fixed values of C and H:
#
# C is 50. H is 30.
#
# D is the variable whose values should be input to your program in a comma-separated sequence.

import math

def solve(x,c,h):
    val = int(x)
    return round(math.sqrt((2*c*val)/h))

C = 50
H = 30
values = input()
array = values.split(',')
ans = []
for item in array:
    ans.append(solve(item, C, H))
print(ans)