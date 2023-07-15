# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.

words = input()
li = words.split(',');
li.sort()
ans = ','.join(li)
print(ans)
