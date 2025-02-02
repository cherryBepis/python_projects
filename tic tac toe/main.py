import pygame
import sys
from game_logic import check_win, check_draw
from bot import get_bot_move

pygame.init()

# window and display settings
WIDTH, HEIGHT = 900, 900
LINE_WIDTH = 5
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)

GRID_SIZE = 3
CELL_SIZE = 150 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-tac-toe')

# images load
X_IMAGE = pygame.transform.scale(pygame.image.load('assets/x.png'), (CELL_SIZE-100, CELL_SIZE-100))
O_IMAGE = pygame.transform.scale(pygame.image.load('assets/o.png'), (CELL_SIZE-100, CELL_SIZE-100))


# game settings
player = 'X'
bot = 'O'
current_player = player
game_over = False

# Функции для рисования
def draw_lines():
    """Draw grid"""
#lines
    pygame.draw.line(screen, LINE_COLOR, (225, 375), (675, 375), LINE_WIDTH)  
    pygame.draw.line(screen, LINE_COLOR, (225, 525), (675, 525), LINE_WIDTH)  
    pygame.draw.line(screen, LINE_COLOR, (375, 225), (375, 675), LINE_WIDTH)  
    pygame.draw.line(screen, LINE_COLOR, (525, 225), (525, 675), LINE_WIDTH)  

#borders
    pygame.draw.line(screen, LINE_COLOR, (225, 225), (675, 225), LINE_WIDTH)  
    pygame.draw.line(screen, LINE_COLOR, (225, 675), (675, 675), LINE_WIDTH)  
    pygame.draw.line(screen, LINE_COLOR, (225, 225), (225, 675), LINE_WIDTH)  
    pygame.draw.line(screen, LINE_COLOR, (675, 225), (675, 675), LINE_WIDTH)  





def draw_marks(board):
    """Draw X and O in the correct grid cells"""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                x = 225 + col * CELL_SIZE + (CELL_SIZE - X_IMAGE.get_width()) // 2
                y = 225 + row * CELL_SIZE + (CELL_SIZE - X_IMAGE.get_height()) // 2
                screen.blit(X_IMAGE, (x, y))
            elif board[row][col] == 'O':
                x = 225 + col * CELL_SIZE + (CELL_SIZE - O_IMAGE.get_width()) // 2
                y = 225 + row * CELL_SIZE + (CELL_SIZE - O_IMAGE.get_height()) // 2
                screen.blit(O_IMAGE, (x, y))


def draw_game_over():
    """Рисуем экран с надписью о завершении игры и кнопкой для перезапуска."""
    font = pygame.font.Font(None, 40)
    text = font.render("Игра закончена!", True, (0, 0, 0))
    screen.blit(text, (WIDTH // 3, HEIGHT // 3 - 40))
    
    # Кнопка перезапуска
    restart_button = pygame.Rect(WIDTH // 3, HEIGHT // 3 + 40, WIDTH // 3, 50)
    pygame.draw.rect(screen, (28, 170, 156), restart_button)
    restart_text = font.render("Играть заново", True, (255, 255, 255))
    screen.blit(restart_text, (WIDTH // 3 + 40, HEIGHT // 3 + 50))
    return restart_button

def main():
    global current_player, game_over
    board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Инициализация поля
    
    running = True
    
    
    while running:
        
        screen.fill(BG_COLOR)
        draw_lines()
        draw_marks(board)

        if game_over:
            # Эффект размытия фона
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(150)  # Прозрачность
            overlay.fill((255, 255, 255))  # Белый цвет
            screen.blit(overlay, (0, 0))

            # Рисуем экран завершения
            restart_button = draw_game_over()
            
            # Слушаем события, чтобы перезапустить игру
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        # Сброс игры
                        board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
                        game_over = False
                        current_player = player

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and current_player == player:
                    mouseX, mouseY = event.pos
                    if 225 <= mouseX < 675 and 225 <= mouseY < 675:  # Проверка, что клик в пределах сетки
                        clicked_row = (mouseY - 225) // CELL_SIZE
                        clicked_col = (mouseX - 225) // CELL_SIZE

                    

                    if board[clicked_row][clicked_col] == ' ':
                        board[clicked_row][clicked_col] = player
                        if check_win(board, player):
                            print("Игрок победил!")
                            game_over = True
                        elif check_draw(board):
                            print("Ничья!")
                            game_over = True
                        current_player = bot

            if current_player == bot and not game_over:
                print("Ход бота...")
                row, col = get_bot_move(board)
                board[row][col] = bot
                if check_win(board, bot):
                    print("Бот победил!")
                    game_over = True
                elif check_draw(board):
                    print("Ничья!")
                    game_over = True
                current_player = player

        pygame.display.update()

if __name__ == "__main__":
    main()
