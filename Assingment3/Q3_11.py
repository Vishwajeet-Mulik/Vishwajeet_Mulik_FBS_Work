age1 = int(input("Enter the age of person1:"))
age2 = int(input("Enter the age of person2:"))
age3 = int(input("Enter the age of person3:"))
age4 = int(input("Enter the age of person4:"))
age5 = int(input("Enter the age of person5:"))
ticket_amount = int(input("Enter the ticket amount:"))
total_amount = 0


if (age1 <12):
    print("Person1 is below 12 will get 30% discount.")
    ticket_cost = ticket_amount * 70 /100
elif(age1 >59):
    print("Person1 is above 59 will get 50% discount.")
    ticket_cost = ticket_amount * 50 /100
else:
    print("other full ticket.")
    ticket_cost = ticket_amount
if (age2 <12):
    ticket_cost = ticket_amount * 70 /100
    print("Person2 is below 12 will get 30% discount.")
elif(age2 > 59):
    ticket_cost = ticket_amount * 50 /100
    print("person2 is above 59 will get 50% discount.")
else:
    ticket_cost = ticket_amount
    print("Other full ticket.")
if(age3 <12):
    ticket_cost = ticket_amount * 70 /100
    print("Person3 is below 12 will get 30% discount.")
elif(age3 >59):
    ticket_cost = ticket_amount * 50 /100
    print("Person3 is above 59 will get 50% discount.")
else:
    ticket_cost = ticket_amount
    print("Other full ticket.")
if(age4 <12):
    ticket_cost = ticket_amount * 70 /100
    print("Person4 is below 12 will get 30% discount.")
elif(age4 >59):
    ticket_cost = ticket_amount * 50 /100
    print("Person4 is above 59 will get 50% discount.")
else:
    ticket_cost = ticket_amount
    print("Other full ticket.")
if(age5 <12):
    ticket_cost = ticket_amount * 70 /100
    print("Person5 is below 12 will get 30% discount.")
elif(age5 >59):
    ticket_cost = ticket_amount * 50 /100
    print("Person5 is above 59 will get 50% discount.")
else:
    ticket_cost = ticket_amount
    print("Other full ticket.")
total_amount = total_amount + ticket_cost

