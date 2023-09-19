#this code i use chatGPT to do it and i use sentence :”make a game for children in python”
import random

def choose_word():
    words = ["apple", "banana", "cherry", "dog", "elephant", "flower", "giraffe", "hamburger", "igloo", "jellyfish"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Welcome to Hangman!")
    secret_word = choose_word()  # Select a random word from the list
    guessed_letters = []         # List to store guessed letters
    attempts = 6                 # Number of attempts allowed
    
    while True:
        print(display_word(secret_word, guessed_letters))  # Display the current state of the word
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print("Good guess!")
        else:
            print("Wrong guess.")
            attempts -= 1
        
        if "_" not in display_word(secret_word, guessed_letters):
            print(f"Congratulations! You guessed the word '{secret_word}'!")
            break
        
        print(f"Attempts left: {attempts}")
        
        if attempts == 0:
            print(f"Game over! The word was '{secret_word}'.")
            break

if __name__ == "__main__":
    main()


#Save this code in a Python file (e.g., hangman_game.py) and run it using a Python interpreter.
