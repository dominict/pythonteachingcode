
def calculate_tx(this_item,this_price,this_tax_rate):
    '''Function to calculate item tax.
    this_price needs to be float
    this_tax_rate needs to be float
    returns the item capitalized and the final price'''
    if this_item == "alcohol":
        this_tax_rate += .25
    elif this_item == "cigarette":
        this_tax_rate += .35

    final_price = this_price + (this_price * this_tax_rate)
    return this_item.capitalize(), final_price


purchase = "frog"
item, price = calculate_tx(purchase, 3.99, .08)
print("Here is the result:", item, round(price, 2))
purchase = "alcohol"
item, price = calculate_tx(purchase, 3.99, .08)
print("Here is the result:", item, round(price, 2))
purchase = "cigarette"
item, price = calculate_tx(purchase, 3.99, .08)
print("Here is the result:",item, round(price,2))