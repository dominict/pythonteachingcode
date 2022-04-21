# [ ] create, call and test the str_analysis() function  
def str_analysis(input_string):
    if input_string.isdigit(): # If input only includes numeric values.
        inputInt = int(input_string) # Converts str to int

        if inputInt > 99: # Greater than 99
            return str(inputInt) + " is a big number."
        else: # Less than than 99
            return str(inputInt) + " is a small number."
    else: # If input is not a digit
        if input_string.isalpha(): # Only alphabetic characters
            return input_string + " is all alphabetic characters."
        else: # Multiple character types
            return input_string + " is all multiple character types."

print("Testing the Code \n---") 
while True:
    user_input = input("Enter string for testing: ") 
    if user_input == "": 
        print("")
    else: 
        print(str_analysis(user_input)) 
        break



