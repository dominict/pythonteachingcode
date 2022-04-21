correctNames = []
incorrectNames = []

def get_names():
    #get_ipython().system(u' curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elementsl_20.txt')
    
    # get 5 guesses from the user
    print("list any 5 of the first 20 elements in the Period table: ")
    
    elements_file = open('/Users/cnt2019/elementsl_20.txt', 'r')
    all_elements = elements_file.readlines()
    
    first5 = all_elements[0:5]
    
    first5 = [x.lower().strip() for x in first5]
    
    count = 0
    scores = []
   
    while count < 5:
        guess = input("Enter the name of an element: ").lower().strip()
        if (guess in correctNames) | (guess in incorrectNames):
            print(guess, " was already entered.  <--- ")
        else: 
            count += 1
        
            if guess in first5: 
                scores.append("p")
                correctNames.append(guess)
            else:
                scores.append("f")
                incorrectNames.append(guess)
    
    return scores

    
collectedScores = get_names()
passCount = collectedScores.count("p")
print((passCount * 20), "% correct")
print("Found:", correctNames)
print("Not Found: ", incorrectNames)