# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.The numbers obtained should be
# printed in a comma-separated sequence on a single line.

def check(s):
    if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
        return True
    return False


ans = []
for i in range(1000,3001):
    if check(str(i)):
        ans.append(str(i))
print(','.join(ans))