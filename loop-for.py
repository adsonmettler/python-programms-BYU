# Author: Adson Mettler do Nascimento
# FOR LOOPS studies

for i in range(100, 200, 10):
    print(i)

# LOOP within LOOP: outer LOOP and inner LOOP ###

for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f'--{j}')


# Notice how the inner loop is run every time the outer loop displays it's number.
# Inner loops can be very helpful in iterating through a two-dimensional structure,
#such as the pixels in an image.


## ACTIVITY ##

colors = ["red", "blue", "green", "yellow"]

for item in colors:
    print(item)


# for i in range(1, 9):
#     print(i)

# for i in range(2, 21, 2):
#     print(i)

