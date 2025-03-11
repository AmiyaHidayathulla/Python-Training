#find the maximum substring from the given string
st="banana"
sub=[]
for i in range(len(st)):
    for j in range(i,len(st)):
        sub.append(st[i:j+1])
print(sub)
sub.sort()
print((sub))
print(sub[-1])
