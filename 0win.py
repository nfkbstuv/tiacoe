import pygame as p
from pygame.draw import *

p.init()


score = 0
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
screen = p.display.set_mode((1200, 900))
screen.fill(WHITE)
screen_zvet_moodla = p.Surface((1200, 70))
screen_zvet_moodla.fill(mood)
rscreen = p.Rect((0, 0), (1200, 900))
# MAN PLACET
image = p.image.load('Снимок экрана 2021-11-09 в 16.52.04.png')
width = 1200
height = 900

#### ВТОРАЯ ЧАСТЬ: YUP
# surfaces with YUP
screen_text = p.Surface((210, 70))
screen_text.fill(WHITE)
font = p.font.Font(None, 100)
text = font.render("YUP", True, moo)
text_rect = screen_text.get_rect(topleft=(0, 0))
rect(screen_text, moo, text_rect, 2)
screen_text.blit(text, (0, 0))
# function
def many(n, k):
    screen.blit(screen_text, (n, k))
### text
mtext = font.render(str('!!! НОЛИКИ !!! YES YES CMON CMON YES YES CMON CMON YES YES'), True, WHITE)

    #MOODLEENDING:
        screen.fill(WHITE)
        screen.blit(screen_zvet_moodla, (0, 0))
        screen.blit(mtext, (w, 0))
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
    else:
        n += 1


    p.display.update()


p.quit()
# THE END OF THE GAME - NOLIKI WINS
