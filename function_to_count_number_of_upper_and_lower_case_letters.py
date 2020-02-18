def upercase(s):
    a,b=[0,0]
    for c in s:
        if  c.isupper():
            a+=1
        elif c.islower():
            b+=1
        else:
            pass
    print("number of upper case letters is:",a)
    print("number of lower case letters is:",b)


upercase('hAi')



