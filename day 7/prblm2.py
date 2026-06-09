class Student():
    def __init__(self,name,age):
        print("Student Object is created..!")
        self.name=name
        self.age=age
def details(self):
    print(f"name is {self.name}")
    print(f"age is {self.age}")
s1=Student('ravi',23)
details(s1)
s2=Student('subbu',24)
details(s2)
s3=Student('chaitu',25)
details(s3)
s4=Student('chippa',2)
details(s4)