class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")

class Manager(Employee):
    def __init__(self, name, emp_id, department, team_size):
        super().__init__(name, emp_id, department)
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")

class Developer(Employee):
    def __init__(self, name, emp_id, department, programming_language):
        super().__init__(name, emp_id, department)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

if __name__ == "__main__":
    manager = Manager("Priya", "M001", "IT Management", 10)
    developer = Developer("Shine", "D101", "Software Development", "Python")

    print("Manager Info:")
    manager.display_info()
    print("\nDeveloper Info:")
    developer.display_info()