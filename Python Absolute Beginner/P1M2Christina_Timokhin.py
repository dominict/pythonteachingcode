# [ ] create, call and test fishstore() function 
def fishstore(fish,price):
    return ("Fish Type: "+ fish + " costs $" + price)

fish_entry=input('Enter fish type: ')
price_entry=input('Enter fish type price: ')
print (fishstore(fish_entry,price_entry))