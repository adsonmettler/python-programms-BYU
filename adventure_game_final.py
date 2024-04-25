"""
Author: Anderson Mettler do Nascimento

Creative addition: I added while loops to force the user to give a valid answer.
I also added a main while loop that keeps the program running if the user answers
'wake up' on the last question. This way we can keep the program running and test
all the possible scenarios without the necessity of restarting the program.
"""

print('\n\n\n WELCOME TO ADVENTURE GAME\n')

choice = 'wake up'

while choice == 'wake up':

    print('\nOn a hot summer morning, you wake up very thirsty.')
    print('You go to the kitchen and open the fridge.')
    print('There you find COLD WATER and MILK.')
    drink = input('Which one do you drink? (COLD WATER or MILK)\n').lower()

    while drink not in ('cold water', 'milk'):
        drink = input('\nInvalid Option! Please answer COLD WATER or MILK.\n').lower()

    if drink == 'cold water':
        print('\nAs soon as you start to drink the COLD WATER,')
        print('it begins to rain heavily inside your kitchen.')
        print('The more you drink the heavier it rains.')
        print('Once you finish drinking you notice the kitchen is flooding.')
        print('You can start to SWIM or you can CLIMB the fridge.')
        action = input('What action do you take? (SWIM or CLIMB)\n').lower()

        while action not in ('swim', 'climb'):
            action = input('\nInvalid Option! Please answer SWIM or CLIMB.\n').lower()

        if action == 'swim':
            print('\nAs you start to SWIM in the cold water, you notice')
            print('you are in deep waters. Underneath you lies a wrecked')
            print('pirate ship. You can swim to the PIRATE SHIP or you can')
            print('scream AHOY. You can also realize this is a crazy dream')
            print('and try to WAKE UP.')
            choice = input('What is your choice? (PIRATE SHIP, AHOY or WAKE UP)\n').lower()

            while choice not in ('pirate ship', 'ahoy', 'wake up'):
                choice = input('\nInvalid Option! Please answer PIRATE SHIP, AHOY or WAKE UP.\n').lower()

            if choice == 'pirate ship':
                print('\nYou swim deeper and deeper towards the PIRATE SHIP.')
                print('Once you get there, to your amazement, you find a')
                print('treasure chest. You cannot hold the excitement. You')
                print('quickly open the chest and in there, you find amidst')
                print('some gold coins, the PERFECT grade on the assignment!\n')
            elif choice == 'ahoy':
                print('\nYou scream AHOY three times and the spirit of the Old')
                print('Parrot of the Sea appears to you. Flying still like a hummingbird')
                print('it says in its parrot voice: “AHOY mate, I predict that you will')
                print('get a PERFECT grade on the assignment!”\n')

        else:
            print('\nAs you start to CLIMB the fridge, you accidentally')
            print('open the freezer door. A chilly wind comes rushing out.')
            print('The rain turns to snow and the flood water freezes immediately.')
            print('You can build a SNOWMAN or you can ICE SKATE. You can also')
            print('realize this is a crazy dream and try to WAKE UP.')
            choice = input('What is your choice? (SNOWMAN, ICE SKATE or WAKE UP)\n').lower()

            while choice not in ('snowman', 'ice skate', 'wake up'):
                choice = input('\nInvalid Option! Please answer SNOWMAN, ICE SKATE or WAKE UP.\n').lower()

            if choice == 'snowman':
                print('\nYou have a lot fun building a very large SNOWMAN.')
                print('but then, to your amazement, the SNOWMAN gains a')
                print('life of its own. It starts to walk menacingly in your direction,')
                print('then it smiles at you and says: “Thank you for building me!')
                print('I predict that you will get a PERFECT grade on the assignment!\n')
            elif choice == 'ice skate':
                print('\nYou have a lot of fun ICE SKATING in the kitchen.')
                print('Once you finish, to your amazement, the fridge, the stove, all')
                print('kitchen appliances, and the cabinets start to applaud. Then they')
                print('shout in one accord: “Bravo! You are amazing! We predict that')
                print('you will get a PERFECT grade on the assignment!”\n')

    else:
        print('\nAs soon as you start to drink the MILK,')
        print('a black and white MILK cow enters your kitchen.')
        print('It screams at you in a loud and squeaky voice:')
        print('"That belongs to my babies!" You look at this peculiar')
        print('scene with a puzzled face. In response, the cow pulls a')
        print('straw hat and a banjo from behind the door and starts')
        print('to sing a very sad song about two hungry calves. You can')
        print('start to CRY filled with emotion, or you can pull out your own')
        print('BANJO from the fridge so you can sing in response.')
        action = input('What action do you take? (CRY or BANJO)\n').lower()

        while action not in ('cry', 'banjo'):
            action = input('\nInvalid Option! Please answer CRY or BANJO.\n').lower()

        if action == 'cry':
            print('\nThe song is really sad and you cannot stop thinking about')
            print('those two, poor, hungry calves. So you CRY and CRY.')
            print('You CRY like never before. Never before, indeed! Those')
            print('are not regular tears coming out of your eyes. You are')
            print('pouring streams of MILK from your eyes. Now you can')
            print('MOO loudly like a cow, or you can open a DAIRY BUSINESS.')
            print('You can also realize this is a crazy dream and try to WAKE UP.')
            choice = input('What is your choice? (MOO, DAIRY BUSINESS or WAKE UP)\n').lower()

            while choice not in ('moo', 'dairy business', 'wake up'):
                choice = input('\nInvalid Option! Please answer MOO, DAIRY BUSINESS or WAKE UP.\n').lower()

            if choice == 'moo':
                print('\nYou MOO like a cow, as MILK streams from your eyes. Two')
                print('very skinny calves come running-in in answer to your call.')
                print('They see the MILK coming from your eye and immediately')
                print('start to drink it to quench their hunger. As they drink')
                print('MILK nonstop, they start to get fatter. The cow is so glad')
                print('with this scene that it stops singing and exclaims: “May the')
                print('grader of this task bless you with a PERFECT grade!\n')
            elif choice == 'dairy business':
                print('\nNow that you have an endless source of MILK you decide to open')
                print('a DAIRY BUSINESS. "Moovellous!" exclaims the musical cow, tapping')
                print('its hoof in approval. Soon, your dairy delights become legend. So')
                print('the next time the graders of this task eat any dairy product, they')
                print('will remember to give a PERFECT grade.\n')

        else:
            print('\nYou pull out your old and faithful BANJO from the fridge and')
            print('join in the unusual kitchen concert. The surreal duet between')
            print('you and the singing cow creates an odd harmony that echoes')
            print('through your home. Now you can SING ALONG with the cow, or')
            print('you can initiate a SINGING BATTLE. You can also realize this')
            print('is a crazy dream and try to WAKE UP.')
            choice = input('What is your choice? (SING ALONG, SINGING BATTLE or WAKE UP)\n').lower()

            while choice not in ('sing along', 'singing battle', 'wake up'):
                choice = input('\nInvalid Option! Please answer SING ALONG, SINGING BATTLE or WAKE UP.\n').lower()

            if choice == 'sing along':
                print('\nWhile you and the cow SING ALONG the two very skinny calves')
                print('the song talks about enter the kitchen. They are very moved that')
                print('you are singing such a nice tune about them. So they too join the')
                print('singing. You all sing your hearts out. The singing makes the calves')
                print('forget about their hunger. So at the end of the song they “We hope')
                print('you get a PERFECT grade on the assignment!”\n')
            elif choice == 'singing battle':
                print('\nThe cow sings a verse, then you sing a verse in response. Thus a')
                print('SINGING BATTLE begins. One verse after another, you both sing')
                print('with an ever-increasing fervor. Soon people start coming to your')
                print('home and streaming the singing all over the internet. You and the')
                print('cow become famous and everyone says your singing is PERFECT,')
                print('just as the grade this task should receive.\n')
