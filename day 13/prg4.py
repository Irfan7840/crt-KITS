
num = 472

first_digit = num // 100
middle_digit = (num // 10) % 10
last_digit = num % 10

swapped_num = (last_digit * 100) + (middle_digit * 10) + first_digit

print("Input:")
print(num)
print("\nOutput:")
print(swapped_num)