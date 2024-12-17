import pygame
import sys
from collections import Counter

pygame.init()

# Game constants
WORD_LENGTH = 5
MAX_ATTEMPTS = 6
SECRET_WORD = "nisse"  # A Norwegian Christmas-related word
FONT_SIZE = 40
LETTER_SPACING = 10
TOP_MARGIN = 100
LEFT_MARGIN = 100
SQUARE_SIZE = 60

# Colors
BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
GREEN = (106, 170, 100)
YELLOW = (201, 180, 88)
GRAY = (120, 124, 126)
WHITE = (255, 255, 255)

# Initialize screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle-like Game (NISSE)")

# Fonts
font = pygame.font.SysFont("Arial", FONT_SIZE, bold=True)
msg_font = pygame.font.SysFont("Arial", 50, bold=True)

# Game state
attempts = [[""] * WORD_LENGTH for _ in range(MAX_ATTEMPTS)]
attempt_colors = [[WHITE] * WORD_LENGTH for _ in range(MAX_ATTEMPTS)]
current_attempt = 0
current_letter_index = 0
game_over = False
win = False

def check_word(guess, secret):
    # Returns a list of colors for each letter in the guess
    result_colors = [GRAY] * WORD_LENGTH
    secret_count = Counter(secret)

    # First pass: mark green
    for i, (g_char, s_char) in enumerate(zip(guess, secret)):
        if g_char == s_char:
            result_colors[i] = GREEN
            secret_count[g_char] -= 1

    # Second pass: mark yellow
    for i, g_char in enumerate(guess):
        if result_colors[i] == GRAY and g_char in secret_count and secret_count[g_char] > 0:
            result_colors[i] = YELLOW
            secret_count[g_char] -= 1

    return result_colors

def draw_board():
    screen.fill(BG_COLOR)
    # Draw attempts
    for row in range(MAX_ATTEMPTS):
        for col in range(WORD_LENGTH):
            letter = attempts[row][col]
            color = attempt_colors[row][col]
            x = LEFT_MARGIN + col * (SQUARE_SIZE + LETTER_SPACING)
            y = TOP_MARGIN + row * (SQUARE_SIZE + LETTER_SPACING)

            # Draw square
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE), border_radius=5)
            # Draw letter
            if letter:
                letter_surf = font.render(letter.upper(), True, (0,0,0) if color != WHITE else TEXT_COLOR)
                lw, lh = letter_surf.get_size()
                screen.blit(letter_surf, (x + (SQUARE_SIZE - lw) / 2, y + (SQUARE_SIZE - lh) / 2))
    
    # If game over, display message
    if game_over:
        if win:
            msg = "You Win!"
        else:
            msg = f"You Lose! The word was {SECRET_WORD.upper()}"
        msg_surf = msg_font.render(msg, True, WHITE)
        mw, mh = msg_surf.get_size()
        screen.blit(msg_surf, ((WIDTH - mw)/2, HEIGHT - mh - 50))

    pygame.display.flip()

def handle_keydown(event):
    global current_letter_index, current_attempt, game_over, win

    if game_over:
        # Pressing Esc to quit after game over
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        return

    # Allow letter input if not game over
    if event.key == pygame.K_BACKSPACE:
        if current_letter_index > 0:
            current_letter_index -= 1
            attempts[current_attempt][current_letter_index] = ""
    elif event.key == pygame.K_RETURN:
        # Submit word if full
        if current_letter_index == WORD_LENGTH:
            guess = "".join(attempts[current_attempt])
            # We can just check length and guess since we have a fixed secret word
            # In a bigger game you'd verify if guess is in a dictionary
            if len(guess) == WORD_LENGTH:
                # Process guess
                colors = check_word(guess, SECRET_WORD)
                attempt_colors[current_attempt] = colors
                
                if guess == SECRET_WORD:
                    game_over = True
                    win = True
                else:
                    current_attempt += 1
                    current_letter_index = 0
                    if current_attempt == MAX_ATTEMPTS:
                        game_over = True
    elif event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    else:
        # Letter keys
        if event.unicode.isalpha():
            char = event.unicode.lower()
            if current_letter_index < WORD_LENGTH:
                attempts[current_attempt][current_letter_index] = char
                current_letter_index += 1

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handle_keydown(event)

    draw_board()

pygame.quit()
sys.exit()
