def calculate_tax(total,location,rate):
    if location == "B":
        rate += .01
    tax = total * rate
    return tax

# i need to "call" the function to get it to actually do something
this_total = 5.50
taxed_on_total = calculate_tax(this_total,"B",.08)
shipping = 7
print("Your total is $"+str(round(this_total+taxed_on_total+shipping,2))+".")
