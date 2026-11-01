r = 20
l = 50
b = 40
cost = 35

area_of_rectangle = l*b
area_of_semcircle = 1/2 * 3.14 * r**2

area_of_field = area_of_rectangle + area_of_semcircle
fencing = cost * area_of_field
total_fencing_cost = fencing * 5
print("Area of field:",area_of_field)
print('Cost of total fencing to farm:',total_fencing_cost)