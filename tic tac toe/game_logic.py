def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # horizontal
            return True
        if all([board[j][i] == player for j in range(3)]):  # vertical
            return True
    if all([board[i][i] == player for i in range(3)]):  # main diag
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # 2nd diag
        return True
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)
