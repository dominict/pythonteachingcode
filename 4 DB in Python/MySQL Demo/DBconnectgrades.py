#you must have MySQL installed and running on the host indicated below with the database loaded from the SQL file here first or this code will not run when you try
import pymysql as my

#root password is something you set when you install mysql on your system
#the default may be blank; I used python123 for testing
#BE SURE to match your password to the password you set when installing MySQL. If in doubt, try a blank password
dbconn = my.connect (host='127.0.0.1',port=33067,user='root', password='',  db='students')
 
#print(dbconn) #This is a testing stub to make sure the connection worked. Uncomment it to use it.
cursor = dbconn.cursor()
query = "SELECT ID, FirstName, LastName, Type, Password FROM user"
cursor.execute(query)
#the following line shows the schema descriptions of the headers of the data retrieved in the cursor object from the database using the query
print(cursor.description)


users = []

for (ID, FirstName, LastName, Type, Password) in cursor:
    print("{} {} {} ({}) found. Password is {}.".format(ID, FirstName, LastName, Type, Password))
    thisuser = [ID,FirstName,LastName,Type,Password]
    users.append(thisuser)
cursor.close()
cursor = dbconn.cursor()
query = "SELECT * FROM grades"
cursor.execute(query)
grades = []
for GradeID, Grade,Comment,UserID in cursor:
    thisgrade = [GradeID,Grade,Comment,UserID]
    grades.append(thisgrade)
dbconn.close()

print(users)

print(users[5][1],users[5][2])

print(grades)

print(str(grades[0][1])+" is of type "+str(type(grades[0][1])))
