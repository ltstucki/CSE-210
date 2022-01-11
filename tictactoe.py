def main():
    print("Lets play Tic-Tac-Toe")
    print("Here is your board, choose a number on the board to place an X or an O")

    #The board will be created with a A1-C3 type battleship type of style.
    
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
    endGame = True

    while endGame == True:

        #Print the gameboard out to the player
        print(f"{a1} | {a2} | {a3}\n{b1} | {b2} | {b3}\n{c1} | {c2} | {c3}")

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

main()