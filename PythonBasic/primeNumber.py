
number = int(input("Enter a number: "))
flag = False

if number == 1:
    print(f"{number}, is not a prime number")
elif number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            flag = True
            break

if flag:
    print(f"{number}, is not a prime number")
else:
    prime(f"{number}, is a prime number")



















