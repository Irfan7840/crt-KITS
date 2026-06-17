num = 684
first_digit = num // 100
middle_digit = (num // 10) % 10
last_digit = num % 10
largest_digit = max(first_digit, middle_digit, last_digit)
print("Input:")
print(num)
print("\nOutput:")
print(largest_digit)