number=int(input("Enter the number: "))
a=number
rev=0
while(a!=0):
    rem=a%10
    rev=(rev*10)+rem
    a=a//10
print("Reversed number:",rev)
if(rev==number):
    print(number," is a palindrome")
else:
    print(number," is not a palindrome")


#OR

number=int(input("Enter the number: "))
no=str(number)
rev=no[::-1]
print("Reversed number:",rev)
if(rev==no):
    print(number," is a palindrome")
else:
    print(number," is not a palindrome")