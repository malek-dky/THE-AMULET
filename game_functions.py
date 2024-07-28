import time
import random

score = 10


def update_score(points):
    global score
    score += points
    print(f"\nCurrent score: {score}")
    if score <= 0:
        print("You have lost all your points. Restarting the game...\n")
        score = 10
        start_narr()


def start_narr():
    global score
    score = 10  # Reset score at the beginning

    print("\nIn the kingdom of Elaria")
    time.sleep(3)
    print("legends speak of an ancient amulet hidden deep within the")
    time.sleep(2.5)
    print("enchanted forest of Eldoria.")
    time.sleep(2.5)
    print("This amulet is said to grant immense power and wisdom to its bearer.")
    time.sleep(2.5)
    print("You, a young and courageous adventurer named Arin,")
    time.sleep(2.5)
    print("have decided to seek out this amulet to help your village, which has been suffering from a mysterious plague.\n")
    time.sleep(3)
    print("As the sun rises, you stand at the edge of the forest, ready to begin your quest. The air is filled with the songs of")
    time.sleep(2.5)
    print("birds and the rustling of leaves. You take a deep breath and step into the unknown.\n")
    time.sleep(3)
    print("After walking for a while, you come across a fork in the path.\n")
    time.sleep(3)
    print("To the left, the path seems darker and more ominous, with twisted trees and shadows lurking. To the right, the path is")
    time.sleep(2.5)
    print("brighter, with sunlight filtering through the leaves and the sound of a flowing river in the distance.\n")
    time.sleep(3)
    print("What do you choose?\n")
    time.sleep(2.5)
    print("1. Take the left path.\n")
    time.sleep(2.5)
    print("2. Take the right path.\n")
    time.sleep(2.5)

    while True:
        choice = input("Enter the number of your choice: ").strip()
        if choice == "1":
            update_score(random.randint(-5, 10))
            left_path()
            break  # Exit the loop after valid choice
        elif choice == "2":
            update_score(random.randint(-5, 10))
            right_path()
            break  # Exit the loop after valid choice
        else:
            print("Invalid choice. Please choose 1 or 2.\n")


def left_path():
    time.sleep(3)
    print("\nYou decide to take the left path, feeling a mix of excitement and trepidation.")
    time.sleep(2.5)
    print("The trees seem to close in around you as you venture deeper into the forest,")
    time.sleep(2.5)
    print("their gnarled branches creating eerie shapes in the dim light.")
    time.sleep(2.5)
    print("The air grows cooler, and the sounds of the forest fade away, replaced by an unsettling silence.\n")
    time.sleep(3)
    print("As you continue, you notice faint, glowing symbols etched into the bark of the trees.")
    time.sleep(2.5)
    print("You recall stories of ancient runes used by the forest's original inhabitants to protect their secrets.")
    time.sleep(2.5)
    print("You follow the symbols, hoping they might lead you to the amulet.\n")
    time.sleep(3)
    print("Suddenly, you hear a rustling in the underbrush. You pause, your hand instinctively reaching for your sword.")
    time.sleep(2.5)
    print("A figure emerges from the shadows—a tall, cloaked stranger with piercing eyes that seem to see right through you.\n")
    time.sleep(3)

    stranger_outcomes = [
        '"Greetings, traveler," the stranger says in a deep voice. "I see you seek the Enchanted Amulet."\n',
        '"Beware, adventurer," the stranger whispers. "The amulet is cursed. Many have lost their minds seeking it."\n',
        '"Hello, brave soul," the stranger booms. "You have courage, but the path ahead is fraught with danger."\n'
    ]
    print(random.choice(stranger_outcomes))
    time.sleep(3)
    print("The stranger offers you a choice:\n")
    time.sleep(3)
    print("1. Accept the stranger's guidance through the forest.\n")
    time.sleep(3)
    print("2. Politely decline and continue on your own.\n")
    time.sleep(3)

    while True:
        choice = input("Enter the number of your choice: ").strip()
        if choice == "1":
            update_score(random.randint(-5, 10))
            follow_him()
            break  # Exit the loop after valid choice
        elif choice == "2":
            update_score(random.randint(-5, 10))
            go_alone()
            break  # Exit the loop after valid choice
        else:
            print("Invalid choice. Please choose 1 or 2.\n")


