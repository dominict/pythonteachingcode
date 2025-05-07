# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
# [] copy and paste in edX assignment page
quote = input("enter a 1 sentence quote, non-alpha separate words: ")

word = ""
position = 0
end = len(quote)

while position <= end:
    if position == end and word[0] >= 'h':
         print(word.upper())
         
         break
    
    letter = quote[position]
    
    if letter.isalpha():
        word += letter.lower()
        
    elif len(word) > 0 and word[0] >= 'h':
        print(word.upper())
        word = ""
    else: 
        word = ""

    position += 1