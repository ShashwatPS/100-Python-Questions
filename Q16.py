# Use a list comprehension to square each odd number in a list. The list is input by a sequence
# of comma-separated numbers.

numbers = input()
number_li = numbers.split(",")
squared_numbers = [str(int(num)**2) for num in number_li if int(num)%2!=0]
print(','.join(squared_numbers))