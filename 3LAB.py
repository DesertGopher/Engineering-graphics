import pygame
import math

pygame.init()
screen = pygame.display.set_mode([690, 490])

# Цвета
white = [255, 255, 255]
black = [0, 0, 0]
bg = [240, 240, 240]
step_color = [200, 200, 200]
purple = [128, 0, 128]
red = [255, 0, 0]
blue = [107, 153, 255]


blue_step = [0, 0, 255]
green=[0,255,0]

screen.fill(bg)
pygame.display.set_caption("Говно")

x = [280, 200, 270, 480, 550, 490]
y = [340, 270, 80, 70, 210, 310]

#x = [210, 160, 290, 600, 470, 350]
#y = [380, 100, 200, 170, 390, 270]

#160, 100 --- 600, 170     445.53
#210, 380 --- 470, 390     260.19

line_1 = [x[0], y[0], x[1], y[1]]
line_2 = [x[1], y[1], x[2], y[2]]
line_3 = [x[2], y[2], x[3], y[3]]
line_4 = [x[3], y[3], x[4], y[4]]
line_5 = [x[4], y[4], x[5], y[5]]
line_6 = [x[5], y[5], x[0], y[0]]

lines = [line_1, line_2, line_3, line_4,
         line_5, line_6]

diagonals = []
itog = [[1,1,2,2]]


def axes():
    pygame.draw.line(screen, black,
                     [0, 0],
                     [0, 490], 3)
    pygame.draw.line(screen, black,
                     [0, 0],
                     [690, 0], 3)
    pygame.draw.circle(screen, black,
                       (0, 0), 6)

    # -----Стрелочки на осях-----#
    pygame.draw.line(screen, black,
                     [690, 0],
                     [680, 5], 3)

    pygame.draw.line(screen, black,
                     [0, 490],
                     [5, 480], 3)

    font = pygame.font.Font(None, 25)
    textX = font.render("X", True, black)
    textY = font.render("Y", True, black)
    screen.blit(textX, [680, 10])
    screen.blit(textY, [10, 475])
    font_step = pygame.font.Font(None, 18)
    j = int(50)
    n = 10
    for i in range(1, 80):
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
def draw_polygon():
    pygame.draw.lines(screen, black, True,
                      [[x[0], y[0]], [x[1], y[1]], [x[2], y[2]], [x[3], y[3]],
                       [x[4], y[4]], [x[5], y[5]]], 2)
def draw_diagonal_red(x1, y1, x2, y2):
    pygame.draw.line(screen, red, [x1, y1], [x2, y2], 1)
def draw_diagonal(x1, y1, x2, y2):
    pygame.draw.line(screen, black, [x1, y1], [x2, y2], 1)
def draw_diagonal_white(x1, y1, x2, y2):
    pygame.draw.line(screen, bg, [x1, y1], [x2, y2], 1)
def draw_diagonal_purple(x1, y1, x2, y2):
    pygame.draw.line(screen, purple, [x1, y1], [x2, y2], 1)
def check_crossing(x1, y1, x2, y2):
    diagonal = x1 * y2 - x2 * y1
    A1 = y1 - y2
    B1 = x2 - x1
    equations(diagonal, A1, B1, x1, y1, x2, y2)


