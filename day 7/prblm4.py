class emp():
      def __init__(self,name,id,job,sal,dept):
            print("emp object is created")
            self.name=name
            self.id=id
            self.job=job
            self.sal=sal
            self.dept=dept
def details(self):
    print(f"name is {self.name}")
    print(f"id is {self.id}")
    print(f"job is {self.job}")
    print(f"sal is {self.sal}")
    print(f"dept is {self.dept}")
s1=emp('ravi',23,'IT',30000,'CAI')
details(s1)
s2=emp('chaitu',24,'IT',40000,'CSE')
details(s2)
s3=emp('subbu',25,'IT',50000,'EEE')
details(s3)
