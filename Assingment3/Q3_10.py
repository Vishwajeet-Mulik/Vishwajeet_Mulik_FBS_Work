#WAP a code to check whether a male or female is eligible to marry
gender= input("Enter the gender(M/F):")
age = int(input("Enter the age:"))
if (gender == "F"):
    if(age >=18):
        print("Girl is Eligiable for Marriage.")
    else:
        print("Girl is Not Eligiable for Marriage.")
else:
    if(gender== "M"):
        if(age>=21):
            print("Boy is Eligiable for Marriage.")
        else:
            print("Boy is not Eligiable for Marriage.")

