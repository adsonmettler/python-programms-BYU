
# Adventure Game project W03 CSE 110
# made by Adson Mettler do Nascimento

# As exceeding activity I added a loop using the WHILE condition.
# The condition for loops are checked, and the loop continue to execute as long as the condition are met.

# Sharing experience COMMENT:
# It was a big challenge! I loved the experience! After I thought was ready the code, I shared with friends, 
# then while the were running the game, I found an error in my loop condition. It was great to share for testing all possibilities.

print('\n\n\nWELCOME TO SPACE ADVENTURE GAME!\n')

while True:
    print('\nYou were left behind in a unexplored planet,')
    print('you face two options at that moment:')
    print('STAY where you are or EXPLORE planet resources.')
    stay_explore = input("Which one do you want to pick, STAY or EXPLORE?\n")
    
    if stay_explore.lower() == 'stay':
        print('\nYou realized that in the shelter you have food for 1 month')
        print('and oxigen for 3 months. As a trainned space explorer')
        print('you know that you need to croop to have food.')
        bean_potato = input("Wich kind of food you will plant, BEAN or POTATO?\n")
        
        if bean_potato.lower() == 'bean':
            print('\nAfter some days you were able to settle everything and started growing bean.')
            print('Now, you know that you have to decide between some priorities.')
            print('Create oxigen for future survival, or set your computer and transponder')
            print('to establish communication with any space station and ask for help,')
            print('or explore the planet to see if you have more survivel resources available.')
            oxygen_communication_explore = input("Which one is your priority, OXYGEN, COMMUNICATION, or EXPLORE?\n")
            if oxygen_communication_explore.lower() == 'oxygen':
                print('\nAfter a month you were able to grow beans enough to start eating them and storage.')
                print('And you found a scientific way to create oxigen, it is a slow process but you did.')
                print("Congratulations you are the first inhabitant of that planet!")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            elif oxygen_communication_explore.lower() == 'communication':
                print('\nYou started looking for the conditions of the transponder and noticed that is broken')
                print('due to last storm you faced. You had to invest couple of weeks to fix the problem,')
                print('connect to your computer and establish safe sign connection to send message into open space.')
                print("Now you are wating for any reply to share your coordinates for rescue. Good job!")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            elif oxygen_communication_explore.lower() == 'explore':
                print('\nYou took the car available and started to explore around into west direction.')
                print('You have found water. You picked and put in the empty containers you found in the car.')
                print('While you were doing that you were approached by the native inhabitants and')
                print("they arrested into their jail for interrogation. What a bad luck!")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            else:
                print("\nPlease, insert a valid option! Go back to the begining.")
            print()

        elif bean_potato.lower() == 'potato':
            print('\nYou prepared and settle everything needed to grow potatos.')
            print('Later on, as an space scientist you know that you need to')
            print('figure out somethings, the communication tools for asking for')
            print('help, the oxigen shortage, and you know that exploring around')
            print('to understand the biome and weather is important too.')
            oxygen_communication_explore = input("What will be your priority, COMMUNICATION, OXYGEN, or EXPLORE?\n")

            if oxygen_communication_explore.lower() == 'oxygen':
                print('\nAs a scientist it was not hard for you to build a lab in the shelter')
                print('and produce your own resource of oxygen, however the process of oxygen')
                print('generation is very slow. After a month you noticed that your potatos')
                print('are growing well. Unfortunately a big storm came and washed all your croop.')
                print("Bad luck, now you have to rebuild everything.")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            elif oxygen_communication_explore.lower() == 'communication':
                print('\nYour potatos are growing well, in the meanwhile you are fixed')
                print('the transponder, conneceted to your computer, and sent a')
                print("message of rescue to the closest space station with your")
                print('coordenates. Congratulations, you will be rescued.')
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            elif oxygen_communication_explore.lower() == 'explore':
                print('\nYou noticed that you have a jetpack inside the shelter,')
                print('you took and went outdoor to explore. After two hours')
                print('of exploring you found a village of native inhabitants,')
                print('they saw you and they shot down you and arrested to')
                print("the jail for interrogation.")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            else:
                print("\nPlease, insert a valid option! Go back to the begining.")
            print()
        else:
            print("\nPlease, insert a valid option! Go back to the begining.")

    elif stay_explore.lower() == 'explore':
        print("\nYou realized that you have a very robust car made for that planet conditions,")
        print("after checking the car you noticed that the maximo speed of the car is 40 Km/Hour")
        print("with autonomy of 15 hours. Looking around you found a jetpack, which has a maximo")
        print("speed of 120 Km/Hour with autonomy of 5 hours. What is your choice")
        car_jetpack = input("to explore the planet, CAR or JETPACK? ")
        if car_jetpack.lower() == 'car':
            print("\nAfter around 80 Km you found a flat land with water resource,")
            print("trees with many kind of fruits, and big animals eating fruits")
            print("from the tree. What is your next action? Which resource")
            water_fruit_hunt = input("you pick, WATER, FRUIT, or HUNT? ")
            if water_fruit_hunt.lower() == 'water':
                print("\nYou got the containers you found inside the car and started taking water.")
                print("Suddenly you were atacked by a big animal that was around hunting and looking for food.")
                print("What a bad luck.")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            elif water_fruit_hunt.lower() == 'fruit':
                print("\nAs soon as you approached the tree all the animals ran away.")
                print("And you pick the fruits and put in the container that you took from inside the car.")
                print("Congratulations, you found a great resource of food to survive and become the first")
                print("human living in that planet!")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            elif water_fruit_hunt.lower() == 'hunt':
                print("\nYou noticed that you have a gun inside the car. You sneaky approach the animals")
                print("and shot down one of them. You put the animal in a big container you found in")
                print("the car. In the meanwhile you are approached by native inhabitants who heard the gun noise.")
                print("They arrested you into a jail for interrogation.")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            else:
                print("\nPlease, insert a valid option! Go back to the begining.")
            print()

        elif car_jetpack.lower() == 'jetpack':
            print("\nAfter 2 hours fliying to east you found a village of native inhabitants.")
            print("You are suprised, and thinking what to do, if you get back to the shelter,")
            print("or try to approach them, or just ignore and explore more. What is your")
            getback_approach_explore = input("decision, GET BACK, APPROACH, or EXPLORE? ")
            if getback_approach_explore.lower() == 'get back':
                print("\nAs soon as you got back into the shelter, you noticed that a big storm is comming.")
                print("You make sure everything is safe inside. But when the storm reached you everything was")
                print("destroyed. You found yourself lost and without shelter and resources. What a bad luck!")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            elif getback_approach_explore.lower() == 'approach':
                print("\nYou got down and walked into the village direction. The natives started to talk in a unkown")
                print("language, but they seems friendly. After 2 hours with them a big storm reached the village,")
                print("and because of the natives expertise everything went well and you are safe. Contratulations,")
                print("now you are the first human to inhabitant this planet!")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            elif getback_approach_explore.lower() == 'explore':
                print("\nYou went further into east direction and suddenly a big storm reached you and were not")
                print("able to handle that and felt down. You got very hurt, your jetpack broke, and you got lost.")
                print("What a bad luck!")
                print()
                play_again = input("Would you like to play again? Type YES or NO: ")
                if play_again.lower() == 'yes':
                    play_again.lower() == True
                elif play_again.lower() == 'no':
                    break
                else:
                    print("\nSorry, not valid answer.")
                    break
            else:
                print("\nPlease, insert a valid option! Go back to the begining.")
            print()
        else:
            print("\nPlease, insert a valid option! Go back to the begining.")

    else:
        print("\nPlease, insert a valid option! Go back to the begining.")


