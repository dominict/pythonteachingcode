# [ ] create, call and test the adding_report() function

def adding_report(report): #define the `adding_report` function with one parameter `report` that will be a string with default of "T"  
	#report="T"
	total=0  
	items="book" 
 
	#- inside the function build a forever loop (infinite while loop) and inside the loop complete the following  
	while True:
		#- use a variable to gather input (integer or "Q")  
		variable=input("Input an integer to add to the total or \"Q\" to quit\n")
		# check if the input string is a digit (integer) and if it is then do the below...  

		if variable.isdigit():
			items=(items+"\n"+variable)
			variable=int(variable)

			total=total+variable #add input iteger (NOT STRING) to total 
	#if report type is "A" add the number characters to the item string seperated by a new line! Do not forget the new line!   
		elif variable=="Q":
			if report=="A":
				print("Items")
				print(items)
				print ("Total: \n ", total)
			if report=="T":
				print ("TOTAL: ", total)
			break
		else:
				print("input is invalid")

    #Do the while True belo0w then print the answer and run it 
while True:

	intrada=input("enter \'A\' for complete report, or \"T\" just for the total report")
	if intrada=="A" or intrada=="T":
		break
	else:
		print("error, A or T")


adding_report(intrada)