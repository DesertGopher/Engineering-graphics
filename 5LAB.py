import sys
import pygame
import numpy as np
from math import *

pygame.init()
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
blue_step = [0, 0, 255]
bg = [240, 240, 240]
step_color = [200, 200, 200]
purple = [128, 0, 128]
COLOR = blue

WIDTH, HEIGHT = 600, 600
pygame.display.set_caption("Алгоритм Брезенхема.")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SIZE = [9, 9]


def axes():
    step = 10
    screen.fill(bg)
    for i in range(1, 60):
        pygame.draw.line(screen, step_color,
                         [step, 0],
                         [step, 600], 1)
        pygame.draw.line(screen, step_color,
                         [0, step],
                         [600, step], 1)
        step += 10
    pygame.draw.line(screen, black,
                     [300, 0],
                     [300, 600], 2)
    pygame.draw.line(screen, black,
                     [0, 300],
                     [600, 300], 2)
    pygame.draw.circle(screen, black,
                       (300, 300), 3)
    pygame.draw.line(screen, black,
                     [600, 300],
                     [590, 305], 2)
    pygame.draw.line(screen, black,
                     [600, 300],
                     [590, 295], 2)

    pygame.draw.line(screen, black,
                     [300, 600],
                     [305, 590], 2)
    pygame.draw.line(screen, black,
                     [300, 600],
                     [295, 590], 2)

    font = pygame.font.Font(None, 25)
    textX = font.render("X", True, black)
    textY = font.render("Y", True, black)
    screen.blit(textX, [590, 310])
    screen.blit(textY, [310, 585])
    font_step = pygame.font.Font(None, 18)
    j = int(-250)
    n = 10
    for i in range(1, 60):
        pygame.draw.line(screen, black,
                         [n, 298],
                         [n, 302], 1)
        pygame.draw.line(screen, black,
                         [298, n],
                         [302, n], 1)
        if i % 5 == 0:
            if j != 0:
                text_step = font_step.render(str(int(j/10)), True, black)
                screen.blit(text_step, [n - 9, 310])
                screen.blit(text_step, [310, n - 5])
                pygame.draw.line(screen, blue_step,
                                 [296, n],
                                 [304, n], 2)
                pygame.draw.line(screen, blue_step,
                                 [n, 296],
                                 [n, 304], 2)
            elif j == 0:
                text_step = font_step.render(str(int(j/10)), True, black)
                screen.blit(text_step, [310, 310])
                pygame.draw.line(screen, blue_step,
                                 [296, n],
                                 [304, n], 2)
                pygame.draw.line(screen, blue_step,
                                 [n, 296],
                                 [n, 304], 2)
            j += 50
        n += 10


def draw_pixel(position, COLOR):
    global SIZE
    screen.fill(COLOR, (position, SIZE))

axes()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    ras = 16
    d = 0
    x = 0
    y = ras
    for i in range(23):
        clock.tick(10)
        if d < 0:
            if abs(pow((x + 1), 2) + pow(y, 2) - pow(ras, 2)) - abs(pow((x + 1), 2) + pow(y - 1, 2) - pow(ras, 2)) <= 0:
                x += 1
                y = y
                d = d + 2 * x + 1
            else:
                x += 1
                y -= 1
                d = d + 2 * x - 2 * y + 2
        elif (d > 0):
            if abs(pow((x + 1), 2) + pow(y - 1, 2) - pow(ras, 2)) - abs(pow((x), 2) + pow(y - 1, 2) - pow(ras, 2)) <= 0:
                x += 1
                y -= 1
                d = d + 2 * x - 2 * y + 2
            else:
                x = x
                y -= 1
                d = d + 2 * x - 2 * y + 2
        else:
            x = x
            y -= 1
            d = d - 2 * y + 1
        draw_pixel([x * 10 + 300, y * 10 + 300], red)
        draw_pixel([-(x * 10) + 300, y * 10 + 300], blue)
        draw_pixel([-(x * 10) + 300, -(y * 10) + 300], green)
        draw_pixel([x * 10 + 300, -(y * 10) + 300], purple)
        pygame.display.update()
