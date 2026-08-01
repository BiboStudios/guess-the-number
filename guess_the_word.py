import random
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
attempts = 12
print("Welcome to the Guess the Word Game!")
print(f"You have {attempts} attempts to guess the word.")
while attempts > 0:
    guess = input("Enter your guess: ").lower()
    if guess == word:
        print("Congratulations! You've guessed the word correctly!")
        break
    elif len(guess)==1 and guess in word:
        print(f"Good guess! The letter '{guess}' is in the word.")
    else:
        print(f"Sorry, the letter '{guess}' is not in the word.")
    attempts -= 1
    print(f"You have {attempts} attempts left.")
else:
    print(f"Game over! The correct word was '{word}'.")