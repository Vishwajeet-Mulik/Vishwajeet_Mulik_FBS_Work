#take values
cost = int(input("Enter cost price:"))
discount = int(input("Enter discount percentage:"))

#perform operation for discount amount
discount_amount = cost * discount / 100
#perform operation for selling price
selling_price = cost - discount_amount

#display result
print("discount amount=",discount_amount )
print("selling price =", selling_price)