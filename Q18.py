# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
#
# Following are the criteria for checking the password:
#
# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12

def check(str):
    char_small = 0
    char_capital =0
    number = 0
    char_special =0
    length = len(str)
    for i in str:
        if 'a'<=i and i<='z':
            char_small+=1
        elif 'A'<=i and i<='Z':
            char_capital+=1
        elif '0'<=i and i<='9':
            number+=1
        elif i=='$' or i=='#' or i=='@':
            char_special+=1
    if char_small>0 and char_capital>0 and char_special>0 and number>0 and (6<=length and length<=12):
        return True
    else:
        return False

user = input()
ans = []
user_li = user.split(",")
for pas in user_li:
    if(check(pas)):
        ans.append(pas)

print(','.join(ans))