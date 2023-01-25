#check for vertical win
def check_win(board):
    if (board[0] == board[3] == board[6] and board[0] != " ") or (board[1] == board[4] == board[7] and board[1] != " ") or (board[2] == board[5] == board[8] and board[2] != " "):
        return True

# check for diagonal win
    elif (board[0] == board[4] == board[8] and board[0] != " ") or (board[2] == board[4] == board[6] and board[2] != " "): 
        return True

    else:
        return False

board = [" "]*9

print(check_win(board))


