#take values
days = int(input("Enter number of days:"))

years = days // 365
remaining_day = days % 365

weeks = remaining_day // 7
remaining_day = remaining_day % 7

#display result
print("years=", years)
print("weeks=", weeks)
print("days=", remaining_day)
