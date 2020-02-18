import random
player1=["rock","paper","scissor"]
player2=["rock","paper","scissor"]
a=random.choice(player1)
print("player1:",a)

b=random.choice(player2)
print("player2:",b)
if a=="rock" and b=="scissor":
    print("result:player1 win")
if  a=="rock" and b=="paper":
    print("result:player 2 win")
if a=="paper" and b=="scissor":
    print("result:player1 win")
    
