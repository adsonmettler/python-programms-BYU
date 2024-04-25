
# Word Puzzle Game project W04 CSE 110
# Made by: Adson Mettler do Nascimento

## EXCEEDING ##
## INSTRUCTIONS OF THE GAME added ##
# 1. An underscore _ indicates that the letter was not present in the secret word.
# 2. A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.
# 3. An uppercase letter indicates that the letter was present at that exact spot in the secret word.
# 4. A hint that the secret word is a person from The Book of Mormon.


print()
print("Welcome to the word guessing game!")
print()
print("Here is the overall instructions:\n")
print("1. An underscore _ indicates that the letter was not present in the secret word.")
print("2. A lowercase letter indicates that the letter was present somewhere in the")
print("secret word, but not at that position.")
print("3. An uppercase letter indicates that the letter was present at that exact spot")
print("in the secret word.")
print()
print("Are you ready?! Here we go! Hint: I need this for a digital marketing campaign.")
print()
secret_word = "website"
print("Your hint is:", " _ " * len(secret_word))
user_guess = input("What is your guess? ")
guess_count = 1
hint = " _ " * len(secret_word)


while user_guess.lower() != secret_word:
    if len(user_guess) != len(secret_word):
        print("Your guess must have the same number of letters as the secret word.")
    else:
        print("Your guess was not corret.")
        
        hint = ""
        for i in range(len(secret_word)):
            if user_guess.lower()[i] == secret_word[i]:
                hint += user_guess[i].upper()
            elif user_guess.lower()[i] in secret_word:
                hint += user_guess[i].lower()
            else:
                hint += "_"
        
        print("Your hint is:", hint)

    user_guess = input("What is your guess? ")
    guess_count += 1

print("Congratulations! You guessed it!")
print("It took you", guess_count,"guesses.")
