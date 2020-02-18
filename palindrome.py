str=input("enter the string")
rev=[]
a=len(str)
rev=reversed(str)    
if list(str)==list(rev):
    print("palindrome")
else:
    print("not palindrome")
