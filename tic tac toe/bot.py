import random
from game_logic import check_win

def get_bot_move(board):
    ''' bot follows three steps to decide its move:
        1. check if it can win in the current move. if yes, make the winning move.
        2. check if the player can win in the next move. if yes, block them.
        3. if no immediate win or block is needed, pick a random available cell.
    '''
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                if check_win(board, 'O'):
                    return (i, j)
                board[i][j] = ' '  

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                if check_win(board, 'X'):
                    return (i, j)
                board[i][j] = ' '  

    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)
