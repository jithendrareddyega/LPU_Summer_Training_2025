class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def get_info(self):
        return self.__emp_id, self.__name, self.__salary

    def set_info(self, emp_id=None, name=None, salary=None):
        if emp_id: self.__emp_id = emp_id
        if name: self.__name = name
        if salary is not None: self.__salary = salary

    def give_hike(self, percentage):
        self.__salary += self.__salary * (percentage / 100)

    def display(self):
        print(f"ID: {self.__emp_id}, Name: {self.__name}, Salary: {self.__salary}")

# Demonstration
emp = Employee("E101", "Alice", 50000)
emp.display()
emp.give_hike(10)
emp.display()
