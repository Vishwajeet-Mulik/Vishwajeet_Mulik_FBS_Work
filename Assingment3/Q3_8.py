#WAP to check the username and userpassword and then generate the 4 digit captcha to verfied it
uname=input("Enter the username:")
upassword=input("Enter the userpassword:")

usern = "Vishwajeet"
userpass = "1234"
import random
captcha = random.randint(1000,9999)
print(captcha)
Captcha = input("Enter the above captcha:")
if(uname==usern and upassword ==userpass):
    Entry_captcha = captcha
    if Entry_captcha == captcha:
        print("Login Succcessfull")
    else:
        print("Invaild") 
else:
    print("username or userpassword is Wrong")