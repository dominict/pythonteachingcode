# %% [markdown]
# # Module 2 Practice
# ## Functions Arguments & Parameters
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - **create functions with a parameter**  
# - **create functions with a `return` value** 
# - **create functions with multiple parameters**
# - **use knowledge of sequence in coding tasks**  
# - **use coding best practices** 

# %% [markdown]
# ## &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Tasks</B></font>

# %%
# [ ] define and call a function short_rhyme() that prints a 2 line rhyme
def short_ryme():
   print("Once I dive into these pages,")
   print("I may not come out for ages.")
short_ryme()

# %%
# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case
def title_it(msg):
    print(msg.title())

title_it(" my name is christinA ")

# %%
# [ ] get user input with prompt "what is the title?" 
# [ ] call title_it() using input for the string argument
user_input=input("what is the title?")
title_it(user_input)

# %%
# [ ] define title_it_rtn() which returns a titled string instead of printing
# [ ] call title_it_rtn() using input for the string argumetnt and print the result
def title_it_rtn(msg):
   return msg.title()

user_input = input("what is the title?")
titled = title_it_rtn(user_input)
print(titled)

# %% [markdown]
# ## Program: bookstore()
# create and test bookstore()
# - **bookstore() takes 2 string arguments: book & price**
# - **bookstore returns a string in sentence form** 
# - **bookstore() should call title_it_rtn()** with book parameter  
# - **gather input for book_entry and price_entry to use in calling bookstore()**
# - **print the return value of bookstore()**
# >example of output: **`Title: The Adventures Of Sherlock Holmes, costs $12.99`**

# %%
# [ ] create, call and test bookstore() function
def bookstore(book, price):
    return title_it_rtn(book) + ", costs " + price 

book_entry = input("what is the book title?")
price_entry = input("what is the book price?")
output = bookstore(book_entry, price_entry)
print("Title: " + output)


# %% [markdown]
# ### Fix the error

# %%
def make_greeting(name, greeting = "Hello"):
    return (greeting + " " + name + "!")

# get name and greeting, send to make_greeting 

def get_name():
    name_entry = input("enter a name: ")
    return name_entry

def get_greeting():
    greeting_entry = input("enter a greeting: ")
    return greeting_entry

#moved make greeting and other function calls after their defintions
print(make_greeting(get_name(), get_greeting()))



# %% [markdown]
# 
# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft


