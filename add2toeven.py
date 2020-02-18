num=int(input("enter the number:"))
while(num!=1):
    if(num%2==0):
        num/=2
        print("if even",num)
    else:
        num=(num*3)+1
        print("if odd",num)
print("final value",num)       
