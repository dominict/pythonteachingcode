'''
This is a grade tracking program - think through the goal up front- what is the task and design?
needs to enable several basic functions for faculty members.
This comment in triple quotes is called a docstring.
It is text that explains what a code file (aka module) or function does.
See https://www.geeksforgeeks.org/python-docstrings/
'''
#import libraries (aka module) first
import statistics as s

#add constants next
admins = {'Faculty1':'ABC123','Faculty2':'ABC123','Dominic':'Thomas'}

# Like the admins above is a dictionary but of students.
# Dictionaries use curly brackets with colons to associate keys with values.
# In this case, each student's first name is a key. The values are lists of grades.
# Lists are denoted with square brackets.
# Values are indexed within starting with 0 for the first one.
# Each value is separated by commas.
students = {'Alex':[87,88,98],
            'Sally':[88,67,93],
            'Nboke':[90,88,78]}

# Now we define functions. Functions encapsulate logic into reusable recipes that can be
# executed whenever we need them by calling their name with parentheses.
def enter_grades():
    '''
    Function to input a grade for a given student.
    '''
    name_to_enter = input('Student name: ')
    grade_to_enter = input('Grade: ')
    # This checks through the keys of the students dictionary to see if the name entered
    # exactly matches any one in there.
    if name_to_enter in students:
        print('Adding grade for'+name_to_enter)
        students[name_to_enter].append(float(grade_to_enter)) #float will have a .0
        print(str(name_to_enter)+' now has these grades:')
        print(students[name_to_enter])
    else:
        print('Student not found. Please check your spelling or go back and add if new.')

def remove_student():
    '''
    Function to remove a specific student.
    '''
    name_to_remove = input('Who do you want to remove? ')
    if name_to_remove in students:
        print('Removing '+name_to_remove)
        del students[name_to_remove]
        print(students)
    else:
        print('Student not found.')

def average_students():
    '''
    Function to average all students' grades.
    '''
    for student in students:
        grades = students[student]
        average = s.mean(grades) #notice the s? we imported the statistics module as s.
        #Thus, we are using a fucntion called "mean()" from the statistics module.
        print(student,' average ',average)

def main():
    '''
    Function to show user main menu and process option selections.
    '''
    print("User: " + login)
    # Here we present our main menu options once a person logs in successfully.
    print("""
    Welcome to the Grade Tracker

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Averages
    [4] - Exit
    """)

    action = input('What would you like to do? (Enter a number) ')
    #Here we process their choice of what they want to do.
    if action == '1':
        #print('1 selected')
        enter_grades()
    elif action == '2':
        #print('2 selected')
        remove_student()
    elif action == '3':
        #print('3 selected')
        average_students()
    elif action == '4':
        #print('4 selected')
        exit()
    else:
        print('Valid option not selected.') #need to cause it to reprompt

login = input('Faculty account name: ')

if login in admins:
    password = input('Password: ')
    if admins[login] == password:
        print('Welcome,',login)
        #now run the code
        while True:
            main()
    else:
        print('Invalid password.')
else:
    print('Invalid user.')
