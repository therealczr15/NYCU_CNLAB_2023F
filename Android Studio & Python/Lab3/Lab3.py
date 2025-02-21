import tkinter as tk

# create board
def  create_board(window):
    # create a 3x3 board
    for i in range(3):
            for j in range(3):
                button = tk.Button(window, text="", font=("Arial", 50),
                                   height = 2, width = 6, bg = 'gray',
                                   command = lambda row = i, col = j: handle_click(row, col))
                button.grid(row = i, column = j, sticky = "nsew")
         
# handle button clicks
def handle_click(row, col):
        global current_player
        global board
        
        # check which button has been clicked and change player
        if board[row][col] == 0:
            
            # 1 means 'O' & 2 means 'X'
            if current_player == 1:
                board[row][col] = 1
                current_player = 2
            else:
                board[row][col] = 2
                current_player = 1
                
            # change text on button to show 'O' or 'X'
            button = window.grid_slaves(row = row, column = col)[0]
            if board[row][col] == 1:
                button.config(text = 'O', bg = 'gray')
            else:
                button.config(text = 'X', bg = 'gray')
            check_winner()

# check for a winner or a tie
def check_winner():    
    winner = None
    winner_path = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    # check rows
    for i in range(3):
        # if there is a row connected as a line, store the information of this row in the winner_path
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != 0 :
            winner = board[i][0]
            winner_path[i][0] = 1
            winner_path[i][1] = 1
            winner_path[i][2] = 1
    
    # check columns
    for i in range(3):
        # if there is a column connected as a line, store the information of this column in the winner_path
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != 0 :
            winner = board[0][i]
            winner_path[0][i] = 1
            winner_path[1][i] = 1
            winner_path[2][i] = 1
    
    # check diagnoals
    # if there is a diagnoal connected as a line, store the information of this diagnoal in the winner_path
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != 0 :
        winner = board[0][0]
        winner_path[0][0] = 1
        winner_path[1][1] = 1
        winner_path[2][2] = 1
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != 0 :
        winner = board[0][2]
        winner_path[0][2] = 1
        winner_path[1][1] = 1
        winner_path[2][0] = 1
        
    # check if tie
    # if every board is filled with values but no lines are connected, it results in a tie
    if winner == None and not(0 in board[0]) and not(0 in board[1]) and not (0 in board[2]):
        winner = "tie"
    
    # if there is a winner or a tie
    if winner:
        declare_winner(winner, winner_path)
        
# declare the winner and ask to restart the game
def declare_winner(winner, winner_path):
    if winner == "tie":
        
        # output message
        message = "It's a tie! Do you want to restart the game?"
        
        # refresh board color
        for i in range(3):
                for j in range(3):
                    button = window.grid_slaves(row = i, column = j)[0]
                    button.config(bg = 'red')
    else:
        
        # output message
        if winner == 1:
            message = "Player O wins! Do you want to restart the game?"
        elif winner == 2:
            message = "Player X wins! Do you want to restart the game?"

        # refresh board color
        for i in range(3):
                for j in range(3):
                    if winner_path[i][j] == 1 :
                        button = window.grid_slaves(row = i, column = j)[0]
                        button.config(bg = 'blue')
           
    # ask if the player wants to continuing
    answer = tk.messagebox.askyesno(title = "Game Over", message = message)
    
    if answer:
        
        # player another round
        global board
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        # reset the board
        for i in range(3):
            for j in range(3):
                button = window.grid_slaves(row = i, column = j)[0]
                button.config(text = "", bg = 'gray')
        
        # reset player
        global current_player
        current_player = 1
        
    else:
        
        # destroy window
        window.destroy()
        
        
if __name__ == '__main__':
    
    # create main window
    window = tk.Tk()
    window.title("Lab3 Tic-Tac-Toe")
    
    # create game board
    create_board(window)
    
    # initial variables
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = 1
    
    window.mainloop()