def equations(C1, A1, B1, x1, y1, x2, y2):
    check = int(0)
    for n in [0, 1, 2, 3, 4, 5]:
        A2 = lines[n][1] - lines[n][3]
        B2 = lines[n][2] - lines[n][0]
        C2 = lines[n][0] * lines[n][3] - lines[n][2] * lines[n][1]
        #check = int(0)

        if B1 * A2 - B2 * A1 != 0 and A1 != 0:
            Y_POINT = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
            X_POINT = (-C1 - B1 * Y_POINT) / A1

            if (min(x1, x2) < X_POINT < max(x1, x2) and
                min(y1, y2) < Y_POINT < max(y1, y2)) and \
                    (min(lines[n][0], lines[n][2]) < X_POINT < max(lines[n][0], lines[n][2]) and
                     min(lines[n][1], lines[n][3]) < Y_POINT < max(lines[n][1], lines[n][3])):
                check += 1
                #pygame.draw.circle(screen, red, (X_POINT, Y_POINT), 3)

        elif B1 * A2 - B2 * A1 != 0 and A2 != 0:
            Y_POINT = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
            X_POINT = (-C2 - B2 * Y_POINT) / A2

            if (min(x1, x2) < X_POINT < max(x1, x2) and
                min(y1, y2) < Y_POINT < max(y1, y2)) and \
                    (min(lines[n][0], lines[n][2]) < X_POINT < max(lines[n][0], lines[n][2]) and
                     min(lines[n][1], lines[n][3]) < Y_POINT < max(lines[n][1], lines[n][3])):
                check += 1

        elif B1 * A2 - B2 * A1 == 0:  # условие параллельности
            draw_diagonal(x1, y1, x2, y2)

    if 0.6 > ((math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1))) % 445) > 0.5:
        #draw_diagonal_white(x1, y1, x2, y2)
        pass
    elif 0.2 > ((math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1))) % 260) > 0.1:
        #draw_diagonal_white(x1, y1, x2, y2)
        pass
    elif check != 0:
        #draw_diagonal_white(x1, y1, x2, y2)
        pass
    elif check == 0:
        C1 = x1 * y2 - x2 * y1
        A1 = y1 - y2
        B1 = x2 - x1
        diag_equations(C1, A1, B1, x1, y1, x2, y2)
    draw_polygon()




def diag_equations(C1, A1, B1, x1, y1, x2, y2):
    check = int(0)
    for n in range(0, int(len(itog))):
        print(n)
        A2 = itog[n][1] - itog[n][3]
        B2 = itog[n][2] - itog[n][0]
        C2 = itog[n][0] * itog[n][3] - itog[n][2] * itog[n][1]
        #check = int(0)

        if B1 * A2 - B2 * A1 != 0 and A1 != 0:
            Y_POINT = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
            X_POINT = (-C1 - B1 * Y_POINT) / A1

            if (min(x1, x2) < X_POINT < max(x1, x2) and
                min(y1, y2) < Y_POINT < max(y1, y2)) and \
                    (min(itog[n][0], itog[n][2]) < X_POINT < max(itog[n][0], itog[n][2]) and
                     min(itog[n][1], itog[n][3]) < Y_POINT < max(itog[n][1], itog[n][3])):
                        check += 1
                        #pygame.draw.circle(screen, green, (X_POINT, Y_POINT), 3)

        elif B1 * A2 - B2 * A1 != 0 and A2 != 0:
            Y_POINT = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
            X_POINT = (-C2 - B2 * Y_POINT) / A2

            if (min(x1, x2) < X_POINT < max(x1, x2) and
                min(y1, y2) < Y_POINT < max(y1, y2)) and \
                    (min(itog[n][0], itog[n][2]) < X_POINT < max(itog[n][0], itog[n][2]) and
                     min(itog[n][1], itog[n][3]) < Y_POINT < max(itog[n][1], itog[n][3])):
                        check += 1

    if 0.6 > ((math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1))) % 445) > 0.5:
        #draw_diagonal_white(x1, y1, x2, y2)
        pass
    elif 0.2 > ((math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1))) % 260) > 0.1:
        #draw_diagonal_white(x1, y1, x2, y2)
        pass
    elif check != 0:
        #draw_diagonal_white(x1, y1, x2, y2)
        pass
    elif check == 0:
        sos = [x1, y1, x2, y2]
        itog.append(sos)
        #draw_diagonal_purple(x1, y1, x2, y2)



for i in [0, 1, 2, 3, 4, 5]:
    for j in [1, 2, 3, 4, 5, 0]:
        sas = [x[i], y[i], x[j], y[j]]
        diagonals.append(sas)
        check_crossing(x[i], y[i], x[j], y[j])

print(itog)
print(len(itog))

for zuz in range(0, len(itog)):
    draw_diagonal_purple(itog[zuz][0], itog[zuz][1], itog[zuz][2], itog[zuz][3])
axes()
draw_polygon()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
