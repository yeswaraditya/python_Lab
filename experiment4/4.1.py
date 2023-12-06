name=str(input("enter student name"))
student_class=str(input("enter student class"))
section=str(input("enter student section"))
sub1=int(input("enter maths marks"))
sub2=int(input("enter physics marks"))
sub3=int(input("enter social marks"))
sub4=int(input("enter biology marks"))
sub5=int(input("enter hindi marks"))
totalmarks=sub1+sub2+sub3+sub4+sub5
percentage=(totalmarks/500)*100
print("Name : ",name) 
print("Class : ",student_class) 
print("Section : ",section)
print("percentage :",percentage)

if percentage < 45:
    print("status:fail")
    
elif   45 <= percentage <= 60:
    print("status:pass")
    
elif   60 <= percentage <= 75:
    print("status:good")
    
elif   75 <= percentage <= 85:
    print("status:very good")
    
elif   85 <= percentage <= 100:
    print("status:excellent")
    
else:
    print("error")

