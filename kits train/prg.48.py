a = [2, 4, 5, 7]

even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even =", even)
print("Count =", len(even))

print("Odd =", odd)
print("Count =", len(odd))