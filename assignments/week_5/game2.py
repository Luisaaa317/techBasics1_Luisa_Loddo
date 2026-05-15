
import time
 # defining my variable for points and my constants for pauses
points = 0
PAUSE_S = 1
PAUSE_M = 1.5
PAUSE_L = 2

#defining a function that covers the standard procedure of starting this/any game
def start_game(user_name):
    print("Welcome to this mini-game!")
    time.sleep(PAUSE_M)
    print("Please pick a username!")
    time.sleep(PAUSE_S)
    user_name = input("Please enter your username!")
    time.sleep(PAUSE_S)
    print("Welcome", user_name)
    time.sleep(PAUSE_S)
    return user_name

#function for explaining how the game works
def game_explanation():
    print("Let me explain how this game works!")
    time.sleep(PAUSE_S)
    print("This game is a quiz.")
    time.sleep(PAUSE_S)
    print("You can choose a category in which you're being quizzed!")
    time.sleep(PAUSE_L)
    print("The categories are: math, countries or animals.")

#function that checks if the users answer is correct
def check_user_answer(user_answer, correct_answer):
    global points
    if user_answer == correct_answer:
        print("Correct! You gained a point!")
        points = points + 1
        return points
    else:
        print(f"Incorrect! The answer was {correct_answer}.")
        time.sleep(PAUSE_S)
        return points

#defining main function
def main():
    initiation = input("Please enter 'start'.")
    start_game(name)

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
        time.sleep(PAUSE_S)
        game_explanation()
        time.sleep(PAUSE_L)
        print("Please pick a category!")
        category = input("Please enter your pick!")
        if category == "math":
            print("You chose math.")
            time.sleep(PAUSE_S)
            print("Lets start!")
            time.sleep(PAUSE_L)
            print("What does 22-3*4 equal?")
            time.sleep(PAUSE_M)
            answer = input("22-3*4=")
            points = check_user_answer(answer, "10")
            print("Next question!")
            time.sleep(PAUSE_S)
            print("What does 23-60+83 equal?")
            time.sleep(PAUSE_M)
            answer = input("23-60+83=")
            points = check_user_answer(answer, "46")
            print("Last question!")
            time.sleep(PAUSE_S)
            print("What does 6*6+6 equal?")
            time.sleep(PAUSE_M)
            answer = input("6*6+6=")
            points = check_user_answer(answer, "42")
            print("This game is over! You achieved", points, "out of 3 points.")
        elif category == "countries":
            print("You chose countries!")
            time.sleep(PAUSE_S)
            print("Lets start!")
            time.sleep(PAUSE_L)
            print("What's the capital city of Australia?")
            time.sleep(PAUSE_M)
            answer = input("What's the capital city of Australia?")
            points = check_user_answer(answer, "Canberra")
            print("Next question!")
            time.sleep(PAUSE_S)
            print("How many states does the US consist of?")
            time.sleep(PAUSE_M)
            answer = input("How many states does the US consist of?")
            points = check_user_answer(answer, "50")
            print("Last question!")
            time.sleep(PAUSE_S)
            print("What is the biggest country on Earth?")
            time.sleep(PAUSE_M)
            answer = input("What is the biggest country on Earth?")
            points = check_user_answer(answer, "Russia")
            print("This game is over! You achieved", points, "out of 3 points.")
        elif category == "animals":
            print("You chose animals!")
            time.sleep(PAUSE_S)
            print("Lets start!")
            time.sleep(PAUSE_L)
            print("What's the worlds largest mammal?")
            time.sleep(PAUSE_M)
            answer = input("What's the worlds largest animal?")
            points = check_user_answer(answer, "blue whale")
            print("Next question!")
            time.sleep(PAUSE_S)
            print("What's the worlds fastest mammal?")
            time.sleep(PAUSE_M)
            answer = input("What's the worlds fastest mammal?")
            points = check_user_answer(answer, "leopard")
            print("Last question!")
            time.sleep(PAUSE_S)
            print("What's the deadliest animal on Earth?")
            time.sleep(PAUSE_M)
            answer = input("What's the deadliest animal on Earth?")
            points = check_user_answer(answer, "mosquito")
            print("This game is over! You achieved", points, "out of 3 points.")
        else:
            print("The category you picked is not recognized.")
            time.sleep(PAUSE_S)
            print("Please restart.")

#executing main function
if __name__ == "__main__":
    main()
