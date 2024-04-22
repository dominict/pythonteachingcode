'''
This is a file full of functions examples.
'''

def calculate_bmi(height, weight, units="standard"):
    '''
    This function calculates BMI and returns the value. It expects height in inches and weight in pounds.
    Change units to metric if metric. Then input KG and Meters.
    '''

    if units == "standard":
        bmi = (weight/(height*height))*703
    else:
        bmi = weight/(height*height)
    return bmi

print("standard case: ",calculate_bmi(62,138))

print("metric case: ",calculate_bmi(1.575,62.596,"metric"))