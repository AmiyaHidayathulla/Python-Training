visit=int(input("Total no of ranks to be visited: "))
li=[]
print("Enter the ranks: ")
for i in range(visit):
    a=int(input())
    li.append(a)
b=li[0]
count=0
for rank in li[1:]:
    if(rank<b):
        count+=1
        b=rank
print("No. of ranks cut in the list: ",count)