def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


limit = int(input("Enter the limit: "))
print("Fibonacci series:")
for i in range(limit):
    print(fibonacci(i), end=" ")