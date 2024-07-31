import random
low=int(input("Enter lower limit: "))
high=int(input("Enter higher limit:"))
no=random.randint(low,high)
print("Guessed no: ",no)
count=0
while True:
    guess=int(input("Guess the number: "))
    count+=1
    print("User guesses: ",guess)
    if(no==guess):
        print("You guessed it right\n")
        break
    if(no>guess):
        print("High")
    else:
        print("Low")
print("Total no. of guesses: ",count)