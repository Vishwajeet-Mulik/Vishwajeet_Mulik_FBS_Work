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