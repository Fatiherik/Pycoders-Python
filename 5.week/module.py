import random

hit1=0
hit2=0

board1 = []
for x in range(0, 5):
    board1.append(["o"] * 5)

board2 = []
for x in range(0, 5):
    board2.append(["o"] * 5)

ships = {"Submarine": 3,
         "Patrol Boat": 2}

def user_board():
    for row in board1:
        print(" ".join(row))

def comp_board():
    for row in board2:
        print(" ".join(row))

def user_place_ship(board1,ships):
    for ship in ships.keys():
        valid = False
        while (not valid):
            x, y = get_coor()
            ori = v_or_h()
            valid = validate(board1, ships[ship], x, y, ori)
            if not valid:
                print("Cannot place a ship there.\nPlease take a look at the board and try again.")
                input("Hit ENTER to continue")

        board1=place_ship(board1,ships[ship],ship[0],ori,x,y)
    return board1

def comp_place_ship(board2,ships):
    for ship in ships.keys():
        valid = False
        while (not valid):
            x = random.randint(1, 5) - 1
            y = random.randint(1, 5) - 1
            o = random.randint(0, 1)
            if o == 0:
                ori = "v"
            else:
                ori = "h"
            valid = validate(board2, ships[ship], x, y, ori)
        board2 = place_ship(board2, ships[ship],ship[0],ori,x,y)
    return board2

def place_ship(board,ship,s,ori,x,y):
	#place ship based on orientation
	if ori == "v":
		for i in range(ship):
			board[x+i][y] = s
	elif ori == "h":
		for i in range(ship):
			board[x][y+i] = s
	return board

def validate(board, ship, x, y, ori):
    # validate the ship can be placed at given coordinates
    if ori == "v" and x + ship > 5:
        return False
    elif ori == "h" and y + ship > 5:
        return False
    else:
        if ori == "v":
            for i in range(ship):
                if board[x + i][y] != "o":
                    return False
        elif ori == "h":
            for i in range(ship):
                if board[x][y + i] != "o":
                    return False
    return True

def v_or_h():
    # get ship orientation from user
    while (True):
        user_input = input("vertical or horizontal (v,h) ? ")
        if user_input == "v" or user_input == "h":
            return user_input
        else:
            print ("Invalid input. Please only enter v or h")

def get_coor():
    while (True):
        user_input = input("Please enter coordinates (row,col) ? ")
        try:
            # see that user entered 2 values seprated by comma
            coor = user_input.split(",")
            if len(coor) != 2:
                raise Exception("Invalid entry, too few/many coordinates.")

            # check that 2 values are integers
            coor[0] = int(coor[0]) - 1
            coor[1] = int(coor[1]) - 1

            # check that values of integers are between 1 and 10 for both coordinates
            if coor[0] > 5 or coor[0] < 0 or coor[1] > 5 or coor[1] < 0:
                raise Exception("Invalid entry. Please use values between 1 to 5 only.")

            # if everything is ok, return coordinates
            return coor

        except ValueError:
            print ("Invalid entry. Please enter only numeric values for coordinates")
        except Exception as e:
            print (e)

def make_move(board, x, y):
    # make a move on the board and return the result, hit, miss or try again for repeat hit
    if board[x][y] == "o":
        return "miss"
    elif board[x][y] == '*' or board[x][y] == '$':
        return "try again"
    else:
        return "hit"


def user_move(board2):
    # get coordinates from the user and try to make move
    # if move is a hit, check ship sunk and win condition
    while (True):
        x, y = get_coor()
        res = make_move(board2, x, y)
        if res == "hit":
            print ("Hit at " + str(x + 1) + "," + str(y + 1))
            sink(board2, hit2, x, y)
            board2[x][y] = '$'
            if check_win(hit2):
                return "WIN"
        elif res == "miss":
            print("Sorry, " + str(x + 1) + "," + str(y + 1) + " is a miss.")
            board2[x][y] = "*"
        elif res == "try again":
            print ("Sorry, that coordinate was already hit. Please try again")

        if res != "try again":
            return board2


def computer_move(board1):
    # generate user coordinates from the user and try to make move
    # if move is a hit, check ship sunk and win condition
    while (True):
        x = random.randint(1, 5) - 1
        y = random.randint(1, 5) - 1
        res = make_move(board1, x, y)
        if res == "hit":
            print ("Hit at " + str(x + 1) + "," + str(y + 1))
            sink(board1, hit1, x, y)
            board1[x][y] = '$'
            if check_win(hit1):
                return "WIN"
        elif res == "miss":
            print ("Sorry, " + str(x + 1) + "," + str(y + 1) + " is a miss.")
            board1[x][y] = "*"

        if res != "try again":
            return board1


def sink(board, hit, x, y):
    # figure out what ship was hit
    if board[x][y] == "S":
        ship = "Submarine"
    elif board[x][y] == "P":
        ship = "Patrol Boat"
    hit += 1
    print(str(hit)+". hit")
    print (ship + " Sunk")

def check_win(hit):
    if hit!=2:
        return False
    return True
