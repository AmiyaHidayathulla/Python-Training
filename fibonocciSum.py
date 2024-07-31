limit=int(input("Enter the limit: "))
n1=0
n2=1
sum=n1+n2
for i in range(2,limit):
    n3=n1+n2
    sum=sum+n3
    n1=n2
    n2=n3
print(" Cumulative Sum of ",limit," numbers of fibonacci series= ",sum)