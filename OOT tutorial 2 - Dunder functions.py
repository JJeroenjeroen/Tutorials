class Employee:

    raise_amount = 1.04

    def __init__(self, first_name, last_name, gross_salary):
        self.First = first_name
        self.Last = last_name
        self.Salary = gross_salary
        self.email = first_name + "." + last_name + "@company.com"


    def fullname(self):
        return (self.First + " " + self.Last)

    def apply_raise(self):
        self.Salary = int(self.Salary * self.raise_amount)


    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.First, self.Last, self.Salary)

    def __str__(self):
        return "Employee('{}', '{}')".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.Salary + other.Salary

    def __len__(self):
        return len(self.fullname())



dev_1 = Employee("Johnny", "Bog", 5000)
dev_2 = Employee("Dik", "Dog", 6000)

print(len(dev_1))

print(len("test"))
print("test".__len__())