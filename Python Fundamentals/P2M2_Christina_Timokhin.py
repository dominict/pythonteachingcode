# [] create list-o-matic
# [] copy and paste in edX assignment page
def list_o_matic(input_string, input_list):
    if input_string == "":
        return print(input_list.pop(), "popped from list")
    else:
        if input_string in input_list:
            input_list.remove(input_string)
            return print(input_string, "removed from list")

        else:
            input_list.append(input_string)
            return print("1 instance of", input_string, "appended to list")


check_list = ['cat', 'goat', 'chicken', 'horse']

while check_list:
    check_string = input("enter the name of an animal or Quit for quit:")
    if check_string.lower() == "quit":
        break
    else:
        list_o_matic(check_string, check_list)
