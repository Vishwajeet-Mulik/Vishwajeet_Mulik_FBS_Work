#digits seperate out program
#num = int(input("Enter the number:"))

#while(num>0):
#    d = num %10
#    print('d',d)
#    num = num // 10
#    print('num',num)


# Find factorial 
# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact* i
# print("factorial=",fact)

#i = 1

#what is while loop
#while loop means we don't know start and ending or we can say we don't know range
#while i <= n:
#    if n % i == 0:
#       print(i)
#    i += 1

# WAP to sum the n number
num = int(input("Enter the number:"))
sum = 0
while(num> 0):
    digit= num % 10
    num = num // 10
    sum = sum + digit
    print(sum)
