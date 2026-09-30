import random

# Predefined word list
words = ["python", "hangman", "coding", "program", "debug"]

# Pick a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = set()

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord: " + " ".join(guessed))
    print(f"Attempts left: {attempts}")
    print(f"Used letters: {', '.join(sorted(used_letters))}")
    
    guess = input("Guess a letter: ").lower()
    
    if guess in used_letters:
        print("You already guessed that letter.")
        continue
    
    used_letters.add(guess)
    
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print("Wrong guess!")
        
# End of game
if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over! The word was:", word)
