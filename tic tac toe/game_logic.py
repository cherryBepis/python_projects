
def check_win(board, player):
    """Проверка на победу игрока."""
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Горизонталь
            return True
        if all([board[j][i] == player for j in range(3)]):  # Вертикаль
            return True
    if all([board[i][i] == player for i in range(3)]):  # Главная диагональ
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Побочная диагональ
        return True
    return False

def check_draw(board):
    """Проверка на ничью."""
    return all(cell != ' ' for row in board for cell in row)
