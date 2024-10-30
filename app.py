import random

choices = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0
games_played = 0  # Counter for the number of games played

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

while True:
    # Ask user for their choice
    user_choice = input("Please choose rock, paper, or scissor: ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please choose rock, paper, or scissor: ").lower()
    print(f"You selected: {user_choice}")

    # randomly select a choice for the computer
    selected_choice = random.choice(choices)
    print(f"The computer selected: {selected_choice}")

    # Determine the winner
    winner = get_winner(user_choice, selected_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    # Increment the games played counter
    games_played += 1

    # Print the scores
    print(f"Score - You: {user_score}, Computer: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again not in ["y", "yes"]:
        print("Thanks for playing!")
        break

# Print the final scores and the number of games played
print(f"Final Score - You: {user_score}, Computer: {computer_score}")
print(f"Total games played: {games_played}")