# %% [markdown]
# # Module 1 Practice 1
# ##  Getting started with Python in Jupyter Notebooks
# ### notebooks, comments, print(), type(), addition, errors and art
# 
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - use Python 3 in Jupyter notebooks
# - write working code using `print()` and `#` comments  
# - write working code using `type()` and variables
# - combine strings using string addition (+)
# - add numbers in code (+)
# - troubleshoot errors
# - create character art  
# 
# # &nbsp;
# >**note:** the **[ ]** indicates student has a task to complete  
#   
# >**reminder:** to run code and save changes: student should upload or clone a copy of notebooks 
# 
# #### notebook use
# - [ ] insert a **code cell** below   
# - [ ] enter the following Python code, including the comment: 
# ```python 
# # [ ] print 'Hello!' and remember to save notebook!
# print('Hello!')
# ```
# Then run the code - the output should be:  
# `Hello!`

# %%
# [ ] print 'Hello' and remember to save notebook!
print('Hello!')

# %% [markdown]
# #### run the cell below   
# - [ ] use **Ctrl + Enter**  
# - [ ] use **Shift + Enter**    

# %%
print('watch for the cat')

# %% [markdown]
# #### Christina's Notebook editing
# - [ ] Edit **this** notebook Markdown cell replacing the word "Student's" above with your name
# - [ ] Run the cell to display the formatted text
# - [ ] Run any 'markdown' cells that are in edit mode, so they are easier to read

# %%
#### [ ] convert \*this\* cell from markdown to a code cell, then run it  
print('Run as a code cell')


# %% [markdown]
# ##  # comments
# create a code comment that identifies this notebook, containing your name and the date

# %%
# Christina Timokhin 
# 02/05/2022

# %% [markdown]
# #### use print() to 
# - [ ] print [**your_name**]
# - [ ] print **is using python!**

# %%
# [ ] print your name
print("Christina Timokhin")
# [ ] print "is using Python"
print("is using Python!")


# %% [markdown]
# Output above should be:  
# `Your Name  
# is using Python!`  

# %% [markdown]
# #### use variables in print()
# - [ ] create a variable **your_name** and assign it a string containing your name
# - [ ] print **your_name**

# %%
# [ ] create a variable your_name and assign it a sting containing your name
christina_timokhin = "Christina Timokhin"
#[ ] print your_name
print(christina_timokhin)


# %% [markdown]
# #### create more string variables
# - **[ ]** create variables as directed below
# - **[ ]** print the variables

# %%
# [ ] create variables and assign values for: favorite_song, shoe_size, lucky_number
favorite_song = "Easy on Me"
shoe_size = "8"
lucky_number = "100"
# [ ] print the value of each variable favorite_song, shoe_size, and lucky_number
print(favorite_song)
print(shoe_size)
print(lucky_number)



# %% [markdown]
# #### use string addition
# - **[ ]**  print the above string variables (favorite_song, shoe_size, lucky_number) combined with a description by using **string addition**
# >for example favorite_song displayed as:  
# `favorite song is happy birthday`

# %%
# [ ] print favorite_song with description
favorite_song = "Easy on Me"
print("favorite song is " + favorite_song)
# [ ] print shoe_size with description
shoe_size = "8"
print("shoe size is " + shoe_size)
# [ ] print lucky_number with description
lucky_number = "100"
print("lucky number is " + lucky_number)


# %%


# %% [markdown]
# ##### more string addition
# - **[ ]** make a single string (sentence) in a variable called favorite_lucky_shoe using **string addition** with favorite_song, shoe_size, lucky_number variables and other strings as needed 
# - **[ ]** print the value of the favorite_lucky_shoe variable string
# > sample output:  
# `For singing happy birthday 8.5 times, you will be fined $25`

# %%
# assign favorite_lucky_shoe using
print("My friend was singing " + favorite_song +" "+ shoe_size + " times " + "with " + lucky_number + " listeners") 



# %% [markdown]
# ### print() art

# %% [markdown]
# #### use `print()` and the asterisk **\*** to create the following shapes
# - [ ] diagonal line  
# - [ ] rectangle  
# - [ ] smiley face

# %%
# [ ] print a diagonal using "*"
print("        *")
print("      *")
print("    *")
print("  *")
print("*")

# [ ] rectangle using "*"
print("****************")
print("*              *")
print("*              *")
print("****************")      

# [ ] smiley using "*"
print("**       **")
print("     *      ")
print("*         *")
print(" *       *")  
print("  ******")



# %% [markdown]
# #### Using `type()`
# -**[ ]** calulate the *type* using `type()`

# %%
# [ ] display the type of 'your name' (use single quotes)
type('Christina Timokhin')



# %%
# [ ] display the type of "save your notebook!" (use double quotes)
type("save your notebook")



# %%
# [ ] display the type of "25" (use quotes)
type("25")



# %%
# [ ] display the type of "save your notebook " + 'your name'
type("save your notebook " + 'Christina Timokhin ')



