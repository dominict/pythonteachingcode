
def calculate_tx(item,price,tax_rate):
    '''Function to calculate item tax.
    price needs to be float
    tax_rate needs to be float
    returns the item capitalized and the final price'''
    if item == "alcohol":
        tax_rate += .25
    elif item == "cigarette":
        tax_rate += .35
    
    final_price = price + (price * tax_rate)
    return item.capitalize(), final_price


purchase = "frog"    
item, price = calculate_tx(purchase,3.99,.08)
print("Here is the result:",item, round(price,2))
purchase = "alcohol"    
item, price = calculate_tx(purchase,3.99,.08)
print("Here is the result:",item, round(price,2))
purchase = "cigarette"    
item, price = calculate_tx(purchase,3.99,.08)
print("Here is the result:",item, round(price,2))