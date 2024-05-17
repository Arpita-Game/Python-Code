class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def work(self):
        print("Status - Working")


e1 = Employee("Arpita","95k")
print(e1.name,e1.salary)
print(f'Employee name is {e1.name}and salary is{e1.salary}')
e1.work()