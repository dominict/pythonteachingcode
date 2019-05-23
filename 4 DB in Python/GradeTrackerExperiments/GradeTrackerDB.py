import pymysql as my
import getpass

#root password is something you set when you install mysql on your system
#the default may be blank; I use python123 for testing
dbconn = my.connect (host='127.0.0.1',port=3306,user='root', password='python123',  db='students')
 
#print(dbconn)
cursor = dbconn.cursor()
query = "SELECT ID, FirstName, LastName, Type, Password FROM user"
cursor.execute(query)
#the following line shows the schema descriptions of the headers of the data retrieved in the cursor object from the database using the query
#print(cursor.description)


#users = []
students = []
faculty = []

for (ID, FirstName, LastName, Type, Password) in cursor:
    #print("{} {} {} ({}) found. Password is {}.".format(ID, FirstName, LastName, Type, Password))
    thisuser = [ID,FirstName,LastName,Type,Password]
    if thisuser[3] == "faculty":
        faculty.append(thisuser)
    elif thisuser[3]=="student":
        students.append(thisuser)

cursor.close()
cursor = dbconn.cursor()
query = "SELECT * FROM grades"
cursor.execute(query)
grades = []
for GradeID, Grade,Comment,UserID in cursor:
    thisgrade = [GradeID,Grade,Comment,UserID]
    grades.append(thisgrade)
dbconn.close()

#print(users)
print("STUDENTS")
print(students)
print("FACULTY")
print(faculty)
#print(users[1][1],users[1][2])

#print(grades)

#print(str(grades[0][1])+" is of type "+str(type(grades[0][1])))
'''
grade tracking program - think through the goal up front- what is the task and design?
needs to enable several basic functions for teachers
needs to have login to protect the student data
'''
#import libraries first
import statistics as s

#add constants next
#admins = {'Dominic':'thomas','Faculty2':'ABC123'}

#students = {'Alex':[87,88,98],
#            'Sally':[88,67,93],
#            'Nboke':[90,88,78]}

#now define functions
def enterGrades():
    nameToEnter = input('Student name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in students[1]:
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
        average = s.mean(grades)
        print(student,' average ',average)

def main():
    print("User: " + user[1])
    print("""
    Welcome to the Grade Tracker

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Averages
    [4] - Exit
    """)

    action = input('What would you like to do? (Enter a number) ')

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

print("Welcome to the GradeTracker application.")
loginfname = input('First name: ')
loginlname = input('Last name: ')

for sublist in faculty:
    if loginfname in sublist[1]:
        if loginlname == sublist[2]:
            password = getpass.getpass('Password for '+loginfname+' '+loginlname+': ')
            if sublist[4] == password:
                print('Welcome,',loginfname)
                #now run the code
                user = sublist
                while True:
                    main()
            else:
                print('Invalid password.')
        else:
            print('User not found.')
    else:
        print('Invalid user. Check your spelling.')