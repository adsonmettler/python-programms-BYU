# Author: Adson Mettler do Nascimento
# Practice of using list and append function, by adding the names of friends.

friends = []

friends_name = ""

while friends_name != "quit":
    friends_name = input("Type the name of a friend: ")

    if friends_name != "quit":
        friends.append(friends_name)

print()
print("Your friends are:")

for friend in friends:
    print(friend)

