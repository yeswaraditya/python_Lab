#find factorial
n=int(input("Enter number ot find factorial"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)