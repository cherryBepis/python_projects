import random
from game_logic import check_win

def get_bot_move(board):
    """Логика хода бота."""
    # Проверяем, можем ли мы выиграть
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                if check_win(board, 'O'):
                    return (i, j)
                board[i][j] = ' '  # Отменяем ход

    # Проверяем, нужно ли блокировать игрока
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                if check_win(board, 'X'):
                    return (i, j)
                board[i][j] = ' '  # Отменяем ход

    # Если нет выигрыша или блокировки, выбираем случайную клетку
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)
