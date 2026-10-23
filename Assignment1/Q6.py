#input two angles from user and find third angle of the triangle
#take input values
a1 = int(input("Enter the first angle:"))
a2 = int(input("Enter the second angle:"))

#calcuate third angle
a3 = 180 - (a1 + a2)
#display result
print("third angle=", a3)