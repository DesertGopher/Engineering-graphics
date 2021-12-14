import pygame
import math

pygame.init()
screen = pygame.display.set_mode([600, 600])
white = [255, 255, 255]
black = [0, 0, 0]
bg = [240, 240, 240]
step_color = [200, 200, 200]
purple = [128, 0, 128]
red = [255, 0, 0]
blue = [107, 153, 255]
blue_step = [0, 0, 255]
screen.fill(bg)
pygame.display.set_caption("Вращение многоугольника")
pygame.display.flip()

# -----Произвольная точка-----#
global point1
global point2
point1 = 300
point2 = 300


def point():
    pygame.draw.circle(screen, black,
                       (point1, point2), 4)
    pygame.draw.line(screen, blue, [point1, point2], [point1, 0], 1)
    pygame.draw.line(screen, blue, [point1, point2], [0, point2], 1)


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
                     [0, 0],
                     [0, 600], 3)
    pygame.draw.line(screen, black,
                     [0, 0],
                     [600, 0], 3)
    pygame.draw.circle(screen, black,
                       (0, 0), 6)

    # -----Стрелочки на осях-----#
    pygame.draw.line(screen, black,
                     [600, 0],
                     [590, 5], 3)

    pygame.draw.line(screen, black,
                     [0, 600],
                     [5, 590], 3)

    font = pygame.font.Font(None, 25)
    textX = font.render("X", True, black)
    textY = font.render("Y", True, black)
    screen.blit(textX, [590, 10])
    screen.blit(textY, [10, 585])
    font_step = pygame.font.Font(None, 18)
    j = int(50)
    n = 10
    for i in range(1, 60):
        pygame.draw.line(screen, black,
                         [n, 0],
                         [n, 5], 1)
        pygame.draw.line(screen, black,
                         [0, n],
                         [5, n], 1)

        if i % 5 == 0:
            text_step = font_step.render(str(j), True, black)
            screen.blit(text_step, [n - 9, 10])
            screen.blit(text_step, [10, n - 5])
            pygame.draw.line(screen, blue_step,
                             [2, n],
                             [8, n], 2)
            pygame.draw.line(screen, blue_step,
                             [n, 2],
                             [n, 8], 2)
            j += 50
        n += 10
    # pygame.draw.lines(screen, red, True, [[350, 350], [400, 320], [370, 310]], 2)


axes()
point()
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    clock.tick(150)
    for i in range(1, 361, 1):
        clock.tick(150)
        angle = i * math.pi / 180

        '''
        a1 = 100 * math.cos(angle) + point1
        b1 = 100 * math.sin(angle) + point2
        a2 = 150 * math.cos(angle) + point1
        b2 = 70 * math.sin(angle) + point2
        a3 = 180 * math.cos(angle) + point1
        b3 = 210 * math.sin(angle) + point2
        '''

        a1 = point1 + math.cos(angle) * (250 - point1) - math.sin(angle) * (250 - point2)
        b1 = point2 + math.sin(angle) * (250 - point1) + math.cos(angle) * (250 - point2)
        a2 = point1 + math.cos(angle) * (350 - point1) - math.sin(angle) * (250 - point2)
        b2 = point2 + math.sin(angle) * (350 - point1) + math.cos(angle) * (250 - point2)
        a3 = point1 + math.cos(angle) * (300 - point1) - math.sin(angle) * (200 - point2)
        b3 = point2 + math.sin(angle) * (300 - point1) + math.cos(angle) * (200 - point2)

        a_neg = -100 * math.cos(angle) + point1
        b_neg = 100 * math.sin(angle) + point2

        axes()
        point()

        pygame.draw.lines(screen, purple, True,
                          [[a1, b1], [a2, b2],
                           [a3, b3]], 3)
        pygame.draw.lines(screen, blue_step, True,
                          [[a_neg - 30, b_neg - 10], [a_neg + 30, b_neg - 10],
                           [a_neg, b_neg + 30]], 3)

        pygame.draw.circle(screen, black,
                           (a1, b1), 3)
        pygame.draw.circle(screen, black,
                           (a2, b2), 3)
        pygame.draw.circle(screen, black,
                           (a3, b3), 3)

        pygame.draw.line(screen, red, [a1, b1], [point1, point2], 1)
        pygame.draw.line(screen, red, [a2, b2], [point1, point2], 1)
        pygame.draw.line(screen, red, [a3, b3], [point1, point2], 1)

        pygame.draw.circle(screen, black,
                           (a_neg, b_neg), 3)

        pygame.draw.line(screen, red, [a_neg - 30, b_neg - 10], [a_neg, b_neg], 1)
        pygame.draw.line(screen, red, [a_neg + 30, b_neg - 10], [a_neg, b_neg], 1)
        pygame.draw.line(screen, red, [a_neg, b_neg + 30], [a_neg, b_neg], 1)
        pygame.draw.line(screen, red, [a_neg, b_neg], [point1, point2], 1)

        pygame.display.update()
