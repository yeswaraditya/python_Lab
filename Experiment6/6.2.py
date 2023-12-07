a=0

def vowel_count(a):
    vowel=("aeiouAEIOU")
    a=str(input("enter a string"))
    count=0
    
    for i in a:
        if i in vowel:
            count=count+1
    print("no of vowels :",count)
    
vowel_count(a)
    