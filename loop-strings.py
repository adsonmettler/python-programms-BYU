# Author: Adson Mettler do Nascimento
# PRACTICE of "for" loop with numbers and strings mixed using lenght function ###


word = "book"
number_of_letters = len(word)

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")


## ACTIVITY ###


# word = "Commitment"
# favorite_letter = input("\nWhat is your favorite letter? ")

# for letter in word:
#     if letter.lower() == favorite_letter:
#         print(letter.upper(), end="")
#     else:
#         print(letter.lower(), end="")
# print()
# print()

## SECOND PART OF THE ACTIVITY ##

# word = "Commitment"
# favorite_letter = input("What is your favorite letter? ")

# for letter in word:
#     if letter.lower() == favorite_letter:
#         print("_", end="")
#     else:
#         print(letter.lower(), end="")
# print()
# print()


