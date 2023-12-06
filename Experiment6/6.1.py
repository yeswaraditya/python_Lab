
def tip_Calculator(amount,percentage):
    tp=(amount*percentage)/100
    return tp
    
amount=int(input("enter amount"))
percentage=int(input("enter percentage to be tip"))

tip=tip_Calculator(amount,percentage)
print("tip:",tip)