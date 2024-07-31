import random

def play_round():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return None, None
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
    else:
        result = "You lose!"
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)
    return result

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        result = play_round()
        if result:
            if "win" in result:
                user_score += 1
            elif "lose" in result:
                computer_score += 1
            print(f"Score: You {user_score} - Computer {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")


play_game()
