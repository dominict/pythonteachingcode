# [] create words after "G" following the Assignment requirements use of functions, methods and keywords
# Sample quote: "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)

def word_after_g():

    quote = input("Welcome, Ben Reed. Enter a 1 sentence quote, non_alpha seperate words: ")
    word = ""

    for character in quote:
        if character.isalpha():
            word += character
        else:
            if word:
                if word[0].lower() > "g":
                    print(word.upper())
                word = ""

    if word:
        if word[0].lower() >"g":
            print(word.upper())

word_after_g()