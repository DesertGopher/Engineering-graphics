import pygame
import math
import numpy

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
white = [255, 255, 255]
black = [0, 0, 0]
bg = [240, 240, 240]
step_color = [200, 200, 200]
purple = [128, 0, 128]
red = [255, 0, 0]
blue = [107, 153, 255]
blue_step = [0, 0, 255]
screen.fill(bg)
pygame.display.set_caption("Алгоритм плавающего горизонта")
pygame.display.flip()

hh = [1000]
lh = [1000]

alpha = float(25)
beta = float(15)
global TransY
global TransX
TransX = math.sin(beta * math.pi / 180) / math.cos(beta * math.pi / 180)
TransY = math.sin(alpha * math.pi / 180) / math.cos(alpha * math.pi / 180)

dz = float(0.2)
i = int()
gd = int()
gm = int()
d = float()
x = float()
y = float()
z = float()
dx = float()
moveto_x = int()
moveto_y = int()

clock = pygame.time.Clock()


def draw_line(x1, y1, x2, y2):
    pygame.draw.line(screen, purple, [x1, y1], [x2, y2], 1)


size_x = int(WIDTH / 2)
size_y = int(HEIGHT / 2)

for i in range(0, 1001, 1):
    hh.append(-10000)
    lh.append(10000)
x = math.pi
z = -2 * math.pi
y = 8 * math.cos(1.2 * math.sqrt(x * x + z * z)) / (math.sqrt(x * x + z * z) + 1)
dx = 4 * math.pi / 1000

moveto_x = x / dx + size_x
moveto_y = size_y


while True:
    clock.tick(60)
    moveto_x = 10
    moveto_y = (size_y - y * 30)
    for i in range(0, 1001, 1):
        x = -2 * math.pi + dx * i
        y = 8 * math.cos(1.2 * math.sqrt(x * x + z * z)) / (math.sqrt(x * x + z * z) + 1)

        if (y * 30 > hh[i]):
            a = x / dx + size_x
            b = size_y - y * 30
            draw_line(moveto_x, moveto_y, a, b)
            hh[i] = y * 30
        if (y * 30 < lh[i]):
            a = x / dx + size_x
            b = size_y - y * 30
            draw_line(moveto_x, moveto_y, a, b)
            lh[i] = y * 30

        moveto_x = x / dx + size_x
        moveto_y = size_y - y * 30
    z = z + dz

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()
