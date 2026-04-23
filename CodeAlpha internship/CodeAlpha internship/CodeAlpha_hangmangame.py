import random

# Predefined list of words
words = ["python", "hangman", "coding", "random", "loops"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Create hidden version of the word
display_word = ["_"] * len(word)

print("Welcome! guess the word")
print("you have 6 incorrect guesses allowed.\n")

# Game loop
while incorrect_guesses < max_guesses and "_" in display_word:
    print("Word:", " ".join(display_word))
    guess = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check if guess is in the word
    if guess in word:
        print("Correct!\n")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong! Incorrect guesses left: {max_guesses - incorrect_guesses}\n")

# End of game
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
