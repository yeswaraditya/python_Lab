# prime numbers with in a range

start=int(input("Enter start number"))
end=int(input("Enter end number"))

for i in range (start,end+1):
    if(start > 1):
        for j in range(2,i):
            if(i %j ==0):
                break
        else :
            print(i)