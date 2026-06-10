print("program starts")
a=10
print("a=",a)
try:
    print("result=",a/0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")        
print("program ends")