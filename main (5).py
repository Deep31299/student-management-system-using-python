students = []

# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

# Function to enroll a student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))
    grade = calculate_grade(marks)

    student = {
        "roll": roll,
        "name": name,
        "course": course,
        "marks": marks,
        "grade": grade,
        "attendance": [],
        "messages": []
    }
    students.append(student)
    print("✅ Student enrolled successfully!\n")

# Function to mark attendance
def mark_attendance():
    roll = input("Enter Roll Number to mark attendance: ")
    date = input("Enter date (dd-mm-yyyy): ")
    for student in students:
        if student['roll'] == roll:
            student['attendance'].append(date)
            print(f"✅ Attendance marked for {student['name']} on {date}\n")
            return
    print("❌ Student not found.\n")

# Function to view attendance
def view_attendance():
    roll = input("Enter Roll Number to view attendance: ")
    for student in students:
        if student['roll'] == roll:
            print(f"📅 Attendance for {student['name']}: {student['attendance']}\n")
            return
    print("❌ Student not found.\n")

# Function to send a message
def send_message():
    roll = input("Enter Roll Number to send message to: ")
    sender = input("Enter your role (Student/Teacher/Parent): ")
    message = input("Enter your message: ")
    for student in students:
        if student['roll'] == roll:
            student['messages'].append(f"{sender}: {message}")
            print("✅ Message sent.\n")
            return
    print("❌ Student not found.\n")

# Function to view communication messages
def view_messages():
    roll = input("Enter Roll Number to view messages: ")
    for student in students:
        if student['roll'] == roll:
            print(f"💬 Communication log for {student['name']}:")
            for msg in student['messages']:
                print(f" - {msg}")
            print()
            return
    print("❌ Student not found.\n")

# View all students
def view_students():
    if not students:
        print("❌ No student records found.\n")
        return
    print("\n📋 All Student Records:")
    for student in students:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Course: {student['course']}, Marks: {student['marks']}, Grade: {student['grade']}")
    print()

# Search student
def search_student():
    roll = input("Enter Roll Number to Search: ")
    for student in students:
        if student['roll'] == roll:
            print(f"✅ Student Found: {student}")
            return
    print("❌ Student not found.\n")

# Update student
def update_student():
    roll = input("Enter Roll Number to Update: ")
    for student in students:
        if student['roll'] == roll:
            print("Enter New Details:")
            student['name'] = input("New Name: ")
            student['course'] = input("New Course: ")
            student['marks'] = float(input("New Marks: "))
            student['grade'] = calculate_grade(student['marks'])
            print("✅ Student record updated!\n")
            return
    print("❌ Student not found.\n")

# Delete student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print("✅ Student record deleted!\n")
            return
    print("❌ Student not found.\n")

# Main Menu
def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Enroll New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Mark Attendance")
        print("7. View Attendance")
        print("8. Send Message")
        print("9. View Messages")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            mark_attendance()
        elif choice == '7':
            view_attendance()
        elif choice == '8':
            send_message()
        elif choice == '9':
            view_messages()
        elif choice == '10':
            print("🚪 Exiting Student Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 to 10.\n")

# Run the system
menu()
