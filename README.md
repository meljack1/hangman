# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 2
In this milestone, I have implemented code which creates a list of words assigned to a variable called word_list. 

I have also added functionality for a user to input a letter of their choosing, and validation to check that only a single, alphabetical character has been provided by the user. 

## Milestone 3
In this milestone, I have refactored the code from Milestone 2 which asked for an input and validated it into a function, ask_for_input. 

```
def ask_for_input():
    while True:
        guess = input("What letter would you like to guess?")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
```

This code also makes use of a new function, check_guess. This function checks the guessed character against the letters in the randomly-chosen word, and determines whether it is a correct or incorrect guess. 

``` 
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
```
## Milestone 4
In this milestone, I created a class to manage the Hangman game, redefining the check_guess and ask_for_input functions as methods in the class.

The class can now keep track of letters already guessed in a list, the location of correctly guessed letters in the word, and the number of remaining lives, and updates these as correct and incorrect guesses are made. 

## Milestone 5
In this milestone, I created a function to run and adjudicate a game of hangman. The function will loop, asking for a new letter until your life count is 0, or you have guessed every letter correctly. 

