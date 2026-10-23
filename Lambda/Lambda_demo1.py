# add = lambda num1,num2: num1 + num2
# res = add(10,20)
# print(res)

#WAP to calculate simple interest using lambda function
# SI = lambda P , R, T: P * R * T/100
# res = SI(25000, 8, 3,)
# print(res)

#WAP to calculate the square of given data
#Method1
data =[1,2,3,4,5,6,7,8,9,10]
# def sq(n):
#     return n * n
# res = list(map(sq,data))
# print(res)

#Method 2 using lambda
res = list(map(lambda n:n **2,data))
print(res)

