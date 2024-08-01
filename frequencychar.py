str=input("Enter the string: ")
dict={}
for c in str:
    if(c==" "):
        continue
    if c in dict:
        dict[c]+=1
    else:
        dict[c]=1
print(dict)