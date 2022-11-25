# at least 14 char
#contain any sort of letters
#contaion numbers
# and symbols $%^&**


import re

pattern = re.compile(r"(^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$)")

string = 'aAer2334@'
a = pattern.fullmatch(string)

if a == None:
    print('your password must be at least 8 digits long\n contain letters, numbers, any of these symbols $%#@ and end with a number')

else:
    print('logged in')