p1= float(input("Enter the price of product1:"))
p2= float(input("Enter the price of product2:"))
p3= float(input("Enter the price of product3:"))
p4= float(input("Enter the price of product4:"))
p5= float(input("Enter the price of product5:"))

total = p1 + p2 +p3 +p4 + p5
gst = total * 18 /100
bill = total + gst
print(f'Total price {total} Gst amount {gst} total bill {bill}')