#take value for salary
basic = int(input("Enter the salary:"))

#perform operation
da = basic * 10/ 100        #da is Dearness Allowance
ta = basic * 12/100         #ta is travel Allowance
hra = basic * 15/100        #hra is house rent Allowance

total = basic + da + ta + hra

#display result
print("DA=",da)
print("TA=",ta)
print("HRA=",hra)
print("total salary=", total)

