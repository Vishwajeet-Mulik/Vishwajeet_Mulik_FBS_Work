#WAP to check if a given number is prime number or not
n = int(input("Enter the number:"))
if n <=1:
    print('Not a prime number')
else:
    is_prime = True

    for i in range(2,n):
        print