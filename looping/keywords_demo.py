#1.pass
#for i in range(1,10):
#    pass

#2.break: Terminate the loop
#for i in range(1,6):
#    if(i==3):
#        break
#    print(i)

#3. contiue: stop the currect iteration
#for i in range(1,6):
#    if(i==3):
#        continue
#    print(i)
#else:
#    print('else executed')

#WAP a program to find out the prime number
num = int(input("Enter the number:"))
if(num>1):
    for i in range(2,num):
          if(num% i ==0):
            print('Not prime number')
            break
    else:
        print("Prime number")
else:
    print(f'{num} is not a prime number.')

#1. print prime numbers between 1 to n
#2. print first n prime numbers.