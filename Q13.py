# Write a program that accepts a sentence and calculate the number of letters and digits.

string = input()
count = {"Digits":0,"Alphabets":0}
for item in string:
    if(('a'<item and item<'z') or ('A'<item and item<'Z')):
        count["Alphabets"]+=1
    elif('0'<item and item <'9'):
        count["Digits"]+=1
print(count)