
#input marks of 5 Subject
m1 = int(input("Enter the marks of Subject 1:"))
m2 = int(input("Enter the marks of Subject 2:"))
m3 = int(input("Enter the marks of Subject 3:"))
m4 = int(input("Enter the marks of Subject 4:"))
m5 = int(input("Enter the marks of Subject 5:"))

#calcuate total marks
total = m1 + m2 + m3 + m4 + m5

#calcuate the percentage
percentage = (total / 500) * 100

#Display result
print("total marks =", total)
print("percentage =", percentage,"%")