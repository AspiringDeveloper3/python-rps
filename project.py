import random
import time

def main():
    mode = get_mode()

    if(mode == 1):
        user_choice = get_input()
        comp_choice = get_computer_choice()
        print(f"\nYou chose {user_choice}\nComputer chose {comp_choice}\n")
        print(f"Hence, {compare_choices(user_choice,comp_choice)}")
    elif(mode == 2):
        mode_internal(3)
    else:
        mode_internal(5)

def mode_internal(number):
    user_score = 0
    comp_score = 0
    for i in range(number):
        user_choice = get_input()
        comp_choice = get_computer_choice()
        result = compare_choices(user_choice,comp_choice)
        if result == "you win":
            user_score +=1
        elif result == "computer wins":
            comp_score += 1
        print(f"\nYou chose {user_choice}\nComputer chose {comp_choice}\n")
        print(f"Hence, {result}")
        time.sleep(3)
        print(f"\nYour score: {user_score}\nComputer's score: {comp_score}\n")
        time.sleep(3)
    print("FINAL RESULT: ")
    if user_score > comp_score:
        print("You win. Congratulations!\n")
    elif user_score < comp_score:
        print("You lose. Better luck next time!\n")
    else:
        print("It's a draw. How about a re-match?\n")

def get_mode():
    while True:
        try:
            mode = int(input("Choose one game mode out of the following: \nEnter [1] for Sudden Death\nEnter [2] for Best of 3\nEnter [3] for Best of 5\n>>> "))
            if mode not in [1,2,3]:
                print("\nThat is not a valid input. Please enter either '1', '2' or '3'\n")
                time.sleep(3)
            else:
                return mode
        except:
            print("\nThat is not a valid input. Please enter either '1', '2' or '3'\n")
            time.sleep(3)

def get_input():
    while True:
        try:
            choice = int(input("\nMake your choice: \nEnter [1] for Rock\nEnter [2] for Paper\nEnter [3] for Scissors\n>>> "))
            if(choice not in [1,2,3]):
                    print("\nThat is not a valid input. Please enter either '1', '2' or '3'\n")
                    time.sleep(3)
                    pass
            else:
                if choice == 1:
                    return "rock"
                if choice == 2:
                    return "paper"
                else:
                    return "scissors"
        except:
            print("\nThat is not a valid input. Please enter either '1', '2' or '3'\n")
            time.sleep(3)


def get_computer_choice():
    choice_list = ["rock","paper","scissors"]
    return random.choice(choice_list)

def compare_choices(user,computer):
    if user == computer:
        return "it's a draw"
    match user:
        case "rock":
            if(computer == "paper"):
                return "computer wins"
            else:
                return "you win"
        case "scissors":
            if(computer == "paper"):
                return "you win"
            else:
                return "computer wins"
        case "paper":
            if(computer == "rock"):
                return "you win"
            else:
                return "computer wins"



if __name__ == "__main__":
    main()