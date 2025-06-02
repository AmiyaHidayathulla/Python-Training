limit = int(input("Enter the upper limit: "))

num1 = 0
num2 = 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    num3 = num1 + num2
    if num3 >= limit:
        break
    if is_prime(num3):
        print(num3)
    num1 = num2
    num2 = num3
