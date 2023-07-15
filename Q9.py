# Write a program that accepts sequence of lines as input and prints the
# lines after making all characters in the sentence capitalized.

lines = []
while True:
    line = input()
    if not line:
        break
    else:
        lines.append(line.upper())
for item in lines:
    print(item)