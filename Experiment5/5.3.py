# fibonacci series

n= int(input("Enter val of n"))

a,b=0,1
i=1
print("fibonacci seq")

while i <= n:
    print(a)
    next=a+b
    a=b
    b=next
    i=i+1
    