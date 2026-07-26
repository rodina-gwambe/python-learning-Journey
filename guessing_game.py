#Guess the number game using a while loop
secret_word = "python"

while True: 
    guess = input("Guess the secret word: ").lower()
    if guess == secret_word:
        print("Congratulations! You've guessed the secret word.")
        break
    else: print("Incorrect guess. Try again.")