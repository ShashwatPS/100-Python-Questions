# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

sentence = input()
count = {"UPPER": 0, "LOWER": 0}
for letter in sentence:
    if 'a'<=letter and letter <='z':
        count["LOWER"]+=1
    elif 'A'<=letter and letter<='Z':
        count["UPPER"]+=1
print(f'UPPER CASE {count["UPPER"]}')
print(f'LOWER CASE {count["LOWER"]}')