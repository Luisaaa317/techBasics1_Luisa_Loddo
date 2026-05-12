import time
print("Welcome to this mini-game!")
time.sleep(1.5)
print("Please pick a username!")
name = input("Please enter your username!")
time.sleep(1)
print("Welcome", name)
time.sleep(1)

print("Please enter your age!")
age = input("Enter your age:")
if age.isnumeric():
    age = int(age)
if age > 110 or age < 0:
    print("Your age is not possible for a human! Please re-enter your age.")
elif age < 4:
    print("You're too young to play this game!")
else:
    print("Your age has been verified. Have fun playing!")
    time.sleep(1)
    print("Let me explain how this game works!")
    time.sleep(1)
    print("This game is a quiz.")
    time.sleep(1)
    print("You can choose a category in which you're being quizzed!")
    time.sleep(2)
    print("The categories are: math, countries or animals.")
    time.sleep(2)
    print("Please pick a category!")
    category = input("Please enter your pick!")
    if category == "math":
        print("You chose math.")
        time.sleep(1)
        print("Lets start!")
        time.sleep(2)
        points = 0
        print("What does 22-3*4 equal?")
        time.sleep(1.5)
        answer = input("22-3*4=")
        if answer == "10":
            print("Correct! You gained a point!")
            points = points + 1
        else:
            print("Incorrect! The correct answer was 10.")
            time.sleep(1)
            print("Next question!")
        time.sleep(1)
        print("What does 23-60+83 equal?")
        time.sleep(1.5)
        answer = input("23-60+83=")
        if answer == "46":
            print("Correct! You gained a point!")
            points = points + 1
        else:
            print("Incorrect! The correct answer was 46.")
            time.sleep(1)
            print("Get ready for the last question!")
        time.sleep(1)
        print("What does 6*6+6 equal?")
        time.sleep(1.5)
        answer = input("6*6+6=")
        if answer == "42":
            print("Correct! You gained a point!")
            points = points + 1
            time.sleep(1)
            print("This game is over :) You achieved", points, "out of 3 points.")
        else:
            print("Incorrect! The answer was 42.")
            time.sleep(1)
            print("This game is over :( You achieved", points, "out of 3 points.")
    elif category == "countries":
        print("You chose countries!")
        time.sleep(1)
        print("Lets start!")
        time.sleep(2)
        points = 0
        print("What's the capital city of Australia?")
        time.sleep(1.5)
        answer = input("What's the capital city of Australia?")
        if answer == "Canberra":
            print("Correct! You gained a point!")
            points = points + 1
        else:
            print("Incorrect! Canberra is the capital of Australia.")
            time.sleep(1)
            print("Next question!")
        time.sleep(1)
        print("How many states does the US consist of?")
        time.sleep(1.5)
        answer = input("How many states does the US consist of?")
        if answer == "50":
            print("Correct! You gained a point!")
            points = points + 1
        else:
            print("Incorrect! The answer was 50 states.")
            time.sleep(1)
            print("Last question!")
        time.sleep(1)
        print("What is the biggest country on Earth?")
        time.sleep(1.5)
        answer = input("What is the biggest country on Earth?")
        if answer == "Russia":
            print("Correct! You gained a point!")
            points = points + 1
            time.sleep(1)
            print("This game is over :) You achieved", points, "out of 3 points.")
        else:
            print("Incorrect! The answer was Russia.")
            time.sleep(1)
            print("This game is over :( You achieved", points, "out of 3 points.")
    elif category == "animals":
        print("You chose animals!")
        time.sleep(1)
        print("Lets start!")
        time.sleep(2)
        points = 0
        print("What's the worlds largest mammal?")
        time.sleep(1.5)
        answer = input("What's the worlds largest animal?")
        if answer == "blue whale":
            print("Correct! You gained a point!")
            points = points + 1
        else:
            print("Incorrect! The worlds largest animal is the (blue) whale.")
            time.sleep(1)
            print("Next question!")
        time.sleep(1)
        print("What's the worlds fastest mammal?")
        time.sleep(1.5)
        answer = input("What's the worlds fastest mammal?")
        if answer == "leopard":
            print("Correct! You gained a point!")
            points = points + 1
        else:
            print("Incorrect! The fastest mammal is the leopard.")
            time.sleep(1)
            print("Time for the last question!")
        time.sleep(1)
        print("What's the deadliest animal on Earth?")
        time.sleep(1.5)
        answer = input("What's the deadliest animal on Earth?")
        if answer == "mosquito":
            print("Correct! You gained a point!")
            points = points + 1
            time.sleep(1)
            print("This game is over :) You achieved", points, "out of 3 points.")
        else:
            print("Incorrect! The mosquito is the worlds deadliest animal.")
            time.sleep(1)
            print("This game is over :( You achieved", points, "out of 3 points.")
    else:
        print("The category you picked is not recognized.")
        time.sleep(1)
        print("Please restart.")

    


