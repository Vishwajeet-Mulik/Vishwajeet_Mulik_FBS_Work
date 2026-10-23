#WAP to check if given number is strong number
#what is strong number sum of the factorials of its digits is equal to the orginal number
#ex 145 1! +4! + 5! = 145
n = int(input('Enter the number:'))
temp = n
sum = 0

while n > 0:
    digit = n % 10

    fact = 1
    for i in range(1, digit+1):
        fact = fact * i
    sum = sum + fact
    n = n // 10

if sum == temp:
    print('Strong number.')
else:
    print('Not a Strong number.')
