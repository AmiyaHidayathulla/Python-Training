N=int(input("Enter the maximum no of candies in a jar: "))
k=int(input("Enter minimum candies: "))
input=int(input("Enter the no.of candies needed: "))
if(input<N):
    new=N-input
    print("No.of candies sold: ",input)
    if(new<=k):
        new=N
    print("Number of candies available: ",new)
else:
    print("INVALID INPUT")