str1="Hello"
lower=[]
upper=[]

for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)

finalstr="".join(lower+upper)
print(finalstr)