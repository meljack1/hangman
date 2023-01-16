import random
word_list = ["peach", "strawberry", "raspberry", "pear", "tangerine"]
word = random.choice(word_list)

while True:
    guess = input("What letter would you like to guess?")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
