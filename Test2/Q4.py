length = float(input('Enter the length of wall:'))
height = float(input('Enter the height of wall:'))
rate = int(input('Enter the painting cost per sq.m:'))

area = 4 * length * height
cost = area * rate
print('Total area of wall:',area)
print('Total cost of interior painting:',cost)