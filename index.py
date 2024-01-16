import pygame
import sys

# Game parameters
ROWS = 6
COLS = 7
SQUARE_SIZE = 100
RADIUS = SQUARE_SIZE // 2 - 5
GRID_COLOR = (0, 0, 255)  # Color of the grid borders

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()

# Window size
WIDTH = COLS * SQUARE_SIZE
HEIGHT = (ROWS + 1) * SQUARE_SIZE  # Add an extra row for the title
size = (WIDTH, HEIGHT)

# Create the window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect4")

# Function to draw the game board
def draw_board(board):
    for row in range(ROWS):
        for col in range(COLS):
            # Draw the grid squares
            pygame.draw.rect(screen, GRID_COLOR, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            # Draw circles for player pieces
            pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)

    for row in range(ROWS):
        for col in range(COLS):
            # Draw red circles for player 1 pieces
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)
            # Draw yellow circles for player 2 pieces
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)

# Main game function
def main():
    board = [[0] * COLS for _ in range(ROWS)]  # Initialize an empty game board

    turn = 1  # Player 1 starts

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // SQUARE_SIZE

                # Find the first empty row in the selected column
                for row in range(ROWS - 1, -1, -1):
                    if board[row][col] == 0:
                        board[row][col] = turn
                        turn = 3 - turn  # Switch between players

                        draw_board(board)
                        pygame.display.update()

                        if check_win(board):
                            print(f"Player {3 - turn} wins!")
                            pygame.quit()
                            sys.exit()

                        break

        draw_board(board)
        pygame.display.update()

# Function to check for a winner
def check_win(board):
    # Check horizontal lines
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != 0:
                return True

    # Check vertical columns
    for col in range(COLS):
        for row in range(ROWS - 3):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != 0:
                return True

    # Check diagonals up and to the right
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] != 0:
                return True

    # Check diagonals down and to the right
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] != 0:
                return True

    return False

if __name__ == "__main__":
    main()