# [ ] create, call and test fishstore() function 
def fishstore(fish, price):
    # Returns a string in sentence form
    return "Fish Type: " + fish + " costs $" + price
fish_entry = input("Enter the fish type: ")
price_entry = input("Enter the price: ")
report = fishstore(fish_entry, price_entry)
print("Report for Matthew Williams. " + report)
