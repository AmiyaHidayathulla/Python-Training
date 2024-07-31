n=int(input())
k=int(input())
j=int(input())
m=int(input())
p=int(input())
total=n
if((k>m)or(j>p)or(k==0)or(j==0)):
    print("INVALID INPUT")
n1=m//k
n2=p//j
n=n-(n1+n2)
if((m%k>0)or(p%j>0)):
    n=n-1
if(n<total):
    print("Total number of monkeys left on the tree is ",n)
else:
    print("INVALID INPUT")