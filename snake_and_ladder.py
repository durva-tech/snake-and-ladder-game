import pygame
import random
import sys

# -------------------- INITIAL SETUP --------------------
pygame.init()

WIDTH, HEIGHT = 600, 650
CELL_SIZE = 60
ROWS = COLS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and Ladder")

font = pygame.font.SysFont("arial", 24)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
BLUE = (30, 144, 255)

clock = pygame.time.Clock()

# -------------------- SNAKES & LADDERS --------------------
snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2
}

ladders = {
    6: 25,
    11: 40,
    60: 85,
    46: 90
}

# -------------------- FUNCTIONS --------------------
def draw_board():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

def get_coordinates(position):
    position -= 1
    row = position // 10
    col = position % 10

    if row % 2 == 1:
        col = 9 - col

    x = col * CELL_SIZE + CELL_SIZE // 2
    y = HEIGHT - (row * CELL_SIZE + CELL_SIZE // 2) - 50
    return x, y

def roll_dice():
    return random.randint(1, 6)

def draw_player(position, color):
    if position > 0:
        x, y = get_coordinates(position)
        pygame.draw.circle(screen, color, (x, y), 15)

def check_snake_ladder(position):
    if position in snakes:
        return snakes[position]
    if position in ladders:
        return ladders[position]
    return position

def draw_text(text, x, y):
    label = font.render(text, True, BLACK)
    screen.blit(label, (x, y))

# -------------------- GAME VARIABLES --------------------
player_red = 0
player_blue = 0
turn = "RED"
dice_value = 0

# -------------------- GAME LOOP --------------------
running = True
while running:
    clock.tick(30)
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_value = roll_dice()

                if turn == "RED":
                    if player_red + dice_value <= 100:
                        player_red += dice_value
                        player_red = check_snake_ladder(player_red)
                    if dice_value != 6:
                        turn = "BLUE"

                else:
                    if player_blue + dice_value <= 100:
                        player_blue += dice_value
                        player_blue = check_snake_ladder(player_blue)
                    if dice_value != 6:
                        turn = "RED"

    draw_player(player_red, RED)
    draw_player(player_blue, BLUE)

    draw_text(f"Dice: {dice_value}", 10, HEIGHT - 45)
    draw_text(f"Turn: {turn}", 200, HEIGHT - 45)
    draw_text("Press SPACE to roll dice", 350, HEIGHT - 45)

    if player_red == 100:
        draw_text("RED WINS!", 250, HEIGHT // 2)
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    if player_blue == 100:
        draw_text("BLUE WINS!", 250, HEIGHT // 2)
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    pygame.display.update()

pygame.quit()