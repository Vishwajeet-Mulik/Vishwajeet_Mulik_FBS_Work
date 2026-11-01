#WAP to check leap year
year = int(input('Enter the year:'))

if (year%4==0):
    print("It is leap year.")
elif(year%100==0):
    print('Not a leap year')
elif(year%400==0):
    print('It is leap year.')
else:
    print("It is not leap year.")