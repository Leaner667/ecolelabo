import os

def clear_screen():
    # Check if the operating system is Windows or Linux
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/macOS

def print_hangman(incorrect_guesses):
    stages = [
        '''
           --------
           |      
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |     
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \|
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \|/
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
           -
        '''
    ]

    if incorrect_guesses < len(stages):
        print(stages[incorrect_guesses])
    else:
        print("You lost! The hangman is fully hanged!")

def print_word(word, guessed_letters):
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '_'
    return display_word

def main():
    word_to_guess = "bastien"  # Replace with the word to guess.
    max_attempts = 6
    guessed_letters = []
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    while True:
        clear_screen()  # Clear the screen before displaying Hangman
        print_hangman(incorrect_guesses)
        print("Word: ", print_word(word_to_guess, guessed_letters))

        if "_" not in print_word(word_to_guess, guessed_letters):
            print("Congratulations! You won!")
            break

        if incorrect_guesses >= max_attempts:
            print("You lost! The word was:", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            incorrect_guesses += 1

if __name__ == "__main__":
    main()
