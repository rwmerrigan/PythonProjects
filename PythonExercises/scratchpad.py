class Employee:
    def __init__(self, name, age, position, salary):
        # Instance Attributes
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None # example of caching
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
    
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {
        self.position} with a salary of ${self.salary}"
    
    @property # called a function "decorator"
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._annual_salary = None # reset the cached _annual_salary so it
        # can be recalculated
        self._salary = salary
    # read only properties can be defined without a setter

    @property
    def annual_salary(self):
        if self._annual_salary is None: # example of caching
            self._annual_salary = self.salary * 12
        return self._annual_salary

employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

# using the getter and setter methods for salary as shown above allow 
# for the user of the class to set and get the property in the same way
employee1.salary = 2000
print(employee1)