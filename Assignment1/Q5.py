# calcuate the compound interest
#Give values for p, t, r
P = int(input("Enter the Principal:"))
T = int(input("Enter the Time:"))
R = int(input("Enter the R:"))

#calcuate the Compound interest
CI = P *(1 + R /100) **T - P
print("Compound interest=", CI)