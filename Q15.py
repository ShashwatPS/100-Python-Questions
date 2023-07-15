# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a= input()
string = ""
ans = 0

for i in range (1,5):
    string+=a
    ans+=int(string)

print(ans)