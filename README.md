# student-management-system-oop

# 🎓 OOP Student Management System (Python)

A **Python-based Student Management System** demonstrating **OOP concepts** like **inheritance, polymorphism, and encapsulation**, with persistent file storage.  
This project allows managing students and counselors in a simple, structured way.  

---

## ✨ Features
- ➕ Add new students (Roll No, Name, Age)  
- 📜 Display all students  
- 👩‍🏫 Assign students to a counselor  
- 🔍 View counselor details (Name, Age, Assigned Students)  
- ❌ Prevent duplicate roll numbers  
- 💾 Data is stored in a binary file (`students.dat`) using **pickle**  

---

## 🛠️ Tech Stack
- **Language:** Python 3  
- **Modules:** `pickle`, `os`  

---

## 🧩 OOP Concepts Used
1. **Inheritance** – `Student` and `Counselor` inherit from `Person`.  
2. **Polymorphism** – `display()` method behaves differently in `Student` and `Counselor`.  
3. **Encapsulation** – Student roll number `_roll` is private and accessed via a method.  

---

## 🚀 How to Run
1. Clone the repository:
```bash
git clone https://github.com/your-username/oop-student-management.git
cd oop-student-management


