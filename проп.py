import pygame, sys
import numpy as np
import os

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

RED = (255, 0, 0)
BG_COLOR = (20, 200, 160)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (0, 127, 254)
CROSS_COLOR = (255, 0, 195)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

board = np.zeros((BOARD_ROWS, BOARD_COLS))
w = -1200
n = 1
c = 1
ku = 1
a = []
dne = 10
dm = 80
ne = 0
m = 80
k = 1
WHITE = (255, 255, 255)
mood = (52, 119, 107)
moo = (66, 148, 136)
BLACK = (0, 0, 0)

# SCREEN DISPLAY
mscreen = pygame.display.set_mode((1200, 900))
mscreen.fill(WHITE)
screen_zvet_moodla = pygame.Surface((1200, 70))
screen_zvet_moodla.fill(mood)
rscreen = pygame.Rect((0, 0), (1200, 900))
# MAN PLACET
image = pygame.image.load('Снимок экрана 2021-11-09 в 16.52.04.png')
image2 = pygame.image.load('aC7Qb8AelCc.png')
width = 1200
height = 900

#### ВТОРАЯ ЧАСТЬ: YUP
# surfaces with YUP
screen_text = pygame.Surface((210, 70))
screen_text.fill(WHITE)
rect = pygame.Rect(0, 0, 100, 60)
font = pygame.font.Font(None, 100)
text = font.render("YUP", True, moo)
text_rect = screen_text.get_rect(topleft=(0, 0))
rect(screen_text, moo, text_rect, 2)
screen_text.blit(text, (0, 0))
# function
def many(n, k):
    screen.blit(screen_text, (n, k))
### text
mtext = font.render(str('!!! НОЛИКИ !!! YES YES CMON CMON YES YES CMON CMON YES YES'), True, WHITE)
mtext2 = font.render(str('!!! КРЕСТИКИ !!! YES YES CMON CMON YES YES CMON CMON YES YES'), True, WHITE)


def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                                          int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True


def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        # MOODLEENDING:
        mscreen.fill(WHITE)
        mscreen.blit(screen_zvet_moodla, (0, 0))
        mscreen.blit(mtext, (w, 0))
        if w < 1200:
            w += 5
        else:
            w = -1200
        print("WIN")
        k = 1
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 2
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        k = 4
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.5
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.05
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        if ne > 600:
            ne = 0

        ne += dne
        screen.blit(image, (380, 300))
    elif player == 2:
        # MOODLEENDING:
        mscreen.fill(WHITE)
        mscreen.blit(screen_zvet_moodla, (0, 0))
        mscreen.blit(mtext2, (w, 0))
        if w < 1200:
            w += 5
        else:
            w = -1200
        print("WIN")
        k = 1
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 2
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        k = 4
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.5
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.05
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        if ne > 600:
            ne = 0

        ne += dne
        screen.blit(image2, (380, 300))


def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        # MOODLEENDING:
        mscreen.fill(WHITE)
        mscreen.blit(screen_zvet_moodla, (0, 0))
        mscreen.blit(mtext, (w, 0))
        if w < 1200:
            w += 5
        else:
            w = -1200
        print("WIN")
        k = 1
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 2
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        k = 4
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.5
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.05
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        if ne > 600:
            ne = 0

        ne += dne
        screen.blit(image, (380, 300))
    elif player == 2:
        # MOODLEENDING:
        mscreen.fill(WHITE)
        mscreen.blit(screen_zvet_moodla, (0, 0))
        mscreen.blit(mtext2, (w, 0))
        if w < 1200:
            w += 5
        else:
            w = -1200
        print("WIN")
        k = 1
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 2
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        k = 4
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.5
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.05
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        if ne > 600:
            ne = 0

        ne += dne
        screen.blit(image2, (380, 300))

    pygame.display.update()


def draw_asc_diagonal(player):
    if player == 1:
        # MOODLEENDING:
        mscreen.fill(WHITE)
        mscreen.blit(screen_zvet_moodla, (0, 0))
        mscreen.blit(mtext, (w, 0))
        if w < 1200:
            w += 5
        else:
            w = -1200
        print("WIN")
        k = 1
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 2
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        k = 4
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.5
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.05
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        if ne > 600:
            ne = 0

        ne += dne
        screen.blit(image, (380, 300))
    elif player == 2:
        # MOODLEENDING:
        mscreen.fill(WHITE)
        mscreen.blit(screen_zvet_moodla, (0, 0))
        mscreen.blit(mtext2, (w, 0))
        if w < 1200:
            w += 5
        else:
            w = -1200
        print("WIN")
        k = 1
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 2
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        k = 4
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.5
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.05
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        if ne > 600:
            ne = 0

        ne += dne
        screen.blit(image2, (380, 300))

    pygame.display.update()


def draw_desc_diagonal(player):
    if player == 1:
        # MOODLEENDING:
        mscreen.fill(WHITE)
        mscreen.blit(screen_zvet_moodla, (0, 0))
        mscreen.blit(mtext, (w, 0))
        if w < 1200:
            w += 5
        else:
            w = -1200
        print("WIN")
        k = 1
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 2
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        k = 4
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.5
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.05
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        if ne > 600:
            ne = 0

        ne += dne
        screen.blit(image, (380, 300))
    elif player == 2:
        # MOODLEENDING:
        mscreen.fill(WHITE)
        mscreen.blit(screen_zvet_moodla, (0, 0))
        mscreen.blit(mtext2, (w, 0))
        if w < 1200:
            w += 5
        else:
            w = -1200
        print("WIN")
        k = 1
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 2
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        k = 4
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.5
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)
        k = 0.05
        many(k * ne, m)
        many(k * ne, m + dm)
        many(k * ne, m + 2 * dm)
        many(k * ne, m + 3 * dm)
        many(k * ne, m + 4 * dm)
        many(k * ne, m + 5 * dm)
        many(k * ne, m + 6 * dm)
        many(k * ne, m + 7 * dm)
        many(k * ne, m + 8 * dm)
        many(k * ne, m + 9 * dm)

        if ne > 600:
            ne = 0

        ne += dne
        screen.blit(image2, (380, 300))

    pygame.display.update()


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


draw_lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square(clicked_row, clicked_col):

                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()