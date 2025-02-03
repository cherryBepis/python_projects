import pygame
import sys
from game_logic import check_win, check_draw
from bot import get_bot_move
from PIL import Image, ImageFilter



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

restart_img = pygame.image.load("assets/restart.png")  # Загружаем картинку
restart_img_pil = Image.frombytes('RGBA', restart_img.get_size(), pygame.image.tostring(restart_img, 'RGBA'))
blurred_img_pil = restart_img_pil.filter(ImageFilter.GaussianBlur(radius=9))
blurred_img = pygame.image.fromstring(blurred_img_pil.tobytes(), blurred_img_pil.size, 'RGBA')

restart_img = blurred_img


# game settings
player = 'X'
bot = 'O'
current_player = player
game_over = False

# Счет
player_wins = 0
bot_wins = 0


def draw_lines():
    """Draw grid"""
    pygame.draw.line(screen, LINE_COLOR, (225, 375), (675, 375), LINE_WIDTH//2)  
    pygame.draw.line(screen, LINE_COLOR, (225, 525), (675, 525), LINE_WIDTH//2)  
    pygame.draw.line(screen, LINE_COLOR, (375, 225), (375, 675), LINE_WIDTH//2)  
    pygame.draw.line(screen, LINE_COLOR, (525, 225), (525, 675), LINE_WIDTH//2)  

    # Borders
    pygame.draw.line(screen, LINE_COLOR, (225, 225), (675, 225), LINE_WIDTH//2)  
    pygame.draw.line(screen, LINE_COLOR, (225, 675), (675, 675), LINE_WIDTH//2)  
    pygame.draw.line(screen, LINE_COLOR, (225, 225), (225, 675), LINE_WIDTH//2)  
    pygame.draw.line(screen, LINE_COLOR, (675, 225), (675, 675), LINE_WIDTH//2)  


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


def draw_game_over(screen,angle):
    restart_img = pygame.image.load("assets/restart.png")
    restart_img = pygame.transform.scale(restart_img, (150, 150))

    rotated_img = pygame.transform.rotate(restart_img, angle)
    restart_rect = rotated_img.get_rect(center=(450, 450))  # Центр фиксируем

    screen.blit(rotated_img, restart_rect.topleft)

    return restart_rect  # Возвращаем обновленный Rect


def draw_score():
    """Рисует счет под полем"""
    font = pygame.font.Font(None, 40)
    player_text = font.render(f"Игрок: {player_wins}", True, (0, 0, 0))
    bot_text = font.render(f"Бот: {bot_wins}", True, (0, 0, 0))

    screen.blit(player_text, (WIDTH // 3, HEIGHT - 100))
    screen.blit(bot_text, (WIDTH // 3 * 2, HEIGHT - 100))


def main():
    global current_player, game_over, player_wins, bot_wins
    board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # Инициализация поля
    screen = pygame.display.set_mode((900, 900))
    clock = pygame.time.Clock()
    
    running = True
    angle = 0
    direction = -1  
    

    while running:
        screen.fill(BG_COLOR)
        draw_lines()
        draw_marks(board)
        draw_score()

        if game_over:
            # Эффект размытия только на сетке
            overlay = pygame.Surface((WIDTH // 2 + 2, HEIGHT // 2 + 2))
            overlay.set_alpha(150)  # Прозрачность
            overlay.fill((255, 255, 255))  # Белый цвет
            screen.blit(overlay, (225, 225))

            # Рисуем экран завершения
            restart_button = draw_game_over(screen, angle)
            
            pygame.display.flip()
            clock.tick(30)  
            angle += 5 *direction

            # Слушаем события
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
                                player_wins += 1  # Увеличиваем счет
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
                    bot_wins += 1  # Увеличиваем счет
                    game_over = True
                elif check_draw(board):
                    print("Ничья!")
                    game_over = True
                current_player = player

        pygame.display.update()


if __name__ == "__main__":
    main()
