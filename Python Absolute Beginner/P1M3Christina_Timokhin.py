# [ ] create, call and test 
min_order_weight = 12
max_order_weight = 15
price = 4

print("Cheese Order:")

def cheese_order():
    order_amount = float(input("Enter cheese order weight (numeric value): " ))

    if order_amount < min_order_weight:
        belowErr = str(order_amount) + " is below the minimum order amount"
        return(belowErr)
    elif order_amount > max_order_weight:
        aboveErr = str(order_amount) + " is more than currently available stock"
        return(aboveErr)
    else:
        total = order_amount * price
        finalStr = str(order_amount) + " pounds cost $" + str(total) 
        return finalStr

resultStr = cheese_order()
print(resultStr)