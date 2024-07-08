import random

my_board = [" ", " ", " ",
            " ", " ", " ",
            " ", " ", " "]


# Print the Board
def print_board(board):
    print()
    print("-" * 13)
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-" * 13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-" * 13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-" * 13)


# Check for Tie
def check_tie(board):
    if " " not in board:
        return True


# Check for Winner
def check_winner(board, my_player):
    if board[0] == my_player and board[1] == my_player and board[2] == my_player:
        return True
    elif board[3] == my_player and board[4] == my_player and board[5] == my_player:
        return True
    elif board[6] == my_player and board[7] == my_player and board[8] == my_player:
        return True
    elif board[0] == my_player and board[3] == my_player and board[6] == my_player:
        return True
    elif board[1] == my_player and board[4] == my_player and board[7] == my_player:
        return True
    elif board[2] == my_player and board[5] == my_player and board[8] == my_player:
        return True
    elif board[0] == my_player and board[4] == my_player and board[8] == my_player:
        return True
    elif board[2] == my_player and board[4] == my_player and board[6] == my_player:
        return True


# Switch Player
def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


# Reset the Board
def reset_board(board):
    for i in range(len(board)):
        if board[i] == "X" or board[i] == "O":
            board[i] = " "


# Ask the Player to Play Again
def play_again():
    global game_is_running
    valid_input = False
    while not valid_input:
        user_choice = input("Do you want to play again? (Y/N): ")
        if user_choice == "y" or user_choice == "Y":
            valid_input = True
            reset_board(my_board)
        elif user_choice == "n" or user_choice == "N":
            valid_input = True
            game_is_running = False
            print("\nGoodbye!")
        else:
            print("\nPlease enter a valid character!\n")


game_is_running = True
print("\nTIC TAC TOE GAME!")
player = ["X", "O"]
player = player[random.randint(0, 1)]
while game_is_running:
    print_board(my_board)
    idx = int(input(f"\n{player}'s turn: Enter any number from 0 - 8: "))
    if 0 <= idx <= 8:
        if my_board[idx] == "X" or my_board[idx] == "O":
            print("\nCell already occupied. Please select a different number!")
        else:
            my_board[idx] = player
            if check_winner(my_board, player):
                print_board(my_board)
                print(f"\nGame Over! {player} Wins!\n")
                play_again()
            elif check_tie(my_board):
                print_board(my_board)
                print("\nGame Over! It is tied!\n")
                play_again()
            switch_player()
    else:
        print("\nPlease enter a valid number!")