# %%
# [ ] display the type of 25 (no quotes)
type(25)



# %%
# [ ] display the type of 25 + 10 
type(25 + 10)



# %%
# [ ] display the type of 1.55
type(1.55)



# %%
# [ ] display the type of 1.55 + 25
type(1.55 + 25)



# %% [markdown]
# #### Find the type of variables
# - **[ ]** run the cell below to make the variables available to be used in other code
# - **[ ]** display the data type as directed in the cells that follow

# %%
# assignments ***RUN THIS CELL*** before starting the section

student_name = "Gus"
student_age = 16
student_grade = 3.5
student_id = "ABC-000-000"


# %%
# [ ] display the current type of the variable student_name
type(student_name)



# %%
# [ ] display the type of student_age
type(student_age)



# %%
# [ ] display the type of student_grade
type(student_grade)



# %%
# [ ] display the type of student_age + student_grade
type(student_age + student_grade)



# %%
# [ ] display the current type of student_id
type(student_id)



# %%
# assign new value to student_id 
student_id = 888

# [ ] display the current of student_id
type(student_id)



# %% [markdown]
# #### number integer addition
# 
# - **[ ]** create variables (x, y, z) with integer values

# %%
# [ ] create integer variables (x, y, z) and assign them 1-3 digit integers (no decimals - no quotes)
x = 2 
y = 3 
z = 4

# %% [markdown]
# - **[ ]** insert a **code cell** below
# - **[ ]** create an integer variable named **xyz_sum** equal to the sum of x, y, and z
# - **[ ]** print the value of **xyz_sum** 

# %%
xyz_sum = x + y + z 
print(xyz_sum)

# %% [markdown]
# ### Errors
# - **[ ]** troubleshoot and fix the errors below

# %%
# [ ] fix the error 
#print("Hello World!"")  
print("Hello World!")   


# %%
# [ ] fix the error 
#print(strings have quotes and variables have names)
print("strings have quotes and variables have names")


# %%
# [ ] fix the error 
print("I have $" + '5')



# %%
# [ ] fix the error 
print("always save the notebook")


# %% [markdown]
# ## ASCII art
# - **[ ]** Display first name or initials as ASCII Art
# - **[ ]** Challenge: insert an additional code cell to make an ASCII picture

# %%
# [ ] ASCII ART
print("  ******      ********* ")
print(" **               *")
print(" **               *")
print(" **               *")
print("  ******          *")



# %%
# [ ] ASCII ART
print("    O")
print("   /|\\")
print("    |")
print("   / \ ")



# %% [markdown]
# # Module 1 Practice 2
# ## Strings: input, testing, formatting
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - gather, store and use string `input()`  
# - format `print()` output  
# - test string characteristics  
# - format string output  
# - search for a string in a string  

# %% [markdown]
# ## input()
# getting input from users

# %%
# [ ] get user input for a variable named remind_me
print("Enter reminder:")
remind_me = input()
# [ ] print the value of the variable remind_me
print("Reminder is " + remind_me)

# %%
# [ ] print the value of the variable remind_me
print("Reminder is " + remind_me)

# %%
# use string addition to print "remember: " before the remind_me input string
print("remember: " + remind_me)


# %% [markdown]
# ### Program: Meeting Details
# #### [ ] get user **input** for meeting subject and time
# `what is the meeting subject?: plan for graduation`  
# `what is the meeting time?: 3:00 PM on Monday`  
# 
# #### [ ] print **output** with descriptive labels  
# `Meeting Subject: plan for graduation`  
# `Meeting Time:    3:00 PM on Monday`

# %%
# [ ] get user input for 2 variables: meeting_subject and meeting_time
meeting_subject = input("what is the meeting subject?")
meeting_time = input("what is the meeting time?")
# [ ] use string addition to print meeting subject and time with labels
print("meeting subject:",meeting_subject)
print("meeting time:",meeting_time)




# %% [markdown]
# ## print() formatting 
# ### combining multiple strings separated by commas in the print() function

# %%
# [ ] print the combined strings "Wednesday is" and "in the middle of the week" 
print("Wednesday is","in the middle of the week")


# %%
# [ ] print combined string "Remember to" and the string variable remind_me from input above
print("Remember to",remind_me)


# %%
# [ ] Combine 3 variables from above with multiple strings
print("reminder1:",remind_me,"and",meeting_subject,"at",meeting_time)


# %% [markdown]
# ### print() quotation marks

# %%
# [ ] print a string sentence that will display an Apostrophe (')
print("She said she was 'funny'")



# %%
# [ ] print a string sentence that will display a quote(") or quotes
print('She said it was "funny"')


# %% [markdown]
# ## Boolean string tests

# %% [markdown]
# ### Vehicle tests  
# #### get user input for a variable named vehicle  
# print the following tests results  
# - check True or False if vehicle is All alphabetical characters using .isalpha()  
# - check True or False if vehicle is only All alphabetical & numeric characters  
# - check True or False if vehicle is Capitalized (first letter only)  
# - check True or False if vehicle is All lowercase  
# - **bonus** print description for each test (e.g.- `"All Alpha: True"`)

