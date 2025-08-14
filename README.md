# Python Teaching Code
This repository ("repo") contains a variety of starter project code and demo code for showing different capabilities and how to use them in Python.

Begin by forking this repository to your own Github account. Next, you can clone it to your machine and run the examples and customize the code. If you do not fork it first, you will not be able to save changes, as you do not have permission to change this original template in my account.

The projects included here include working code and some experimental code. Some also require additional libraries and capabilities on your computer in order for you to use them. Those are noted below.

1. Gradetracker
> This project is a simple demonstration of an application in fewer than 100 lines of code. You can see functions and other capabilities used here. The code requires the built-in statistics library to be imported. It should run on any version of Python 3.
2. KSU scrape
> This project demonstrates how Python can be used to grab data from a web page and process it into orderly results that can be used for further analysis and actions. It requires several add-on libraries. You will especially need to install the beautiful soup library and the lxml parser library in order to use this code. The command line command for installing is '''pip install bs4''' This may work for you. Otherwise, you may need to try '''python -m pip install bs4''' On a Mac, you will need to guide the install to your Python 3 installation, since Macs also already have Python 2 associated with the command '''python''' by default. So, you would run '''pip3 install bs4'''. Similarly, you can install other modules by putting their official name instead of '''bs4''' in the preceding commands. For more info, watch https://www.youtube.com/watch?v=jnpC_Ib_lbc.
3. calcGUI
> This project shows you a Python application working in a graphical user interface window with buttons and bindings to your keyboard keys. It should work on all Python 3.6 or newer versions, because they have the GUI library tkinter pre-installed. This demo will not run in a web browser or Jupyter code editor, because those editors do not have access to the Display properties of your computer. You need to run it in Visual Studio Code or another method directly on your computer for it to work.
4. DB in Python
> This project demonstrates how to connect Python to a local SQLite file and a MySQL database server. The SQLite part will run on your local machine (SQLite is built in to Python by default). The MySQL part requires that you download and install MySQL server on your local machine first (or you can setup an online instance and connect to it for more advanced users). Next, you have to import the database of student data (.sql file) into your MySQL server. Then, you need to edit the code to use the password for your MySQL server on your machine and install and import the library to connect to MySQL. Then, it can work! There is also a folder here with experimental code for transforming gradetracker into GUI and DB-driven versions. These may not work, but you are welcome to test them and upgrade them.
5. RaspberryPi button
> This project requires some wiring as well as a RaspberryPi computer and associated peripherals. You can simulate a RaspberryPi on your computer using an extension in Visual Studio Code. Search the Extensions library for a current one.
6. Web Page with Flask
> This project requires that you install the flask module. After that, when you run it, it will create a web server on your machine and host your Python and HTML files in dynamic web pages. This demo will not run in a web browser or Jupyter code editor, because those editors do not have access to the operating system properties of your computer. You need to run it in Visual Studio Code or another method directly on your computer for it to work.
7. Data Analytics with Jupyter and Pandas
> COMING SOON
