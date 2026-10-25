userid = "123"
userpass = 'Vishwajeet'


for i in range(1,4):
    uid = input("Enter the userid:")
    upass = input('Enter the userpassword:')
    if (userid == uid and userpass == upass):
        print("Login Successfull")
        break
    else:
        print("Incorrect Credendtials")
else:
    print("Your 3 attempts are over.")


