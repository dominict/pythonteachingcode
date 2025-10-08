# [ ] create, call and test the str_analysis() function  

def str_analysis(text):
    if text.isdigit():
        number = int(text)
        if number > 99:
            return f'{number} is a big number'
        else:
            return f'{number} is a small number'
    elif text.isalpha():
        return f'{text} is all alpha'
    else:
        return f'{text} has mutiple character types'

while True:

    user_input = input("Benjamin Reed, enter word or integer: ")

    if user_input:
        break

analysis_message = str_analysis(user_input)

print(analysis_message)
