from module import *
import time

print("""Let's play Battleship!
You will play the game against computer...
Here is your board, you have 2 ships, one of them 3 dots and the other 2 dots...
Firstly, place your ship on your board...""")

user_board()
user_place_ship(board1,ships)
print("Your board after placing ships")
user_board()
comp_place_ship(board2,ships)
print("Please wait while computer is placing its ships...")
time.sleep(5)
print("Computer have placed its ships, now you can start the game!")

while (1):
    # user move
    board2 = user_move(board2)
    # check if user won
    if board2 == "WIN":
        print ("User WON!")
        quit()

    # display current computer board
    #comp_board()
    input("To end user turn hit ENTER")

    # computer move
    board1 = computer_move(board1)
    # check if computer won
    if board1 == "WIN":
        print ("Computer WON!")
        quit()

    # display user board
    #user_board()
    input("To end computer turn hit ENTER")
