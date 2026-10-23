#check triangle is equilateral, isosceles or scalene
#so first we will check whether triangle is valid or not
a1 = int(input("Enter the first angle:"))
a2 = int(input("Enter the second angle:"))
a3 = int(input("Enter the third angle:"))
if(a1 + a2 > a3 and a2 +a3 > a1 and a1 + a3 > a2):
    print("Triangle is valid.")
    if(a1 == a2 and a2 == a3):
        print("Triangle is equilateral.")
    elif(a1 == a2 or a2 == a3 or a1 == a3):
        print("Triangle is isosceles.")
    else:
        print("Triangle is scalene.")
else:
    print("Triangle is not valid.")
    