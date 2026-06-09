class product:
    def __init__(self,name,price):
        print("product object is created...!")
        self.name=name
        self.price=price
        print("---------------")
P1=product('Phone',25000)
print(f"name={P1.name}")
print(f"price={P1.price}")
P2=product('Laptop',70000)
print(f"name={P2.name}")
print(f"price={P2.price}")
P3=product('Headphones',5000)
print(f"name={P3.name}")
print(f"price={P3.price}")


