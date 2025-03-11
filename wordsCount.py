str1="i love my country, i love u, i hate u"
str2="love"
count=0
words=str1.split()
for word in words:
    if str2== word:
        count=count+1
print(count)

num=words.count(str2)
print(num)
