import random
limit=int(input("Enter the total no. of chances: "))
sys=0
user=0
while(limit!=0):
    u1=int(input("select:\n0 for stone\n1 for paper\n2 for scissors: "))
    s1=random.randint(0,2)
    print("System selected: ",s1)
    limit-=1
    if(u1==s1):
        print("No point\n")
        continue
    if((u1==0)and(s1==2)):
        print("U got 1 point\n")
        user+=1
        continue
    if((u1==2)and(s1==0)):
        print("System got 1 point\n")
        sys+=1
        continue
    if(u1<s1):
        print("System got 1 point\n")
        sys+=1
    else:
        print("U got 1 point\n")
        user+=1
if(sys==user):
    print("Tie")
elif(sys>user):
    print("System Won")
else:
    print("U won")