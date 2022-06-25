#Tic Tac Toe Game
#Author: Dewar P.

def play_match(player_name):
    """This function is responsible for running a tic tac toe
    match. The human user plays a series of tic tac toe games
    with the computer. The match is won when one of the players
    has won two games."""
    
    num_human_wins = 0
    num_computer_wins = 0
    #A loop for the match; loop ends when one of them
    #has two wins.
    while num_human_wins < 2 and num_computer_wins < 2:
        winner = play_one_game(player_name)
        if winner == player_name:
            num_human_wins += 1
        elif winner == "computer":
            num_computer_wins += 1
        
    if num_human_wins > num_computer_wins:
        return "The match was won by " + player_name
    else:
        return "The match was won by the computer"

def play_one_game(player_name):
    """This function is responsible for playing one tic-tac-toe
    game, and reporting (return) the winner.
    It should:
        1) Initialize (clear out) the board
        2) Give the human and the computer repeated turns
            at playing on the board.
        3) Decide if the game is over.
        4) Return the winner player (or "tie") """
    
    board = initialize_board()
    while not game_over(board):
        human_plays(board)
        
        if not game_over(board):
            computer_plays(board)
            
    #Loop ends --> game is over
    if game_winner(board) == "X":
        return player_name
    elif game_winner(board) == "O":
        return "computer"
    else:
        return "tie"
    
def initialize_board():
    board = [  [" ", " ", " "],   [" ", " ", " "],   [" ", " ", " "]   ]    
    return board

def game_over(board):
    
    #Think about how to check for a row win
    for row in range(3):        
        if board[row][0] == "X" and board[row][1] =="X" and board[row][2] == "X":
            return True
        if board[row][0] == "O" and board[row][1] == "O" and board[row][2] == "O":
            return True
        
    #Think about how to check for a column win
    for col in range(3):
        if board[0][col] == "X" and board[1][col] == "X" and board[2][col] == "X":
            return True
        if board[0][col] == "O" and board[1][col] == "O" and board[2][col] == "O":
            return True

    #Check for a win on diagonal 1
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X": #has a small problem (fixed)
        return True
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O": #has a small problem (fixed)
        return True
    
    #Check for a win on diagonal 2
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return True
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return True
            
    #Check to see if all entries are full
    used = 0
    for x in range(3):
        for w in range(3):
            if board[x][w] == "X":
                used = used+1
            if board[x][w] == "O":
                used = used+1
                
    if used == 9:
        return True 
        
        #Otherwise, return False
    else:
        return False

def human_plays(board):
    """Find out where the human wants to place her/his "X" and make the
    corresponding entry in the board. """
    
    row = int(input("In which row do you want to play? [0-2]: "))
    col = int(input("In which col do you want to play? [0-2]: "))
    
    #Ensure that row & col are legitimate. Probably use a loop.
    while board[row][col] == ("X" or "O"):
        print("")
        print("This position has already been used")
        print("")
        print("Try a different position")
        print("")
        row = int(input("In which row do you want to play? [0-2]: "))
        col = int(input("In which col do you want to play? [0-2]: "))
    
    board[row][col] = "X"  #The "X" is now played in that location
    show = print_board(board)
    return

def computer_plays(board):
    """Determine where the computer plays. In that location, place "O". """

    #Scan through the rows and columns to find the first open spot in
    #board, and then play there

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                show = print_board(board)
                return  
           
    #Need to make the computer much smarter.
    
def game_winner(board):
    """Who won the game? Return "X", "O" or "tie". """
    #This is very similar to game_over. Except, don't return True/False.
    
    for row in range(3):        
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return board[0][col]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return "tie"
        
def print_board(board):
    print("")
    print("*" * 13)
    for row in range(3):
        for column in range(3):
            print("*", board[row][column],end=" ")
        print("*")
        print("*" * 13)
        
if __name__=="__main__":
    print(play_match("Peter"))