#WAP to check if given number is perfect number
n = int(input('Enter the number:'))
total = 0
for i in range(1,n): #why not n+1 because perfect number is equal
    if(n%i==0):      #to the sum of its factors excluding the nummber itself
        total = total + i
if total ==n:
    print('Perfect number')
else:
    print('Not a perfect number')