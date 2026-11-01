n = int(input('Enter the three digit number:'))

first = n % 10
second = n //10  % 10
third = n % 10

if( first * 2 == second and first == third* 2):
    print("Yes you have done it")
else:
    print("Please try next time.")
