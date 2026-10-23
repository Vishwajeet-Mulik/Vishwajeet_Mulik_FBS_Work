#take values
feet   = int(input("Enter feet:"))
inches = int(input("Enter inches:"))

#perform operation 
total_inches = feet * 12 + inches     #1 foot = 12 inches
meters = total_inches * 0.0254        #1 inch = 2.54cm
centimeters = total_inches * inches *2.54

#Display result
print("Meters=", meters)
print("centimeters=", centimeters)