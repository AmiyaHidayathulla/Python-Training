limit = int(input("Enter the number of prime Fibonacci numbers to display: "))

num1 = 0
num2 = 1
count = 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while count < limit:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    if is_prime(num3):
        print(num3)
        count += 1
