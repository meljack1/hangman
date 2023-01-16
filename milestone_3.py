while True:
    guess = input("What letter would you like to guess?")
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")