str="This is a python class for CEM students"
str2=str.split()
strNew=""
for word in str2:
    if (len(word)%2==0):
        strNew=strNew+word+" "
print(strNew)