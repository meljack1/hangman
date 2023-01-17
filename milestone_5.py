import random
word_list = ["peach", "strawberry", "raspberry", "pear", "tangerine"]
num_lives = 5

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.num_letters = len(set([c for c in self.word]))
        self.word_guessed = [c if c in self.list_of_guesses else "_" for c in self.word]
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
            print(f"Good guess! {guess} is in the word.")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess.lower())
    def ask_for_input(self):
        while True:
            guess = input("What letter would you like to guess? ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess.lower() in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break

def play_game(word_list):
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters <= 0:
            print("Congratulations. You won the game!")
            break

play_game(word_list)