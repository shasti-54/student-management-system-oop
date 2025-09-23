import pickle
import os

#Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

#Derived Class: Student 
  class Student(Person):
    def __init__(self, roll, name, age):
        super().__init__(name, age)
        self._roll = roll  # private attribute

    def display(self):
        print(f"Student Roll: {self._roll}, Name: {self.name}, Age: {self.age}")

    def get_roll(self):
        return self._roll

# Derived Class: Counselor
class Counselor(Person):
    def __init__(self, name, age, assigned_students=None):
        super().__init__(name, age)
        self.assigned_students = assigned_students if assigned_students else []

    def display(self):
        print(f"Counselor Name: {self.name}, Age: {self.age}, Assigned Students: {len(self.assigned_students)}")

    def assign_student(self, student):
        self.assigned_students.append(student)
        print(f"✅ Student {student.name} assigned to Counselor {self.name}")

#  Student Management
class StudentManagement:
    def __init__(self, filename="students.dat"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "rb") as f:
            try:
                return pickle.load(f)
            except EOFError:
                return []

    def save_students(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.students, f)

    def add_student(self):
        roll = input("Enter Roll No: ")
        if any(s.get_roll() == roll for s in self.students):
            print("❌ Roll number already exists!")
            return
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        student = Student(roll, name, age)
        self.students.append(student)
        self.save_students()
        print("✅ Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No students found!")
            return
        print("\n--- All Students ---")
        for s in self.students:
            s.display()

# Main Program 
def main():
    sm = StudentManagement()
    counselor = Counselor("Ms. Priya", 35)

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Assign Student to Counselor")
        print("4. Show Counselor Info")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            sm.add_student()
        elif choice == "2":
            sm.display_students()
        elif choice == "3":
            roll = input("Enter Roll No to assign: ")
            student = next((s for s in sm.students if s.get_roll() == roll), None)
            if student:
                counselor.assign_student(student)
            else:
                print("❌ Student not found!")
        elif choice == "4":
            counselor.display()
        elif choice == "5":
            print("Exiting... 👋")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