# %%
# [ ] complete vehicle tests 
vehicle = input("What car do you drive?")
print("you car is",vehicle)
print("Is alpha?",vehicle.isalpha())
print("Is alpha numeric?",vehicle.isalnum())
print("Is first letter Capitilized?",vehicle.istitle())
print("Is it lower case?",vehicle.islower())



# %%
# [ ] print True or False if color starts with "b" 
color = input("What color is my car?")
print("you car color is",color)
print('does the color start with "b"?',color.startswith("b"))

# %% [markdown]
# ## Sting formatting

# %%
# [ ] print the string variable capital_this Capitalizing only the first letter
capitalize_this = "the TIME is Noon."
print(capitalize_this.capitalize())


# %%
# print the string variable swap_this in swapped case
swap_this = "wHO writes LIKE tHIS?"
print(swap_this.swapcase())


# %%
# print the string variable whisper_this in all lowercase
whisper_this = "Can you hear me?"
print(whisper_this.lower())


# %%
# print the string variable yell_this in all UPPERCASE
yell_this = "Can you hear me Now!?"
print(yell_this.upper())


# %%
#format input using .upper(), .lower(), .swapcase, .capitalize()
word = input('enter any word: ')
print("you entered a word:",word)
print("upper:",word.upper())
print("lower:",word.lower())
print("swapcase:",word.swapcase())
print("captial:",word.capitalize())

# %% [markdown]
# ### input() formatting

# %%
# [ ] get user input for a variable named color
# [ ] modify color to be all lowercase and print
color = input("enter color")
print("entered color",color)
print("lowercase:",color.lower())

# %%
# [ ] get user input using variable remind_me and format to all **lowercase** and print
# [ ] test using input with mixed upper and lower cases
remind_me = input("enter reminder")
print("entered reminder",remind_me)
print("lowercase:",remind_me.lower())


# %%
# [] get user input for the variable yell_this and format as a "YELL" to ALL CAPS
yell_this = input("enter 'yell'")
print("uppercase:",yell_this.upper())


# %% [markdown]
# ## "in" keyword
# ### boolean: short_str in long_str

# %%
# [ ] get user input for the name of some animals in the variable animals_input
animals_input = input("enter the name of some animals")

# [ ] print true or false if 'cat' is in the string variable animals_input
print('cat' in animals_input)


# %%
# [ ] get user input for color
color = input("enter the color")

# [ ] print True or False for starts with "b"
print(color.startswith("b"))
# [ ] print color variable value exactly as input 
#     test with input: "Blue", "BLUE", "bLUE"
print(color)




# %% [markdown]
# ## Program: guess what I'm reading
# ### short_str in long_str
# 
# 1. **[ ]** get user **`input`** for a single word describing something that can be read 
#  save in a variable called **can_read**  
#  e.g. - "website", "newspaper", "blog", "textbook"  
#  &nbsp;  
# 2. **[ ]** get user **`input`** for 3 things can be read  
#  save in a variable called **can_read_things**  
# &nbsp;  
# 
# 3. **[ ]** print **`true`** if the **can_read** string is found  
#  **in** the **can_read_things** string variable
# 

# %%
# project: "guess what I'm reading"

# 1[ ] get 1 word input for can_read variable
can_read = input("enter 1 word")

# 2[ ] get 3 things input for can_read_things variable
can_read_things = input("enter 3 things")

# 3[ ] print True if can_read is in can_read_things
print(can_read in can_read_things)

# [] challenge: format the output to read "item found = True" (or false)
# hint: look print formatting exercises
print("item found = ",can_read in can_read_things)


# %% [markdown]
# ## Program: Allergy Check
# 
# 1. **[ ]** get user **`input`** for categories of food eaten in the last 24 hours  
#  save in a variable called **input_test**  
# 
# 2. **[ ]** print **`True`** if "dairy" is in the **input_test** string  
# 3. **[ ]** Test the code so far  
# 4. **[ ]** repeat the process checking the input for "nuts", **challenge** add "Seafood" and "chocolate"  
# 5. **[ ]** Test your code  
#   
# 6. **[ ] challenge:** make your code work for input regardless of case, e.g. - print **`True`** for "Nuts", "NuTs", "NUTS" or "nuts"  
# 

# %%
# Allergy check 
# 1[ ] get input for test
input_test = input("enter food categories")

# 2/3[ ] print True if "dairy" is in the input or False if not
print("Dairy:","dairy" in input_test)

# 4[ ] Check if "nuts" are in the input
print("Nuts:","nuts" in input_test)
# 4+[ ] Challenge: Check if "seafood" is in the input
print("Seafood:","seafood" in input_test)
# 4+[ ] Challenge: Check if "chocolate" is in the input
print("Chocolate:","chocolate" in input_test)

#cheese egg nuts candy sugar 

# %% [markdown]
# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft


