# what is palindrome ex 121 if we reverse it and same number comes than it is palindrome
# so we need to shuff first and last digit

num = int(input("Enter the three digit number:"))

first = num // 100 # why floor division by because the hundreds digit is the first digit
last = num % 10
if (first == last):
    print('Number is palindrome')

else:
    print('Number is not palindrome')