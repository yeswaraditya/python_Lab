# Write a python program to count all letters, digits, and special symbols from a given string.

str1="dfdfjf4545kvj@#$"

alpha=digit=special=0

for i in range (len(str1)):
    if(str1[i].isalpha()):
        alpha=alpha+1
    elif (str1[i].isdigit()):
        digit=digit+1
    else :
        special=special+1
        
print("char count",alpha)
print("digit count",digit)
print("special count",special)
