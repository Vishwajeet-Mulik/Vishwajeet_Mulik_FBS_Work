#WAP to check if given number is Armstrong number or not
n =  int(input('Enter the number:'))
temp = n
total = 0
while temp >0:
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if total == n:
    print('Armstrong Number')
else:
    print('Not Arnstrong number')