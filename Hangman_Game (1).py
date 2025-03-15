import random

def choose_word():
    # A list of words to choose from
    words = ["python", "java", "hangman", "programming", "developer", "computer", "algorithm", "function"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with underscores for unguessed letters
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def print_hangman(incorrect_guesses):
    # Hangman art for each incorrect guess
    hangman_stages = [
        '''
           ------
           |    |
                |
                |
                |
                |
        ============
        ''',
        '''
           ------
           |    |
           O    |
                |
                |
                |
        ============
        ''',
        '''
           ------
           |    |
           O    |
           |    |
                |
                |
        ============
        ''',
        '''
           ------
           |    |
           O    |
          /|    |
                |
                |
        ============
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        ============
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        ============
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        ============
        '''
    ]
    print(hangman_stages[incorrect_guesses])

def hangman():
    # Choose a random word
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Maximum number of incorrect guesses allowed
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print_hangman(incorrect_guesses)
        print("\nWord to guess:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        # Get the player's guess
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        # If the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)
        
        # Check if the guess is correct
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
        
        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print_hangman(incorrect_guesses)
        print(f"\nGame Over! You've used all your guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()