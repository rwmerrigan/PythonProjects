from dataclasses import dataclass

@dataclass
class Project:
    name: str

@dataclass
class Address:
    street: str
    city: str
    postal_code: str
    country_code: str

class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.projects = list() # Aggregation example, or "has-a" relationship
        # employee has a project or projects
        self.address = address
    
    def assign_project(self, project):
        self.projects.append(project)

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
    
    @address.setter
    def address(self, value):
        # composition example
        self._address = Address(value.street, value.city, value.postal_code,
                                value.country_code)

class Tester(Employee): # Tester is an employee  
    def run_tests(self):
        print(f"Testing is started by {self.name}...")
        print("Tests are done.")

class Developer(Employee): # Developer is an employee  
    def __init__(self, name, age, salary, framework):
        # once again super calls the employee version of this method, 
        # or more generically the class above this in the hierarchy
        super().__init__(name, age, salary)
        self.framework = framework
    
    def increase_salary(self, percent, bonus=0): # method overriding 
        super().increase_salary(percent) # super() points to the employee increase
        # salary method in a dynamic way, meaning even if the name changes
        self.salary += bonus

#region Prints and Instantiations
addr = Address(
    street="Some Street",
    city="Berlin",
    postal_code="10117",
    country_code="DE"
)

employee1 = Tester("Lauren", 44, 1000, addr)
employee2 = Developer("Ji-Soo", 38, 1000, "Flask")

employee1.increase_salary(20)
employee2.increase_salary(20, 30)

print(employee2.name)
print(employee2.framework)

# isinstance for determining if an instance is part of a class
print(isinstance(employee1, Tester))
print(isinstance(employee1, Employee))
# issubclass for determining if an class is part of a class
print(issubclass(Developer, Employee))
print(issubclass(Employee, object))
print(issubclass(Developer, object))

project_web = Project("Website Redesign")
project_ds = Project("Customer Analytics Dashboard")

employee1.assign_project(project_web)
employee1.assign_project(project_ds)

print(employee1.projects)
#endregion
