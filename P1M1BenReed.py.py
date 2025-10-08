# Create name check code

# [ ] get input for input_test variable
input_test = input("Please enter a names of people met in the last 24 hours: ")
# [ ] print "True" message if "John" is in the input or False message if not
print("John".lower() in input_test.lower())

# [ ] print True message if your name is in the input or False if not
my_name = "Ben"
print(my_name.lower() in input_test.lower())

# [ ] Challenge: Check if another person's name is in the input - print message
other_name = "Rhonda"
print(other_name.lower() in input_test.lower())

# [ ] Challenge: Check if a fourth person's name is in the input - print message
fourth_name = "Apple"
print(fourth_name.lower() in input_test.lower())
