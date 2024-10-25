import random

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0
    draw = 0
    # predefined list
    options = ["rock", "paper", "scissors"]

    # welcome message
    print("Welcome to Rock, Paper, Scissors!")

    # while loop to keep the game running
    while True:
        # User input
        user_choice = input("Please choose rock, paper, or scissors: ").lower()
        # Computer choice
        computer_choice = random.choice(options)
        if user_choice in options:
            print(f"Computer chose {computer_choice}")
            # Check who won
            if user_choice == computer_choice:
                print("It's a tie!")
                draw += 1
            elif user_choice == "rock" and computer_choice == "scissors":
                print("You win!")
                user_score += 1
            elif user_choice == "paper" and computer_choice == "rock":
                print("You win!")
                user_score += 1
            elif user_choice == "scissors" and computer_choice == "paper":
                print("You win!")
                user_score += 1
            else:
                print("Computer wins!")
                computer_score += 1
        # displays score
        print(f"User: {user_score} Computer: {computer_score} Draw: {draw}")
        # Ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thank you for playing!")


# Run the game
rock_paper_scissors_game()
