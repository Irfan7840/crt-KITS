a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c
    print("smallest number =", smallest)