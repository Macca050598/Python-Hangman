import random

def hangman():
    lives = 7
    word = computersWord()
    wordlength = ['_'] * len(word)
    guessedLetters = set()
    print("The word to guess is:", " ".join(wordlength))

    while lives > 0 and "_" in wordlength:
        letterGuess = usersGuess()

        if letterGuess in guessedLetters:
            print("Uh oh, you've already guessed this letter.")
            continue

        guessedLetters.add(letterGuess)

        if letterGuess.lower() in word.lower():
            for i, char in enumerate(word):
                if char.lower() == letterGuess.lower():
                    wordlength[i] = char
            print("Correct! The word now looks like:", " ".join(wordlength))
        else:
            lives -= 1
            print(f"Incorrect! You have {lives} lives left.")

    if "_" not in wordlength:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Game over! The word was {word}.")

def usersGuess():
    return input("Please choose a letter: ").lower()

def computersWord():
    words = ["Apple", "Pear", "Car", "Person", "Computer", "Friend"]
    return random.choice(words)

def main():
    hangman()

if __name__ == "__main__":
    main()