def follow_him():
    time.sleep(3)
    print("\nYou accept the stranger's offer of guidance through the forest.")
    time.sleep(2.5)
    print("The stranger nods solemnly and leads you deeper into the dark forest,")
    time.sleep(2.5)
    print("navigating through the dense undergrowth with ease.")
    time.sleep(3)
    print("\nAlong the way, the stranger shares tales of ancient guardians and hidden traps within Eldoria, and he says")
    time.sleep(2.5)
    print('"There are guardians in this place; they are talking trees which protect the ancient amulet."')
    time.sleep(3)
    print('\n"People say whoever finds it will cure the plague in the kingdom of Elaria and will gain great power."')
    time.sleep(2.5)
    print('"And with great power comes great responsibility."')
    time.sleep(3)
    print("\nSuddenly the ancient guardian appears and asks you,")
    time.sleep(3)

    guardian_questions = [
        '"What is needed for success to make in life."\n',
        '"What do you value most in your journey?"\n',
        '"What will you sacrifice to achieve your goal?"\n'
    ]
    print(random.choice(guardian_questions))
    time.sleep(3)

    guardian_choices = [
        ["1. Money.\n", "2. Family.\n", "3. Love.\n", "4. Health.\n"],
        ["1. Courage.\n", "2. Wisdom.\n", "3. Strength.\n", "4. Compassion.\n"],
        ["1. Time.\n", "2. Wealth.\n", "3. Relationships.\n", "4. Safety.\n"]
    ]
    for choice in random.choice(guardian_choices):
        print(choice)
        time.sleep(2)

    choice = input("Enter the number of your choice: ").strip()
    responses = {
        '1': ("Interesting choice. Let's see how it serves you.\n", 2),
        '2': ("A wise decision. It may guide you well.\n", 3),
        '3': ("A heartfelt answer. It shows your true character.\n", 4),
        '4': ("A practical choice. It may protect you.\n", 1)
    }

    if choice in responses:
        response, points = responses[choice]
        print(response)
        update_score(points)
    else:
        print("Invalid choice. Please enter a valid number.\n")

    while True:
        choice = input("Enter the number of your choice: ").strip()
        if choice in ('1', '2', '3', '4'):
            update_score(random.randint(-10, 1))
            print(response)
            time.sleep(3)
            print("But unfortunately that was the wrong answer")
            time.sleep(2.5)
            print("and for that I will wipe your memories")
            start_narr()
            break
        else:
            print("Invalid choice. Please choose 1 or 2 or 3 or 4\n")


def go_alone():
    time.sleep(3)
    print("\nYou politely decline the stranger's offer of guidance and decide to continue on your own")
    time.sleep(2.5)
    print("through the dark forest.")
    time.sleep(3)
    print("\nThe stranger nods solemnly and fades back into the shadows.\n")
    time.sleep(3)
    print("As you walk alone through the shadows, a tree starts to talk to you and says,")
    time.sleep(3)

    tree_outcomes = [
        '\n"You have woken me up from my sleep and for that you shall pay the price. I will wipe your memories."',
        '\n"You have disturbed the peace of the forest. For that, you shall be cursed."',
        '\n"You dare to walk alone? Beware, for I will haunt your steps."'
    ]
    print(random.choice(tree_outcomes))
    time.sleep(3)
    print("\nAnd then you feel weird and you fall")
    time.sleep(4)
    print("The End")

    play_again()


def right_path():
    time.sleep(3)
    print("\nYou decide to take the right path, drawn by the sunlight and the sound of the flowing river.")
    time.sleep(2.5)
    print("As you walk, the forest feels alive with the sounds of chirping birds and rustling leaves.")
    time.sleep(2.5)
    print("The atmosphere is serene, and you feel a sense of peace wash over you.\n")
    time.sleep(3)
    print("The path leads you to a beautiful clearing with a sparkling river running through it.")
    time.sleep(2.5)
    print("You kneel to drink some of the cool, refreshing water.")
    time.sleep(2.5)
    print("As you drink from it, you notice a tree talking to you, a guardian or something.")
    time.sleep(2.5)
    print('And it says "I AM THE GUARDIAN OF THIS FOREST. ANSWER MY QUESTION TRUTHFULLY TO PROVE YOUR WORTH."\n')
    time.sleep(3)
    print('"What motivates you to seek the amulet?"\n')
    time.sleep(3)
    print("1. To rule.\n")
    time.sleep(2.5)
    print("2. To help others.\n")
    time.sleep(2.5)
    print("3. To gain knowledge.\n")
    time.sleep(2.5)
    print("4. To seek revenge.\n")

    while True:
        choice = input("Enter the number of your choice: ").strip()
        if choice in ["1", "2", "3", "4"]:
            update_score(random.randint(-5, 10))
            print("Interesting, that shows a lot about yourself.")
            time.sleep(2.5)
            print("But your answer was wrong, and for that you shall die.")
            play_again()
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.\n")


def play_again():
    time.sleep(3)
    print("Do you want to play again?\n")
    time.sleep(3)
    choice_p = input("Enter yes or no: ").strip().lower()

    if choice_p == "yes":
        start_narr()
    elif choice_p == "no":
        print("\nOk, thank you for playing.")
        time.sleep(2.5)
        exit()
    else:
        print("Invalid choice. Please enter yes or no.")
        play_again()
