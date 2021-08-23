"""
We make a dictionary with number as places to put either X or 0. And in the beggining of the match, we will have an empty field with places to put our X or 0.
"""
theBoard = {"7": " ", "8": " ", "9": " ", 
            "4": " ", "5": " ", "6": " ",
            "1": " ", "2": " ", "3": " "}


# We make a function that will print the board of tic tac toe game, using our dictionary with empty places, exp. board["1"] => this means that in dictionary, (let's call it list), list 1 will be printed. And looking at dictionary, at "1" we have an empty space.
def printBoard(theBoard):
    print(theBoard["7"] + "|" + theBoard["8"] + "|" + theBoard["9"])
    print("-+-+-")
    print(theBoard["4"] + "|" + theBoard["5"] + "|" + theBoard["6"])
    print("-+-+-")
    print(theBoard["1"] + "|" + theBoard["2"] + "|" + theBoard["3"])


#Just something important
board_keys = []
for key in theBoard:
    board_keys.append(key)


# There we will print all the functionality of a game. 
def game():

    turn = "X"
    count = 0 

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn, " + turn + " .Move to witch place?")

        move = input()

        
        
        if theBoard[move] == " ":
            theBoard[move] = turn
            count += 1
        else: 
            print("That place is already filed.\nMove to wich place ?")
            continue
        
        if count >= 5:
            if theBoard["7"] == theBoard["8"] == theBoard["9"] != " ":
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" ***** " + turn + " won. ***** ")
                break
            elif theBoard["4"] == theBoard["5"] == theBoard["6"] != " ":
                printBoard(theBoard)
                print("\nGame Over\n")
                print(" ***** " + turn + " won. ***** ")
                break
            elif theBoard["1"] == theBoard["2"] == theBoard["3"] != " ":
                printBoard(theBoard)
                print("\nGame Over\n")
                print(" ***** " + turn + " won. ***** ")
                break
            elif theBoard["1"] == theBoard["4"] == theBoard["7"] != " ":
                printBoard(theBoard)
                print("\nGame Over\n")
                print(" ***** " + turn + " won. ***** ")
                break
            elif theBoard["2"] == theBoard["5"] == theBoard["8"] != " ":
                printBoard(theBoard)
                print("\nGame Over\n")
                print(" ***** " + turn + " won. ***** ")
                break
            elif theBoard["3"] == theBoard["6"] == theBoard["9"] != " ":
                printBoard(theBoard)
                print("\nGame Over\n")
                print(" ***** " + turn + " won. ***** ")
                break
            elif theBoard["1"] == theBoard["5"] == theBoard["9"] != " ":
                printBoard(theBoard)
                print("\nGame Over\n")
                print(" ***** " + turn + " won. ***** ")
                break
            elif theBoard["3"] == theBoard["5"] == theBoard["7"] != " ":
                printBoard(theBoard)
                print("\nGame Over\n")
                print(" ***** " + turn + " won. ***** ")
                break
        
        #This code will declare a tie
        if count == 9: 
            print("\nGame Over\n")
            print("It's a tie")
        
        #This code will change turn from X to 0 after each move
        if turn == "X":
            turn = "0"
        else: 
            turn = "X"
    #This code will restart the game if players want to play it again        
    restart = input("Do you want to restart the game, to play again?(y/n): ")
    if restart == 'y' or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "
            
        game()

if __name__ == '__main__':
    game()


            