# def addition(num1, num2):
#     sum = num1 + num2
#     return sum

# num1 = int(input("Enter number1:"))
# num2 = int(input("Enter number2:"))
# res = addition(num1, num2)
# print("Addition:",res)

def fact(num):
    mult = 1
    for i in range(1, num +1):
        mult*=1
    return mult
n = 5
res = fact(n)
print('Factorial:',res)