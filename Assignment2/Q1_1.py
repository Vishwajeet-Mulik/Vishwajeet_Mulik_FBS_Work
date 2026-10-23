#convert hours,min,seconds into seconds
#take the value
hours = int(input("Enter hours:"))
minutes = int(input("Enter minutes:"))
seconds = int(input("Enter seconds:"))

#perform operation
total = hours * 3600 + minutes * 60 + seconds

#display result
print("total seconds=", total)