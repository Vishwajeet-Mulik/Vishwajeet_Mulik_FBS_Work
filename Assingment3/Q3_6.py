cp =int(input("Enter the cost price:"))
sp =int(input("Enter the selling price:"))
if(sp>cp):
    print("Profit is:",sp-cp)
elif(cp>sp):
    print("Loss is:",cp-sp)
else:
    print("No profit no loss") 