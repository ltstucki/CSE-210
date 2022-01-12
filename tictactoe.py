#Landon Stucki
#CSE210 Tic Tac Toe Project
def main():
    print("Lets play Tic-Tac-Toe")
    print("Here is your board, choose a number on the board to place an X or an O")

    ticTacToe()

    #The board will be created with a A1-C3 type battleship type of style.
def ticTacToe():
    #the creation of players
    player1 = "x"
    player2 = "o"
    #Creation of the 1-9 spots on board [Note the variables are made [strings] for easy change to 'X' and 'O']
    #top row
    a1 = "1"
    a2 = "2"
    a3 = "3"
    #middle row
    b1 = "4"
    b2 = "5"
    b3 = "6"
    #top row
    c1 = "7"
    c2 = "8"
    c3 = "9"

    #Print the gameboard out to the player
    print(f"{a1} | {a2} | {a3}\n{b1} | {b2} | {b3}\n{c1} | {c2} | {c3}")
    endGame = True
    while endGame == True:


        player1 = input("X's turn too choose a square! (1-9): ")

        #Update/Change the boards move (X goes first)
        if player1 == a1:
            a1 = "X"
        elif player1 == a2:
            a2 = "X"
        elif player1 == a3:
            a3 = "X"
        elif player1 == b1:
            b1 = "X"
        elif player1 == b2:
            b2 = "X"
        elif player1 == b3:
            b3 = "X"
        elif player1 == c1:
            c1 = "X"
        elif player1 == c2:
            c2 = "X"
        elif player1 == c3:
            c3 = "X"
        
        print(f"{a1} | {a2} | {a3}\n{b1} | {b2} | {b3}\n{c1} | {c2} | {c3}")

                #Check if there is a winner for X's
        if a1 == "X" and a2 == "X" and a3 == "X":
            print("Game Over! Thanks for Playing!")
            break
        elif b1 == "X" and b2 == "X" and b3 == "X":
            print("Game Over! Thanks for Playing!")
            break
        elif c1 == "X" and c2 == "X" and c3 == "X":
            print("Game Over! Thanks for Playing!")
            break
        elif a1 == "X" and b2 == "X" and c3 == "X":
            print("Game Over! Thanks for Playing!")
            break
        elif a1 == "X" and b1 == "X" and c1 == "X":
            print("Game Over! Thanks for Playing!")
            break
        elif a2 == "X" and b2 == "X" and c2 == "X":
            print("Game Over! Thanks for Playing!")
            break
        elif a3 == "X" and b3 == "X" and c3 == "X":
            print("Game Over! Thanks for Playing!")
            break
        elif a3 == "X" and b2 == "X" and c1 == "X":
            print("Game Over! Thanks for Playing!")
            break
        
        #Check if there is no winner
        if a1 and a2 and a3 and b1 and b2 and b3 and c1 and c2 and c3 == ("X" or "O"):
            print("Game! Over! Draw! Thanks for Playing!")
            break
        #Update/Change the boards move (O's turn now)

        player2 = input("O's turn too choose a square! (1-9): ")
        if player2 == a1:
            a1 = "O"
        elif player2 == a2:
            a2 = "O"
        elif player2 == a3:
            a3 = "O"
        elif player2 == b1:
            b1 = "O"
        elif player2 == b2:
            b2 = "O"
        elif player2 == b3:
            b3 = "O"
        elif player2 == c1:
            c1 = "O"
        elif player2 == c2:
            c2 = "O"
        elif player2 == c3:
            c3 = "O"   

        #Print the gameboard out to the player
        print(f"{a1} | {a2} | {a3}\n{b1} | {b2} | {b3}\n{c1} | {c2} | {c3}")

        #Check if there is a winner for O's
        if a1 == "O" and a2 == "O" and a3 == "O":
            print("Game Over! Thanks for Playing!")
            break
        elif b1  == "O"and b2 == "O" and b3 == "O":
            print("Game Over! Thanks for Playing!")
            break
        elif c1 == "O" and c2 == "O" and c3 == "O":
            print("Game Over! Thanks for Playing!")
            break
        elif a1 == "O" and b2 == "O" and c3 == "O":
            print("Game Over! Thanks for Playing!")
            break
        elif a1 == "O" and b1 == "O" and c1 == "O":
            print("Game Over! Thanks for Playing!")
            break
        elif a2 == "O" and b2 == "O" and c2 == "O":
            print("Game Over! Thanks for Playing!")
            break
        elif a3 == "O" and b3 == "O" and c3 == "O":
            print("Game Over! Thanks for Playing!")
            break
        elif a3 == "O" and b2 == "O" and c1 == "O":
            print("Game Over! Thanks for Playing!")
            break

        
        #Check if there is no winner
        if a1 and a2 and a3 and b1 and b2 and b3 and c1 and c2 and c3 == ("X" or "O"):
            print("Game! Over! Draw! Thanks for Playing!")
            break
main()