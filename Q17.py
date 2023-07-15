# Write a program that computes the net amount of a bank account based a transaction
# log from console input.

ans = 0

while True:
    line = input()
    if not line:
        break
    line_li = line.split(" ")
    amount = int(line_li[1])
    if line_li[0]=='D':
        ans+=amount
    else:
        ans-=amount

print(ans)

