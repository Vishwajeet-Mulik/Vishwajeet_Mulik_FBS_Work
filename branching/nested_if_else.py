gender = input("Enter gender(F/M):")
age = int(input("Enter the age:"))

if(gender == 'F'):
    if(age >=18):
        print("Girl is eligible for marriage:")
    else:
        print("Girl is not eligible for marriage:")

else:
    if(age >=21):
        print("boy is eligible for marriage:")
    else:
        print("boy is not eligible for marriage:")