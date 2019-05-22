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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, gross_salary, prog_lang):
        super().__init__(first_name, last_name, gross_salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first_name, last_name, gross_salary, employees = None):
        super().__init__(first_name, last_name, gross_salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Johnny", "Bog", 5000, "Python")
dev_2 = Employee("Dik", "Dog", 6000)
manager_1 = Manager("Sue", "Smith", 9000, [dev_1])

print(manager_1.email)

manager_1.print_emps()
manager_1.add_emp(dev_2)
manager_1.print_emps()