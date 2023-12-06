name=str(input("enter student name"))
student_class=str(input("enter student class"))
section=str(input("enter student section"))
grade=str(input("enter student grade"))
print("name:",name)
print("class:",student_class)
print("section:",section)

if (grade=='A' or grade=='a'):
    print("grade:Out Standing")
    
elif (grade=='B' or grade=='b'):
    print("grade:Excellent")
    
elif (grade=='C' or grade=='c'):
    print("grade:very good")
    
elif (grade=='D' or grade=='d'):
    print("grade:good")
    
elif (grade=='E' or grade=='E'):
    print("grade:satisfactory")
    
else :
    print("unrecognised")
   