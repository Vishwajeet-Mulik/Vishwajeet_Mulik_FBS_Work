sub1 = int(input("Enter the marks of subject 1:"))
sub2 = int(input("Enter the marks of subject 2:"))
sub3 = int(input("Enter the marks of subject 3:"))
sub4 = int(input("Enter the marks of subject 4:"))
sub5 = int(input("Enter the marks of subject 5:"))
outoff = int(input("Exam conducted outoff:"))
total = sub1 + sub2 + sub3 + sub4 + sub5
print("Total marks:", total)

percentage = (total / outoff) * 100
print("Percentage:", percentage)


if percentage > 90:
    print("A")
elif percentage > 80:
    print("B1")
elif percentage > 70:
    print("B2")
elif percentage > 60:
    print("C")
elif percentage > 50:
    print("C1")
elif percentage > 40:
    print("D")
else:
    print("Fail")