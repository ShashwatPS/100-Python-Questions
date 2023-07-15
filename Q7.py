# _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i _ j.

ans = []
x= int(input())
y= int(input())
for i in range (0,x):
    temp = []
    for j in range (0,y):
        temp.append(i*j)
    ans.append(temp)
print(ans)