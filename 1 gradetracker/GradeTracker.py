'''
grade tracking program - think through the goal up front- what is the task and design?
needs to enable several basic functions for teachers
needs to have login to protect the student data
'''
#import libraries first
import statistics as s

#add constants next
admins = {'Faculty1':'ABC123','Faculty2':'ABC123'}

#Like the admins above is a dictionary but of students. Dictionaries use curly brackets with colons to associate keys with values. In this case, each student's first name is a key. The values are lists of grades. 
#Lists are denoted with square brackets. Values are indexed within starting with 0 for the first one. Each value is separated by commas.
students = {'Alex':[87,88,98],
            'Sally':[88,67,93],
            'Nboke':[90,88,78]}

#Now we define functions. Functions encapsulate logic into reusable recipes that can be executed whenever we need them by calling their name with parentheses.
def enterGrades():
    nameToEnter = input('Student name: ')
    gradeToEnter = input('Grade: ')
    #This checks through the keys of the students dictionary to see if the name entered exactly matches any one in there.
    if nameToEnter in students:
        print('Adding grade for'+nameToEnter)
        students[nameToEnter].append(float(gradeToEnter)) #float will have a .0
        print(str(nameToEnter)+' now has these grades:')
        print(students[nameToEnter])
    else:
        print('Student not found. Please check your spelling or go back and add if new.')

def removeStudent():
    nameToRemove = input('Who do you want to remove? ')
    if nameToRemove in students:
        print('Removing '+nameToRemove)
        del students[nameToRemove]
        print(students)
    else:
        print('Student not found.')

def averageStudents():
    for student in students:
        grades = students[student]
        average = s.mean(grades) #notice the s? we imported the statistuics module as s. Thus, we are using a fucntion called "mean()" from the statistics module.
        print(student,' average ',average)

def main():
    print("User: " + login)
    #Here we present our main menu options once a person logs in successfully.
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
        enterGrades()
    elif action == '2':
        #print('2 selected')
        removeStudent()
    elif action == '3':
        #print('3 selected')
        averageStudents()
    elif action == '4':
        #print('4 selected')
        exit()
    else:
        print('Valid option not selected.') #need to cause it to reprompt

login = input('User: ')

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