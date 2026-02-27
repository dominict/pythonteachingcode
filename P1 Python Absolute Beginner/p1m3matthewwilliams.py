# [ ] create fucntion, call and test 
def cheese_program(order_amount, max_amount=100.0, min_amount=0.5, price=7.99):
    order_amount = float(order_amount)
    max_amount = float(max_amount)
    min_amount = float(min_amount)
    if order_amount > max_amount:
        print(f"{order_amount} is more than currently available stock")
    elif order_amount < min_amount:
        print(f"{order_amount} is below minimum order amount")
    else:
        total_cost = order_amount * price
        print(f"{order_amount} costs ${total_cost:.2f}")

name = "Matthew Williams"
user_weight = input(f"{name}, enter cheese order weight (numeric value): ")

cheese_program(user_weight)
