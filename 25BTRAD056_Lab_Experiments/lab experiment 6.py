number = int(input("Enter a number: "))

if number < 2:
    print(number, "is not a prime number")
else:
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)
