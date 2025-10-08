# [ ] create, call and test the adding_report() function
def adding_report(report_type = "T"):
    ##Takes integer input from the user until they quit, prints total.

    total = 0 ##resets the total sum for each time the function is called.
    items = "" ##resets the string for each time the function is called for the A report.
    print("Input an integer to add to the total or 'Q' to quit")

    while True:
        user_input = input('Enter an integer or "Q" to quit: ') # gets input from the user.

        if user_input.isdigit(): ##checks in input is a digit.
            number = int(user_input) #if the number is a string, cast to integer.
            total += number ##take the number and add it to the total

            if report_type == "A":
                items += user_input + "\n" ##if the report type is A, add the input to items list.
        
        elif user_input.lower().startswith("q"): ##if input is not a digit, check if it is the quit command.

            if report_type == "A": ##If the report type is A, print all of the input integers and the total.
                print("\nItems")
                print(items)
                print("Total")
                print(total)
            else:
                print("\nTotal") ##If the report type is T, or any other type, print only the total.
                print(total)

            print("Calculated by: Benjamin S. Reed")
            break

        else:
            print(f'"{user_input}" is invalid')


print("\n--- Running Report Type 'A' ---")
adding_report("A")

##print("\n\n--- Running Report Type 'T' ---")
##adding_report("T")

