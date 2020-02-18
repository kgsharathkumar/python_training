c=int(1)
a=int(input('enter the number='))
for b in range(1,a):
    if(a%b==0):
        c+=c
if(c==2):
    print("prime")
else:
    print("not prime")
    
