class Student:  
    def __init__(self, name, age, department, grade ):  
        self.name = name  
        self.age = age  
        self.grade = grade
        self.department = department

    def display_info(self):  
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}, Grade: {self.grade}")
        
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"Updated Grade: {self.grade}")

if __name__ == "__main__":
    student1 = Student("Alice", 20, "Computer Science", "A")
    student1.display_info()
    student1.update_grade("A+")
    
    student2 = Student("Bob", 22, "Mathematics", "B")
    student2.display_info()
    student2.update_grade("B+")
    
    student3 = Student("Charlie", 21, "Physics", "C")
    student3.display_info()
    student3.update_grade("C+")