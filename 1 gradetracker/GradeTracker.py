"""
Grade Tracker Program
---------------------
A simple command-line tool for faculty to manage and track student grades.

Features:
- Secure login for faculty members.
- Add new grades to existing students.
- Remove students.
- View averages for all students.

Author: <Your Name>
"""

import statistics as s

# -----------------------------
# Constants
# -----------------------------
ADMINS = {
    'Dominic': 'Hacker',
    'Faculty2': 'ABC123',
    'Faculty3': '123ABC'
}

STUDENTS = {
    'Alex': [87, 88, 98],
    'Sally': [88, 67, 93],
    'Nboke': [90, 88, 78]
}

# -----------------------------
# Helper Functions
# -----------------------------
def enter_grades():
    """Add a grade for an existing student."""
    name = input('Enter student name: ').strip()
    if name not in STUDENTS:
        print(f"❌ Student '{name}' not found. Please check spelling or add manually later.")
        return

    try:
        grade = float(input('Enter grade (0–100): '))
        if 0 <= grade <= 100:
            STUDENTS[name].append(grade)
            print(f"✅ Added grade for {name}. Current grades: {STUDENTS[name]}")
        else:
            print("❌ Grade must be between 0 and 100.")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric grade.")


def remove_student():
    """Remove a student from the system."""
    name = input('Enter student name to remove: ').strip()
    if name in STUDENTS:
        confirm = input(f"Are you sure you want to remove {name}? (y/n): ").lower()
        if confirm == 'y':
            del STUDENTS[name]
            print(f"✅ {name} removed successfully.")
        else:
            print("❎ Removal cancelled.")
    else:
        print(f"❌ Student '{name}' not found.")


def average_students():
    """Display the average grade for each student."""
    print("\n--- Student Averages ---")
    for student, grades in STUDENTS.items():
        if grades:
            avg = s.mean(grades)
            print(f"{student}: {avg:.2f}")
        else:
            print(f"{student}: No grades recorded.")
    print("------------------------\n")


def show_menu():
    """Display the main menu."""
    print("""
======= Grade Tracker Menu =======
1. Enter Grades
2. Remove Student
3. Show Student Averages
4. Exit
=================================
""")


def main():
    """Main control loop."""
    while True:
        show_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            enter_grades()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            average_students()
        elif choice == '4':
            print("Exiting... Goodbye.")
            break
        else:
            print("❌ Invalid choice. Please select 1–4.")


# -----------------------------
# Entry Point: Login
# -----------------------------
def login():
    """Handle faculty login."""
    print("===== Faculty Login =====")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in ADMINS and ADMINS[username] == password:
        print(f"✅ Welcome, {username}!")
        return True
    else:
        print("❌ Invalid credentials.")
        return False


if __name__ == "__main__":
    if login():
        main()
    else:
        print("Access denied.")
