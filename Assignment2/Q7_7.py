#take values
num =int(input("Enter three digit number:"))

#perform operation

a = num // 100
b = (num // 10) % 10
c = num % 10

sum = a + b + c
print("sum of three digit=", sum)