import random
word_list = ["peach", "strawberry", "raspberry", "pear", "tangerine"]

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.num_letters = len(set([c for c in self.word]))
        self.word_guessed = [c if c in self.list_of_guesses else "_" for c in self.word]

def ask_for_input():
    while True:
        guess = input("What letter would you like to guess?")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
