import pygame, sys
from pygame.locals import *
from math import sin, cos
FPS = 60
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
CELLSIZE = 100
CELLWIDTH = 100
CELLHEIGHT = 100
RADIUS = 40
ANGLE = 0



# R G B
WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
DARKGREEN = ( 0, 155, 0)
DARKGRAY = ( 40, 40, 40)
BGCOLOR = BLACK

def quitgame():
    pygame.quit()
    sys.exit()


def Dot(a, center, angle):
    center_x, center_y = center
    x, y = (RADIUS * cos(a * angle), RADIUS * sin(a * angle))
    new_center = (center_x + int(x), center_y + int(y))
    pygame.draw.circle(DISPLAYSURF, WHITE, new_center, 4)

    return new_center


def Centers():

    hcen = []
    vcen = []
    for i in range(1, WINDOWHEIGHT // CELLSIZE):
        hcenter = (CELLWIDTH // 2, CELLHEIGHT // 2 + i * CELLSIZE)
        hcen.append(hcenter)
    for i in range(1, WINDOWWIDTH // CELLSIZE):
        vcenter = (CELLWIDTH // 2 + i * CELLSIZE, CELLHEIGHT // 2)
        vcen.append(vcenter)
    return hcen, vcen


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, ANGLE

    # Initialization
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Lissajeous Curves')

    hcenters, vcenters = Centers()

    cumulative_points = []
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quitgame()

        DISPLAYSURF.fill((0, 0, 0))

        # Draw Vertical and Horizontal Lines
        for i in range(WINDOWWIDTH // CELLSIZE + 1):
            vline = pygame.Rect(i * CELLSIZE, 1, 1, WINDOWHEIGHT)
            pygame.draw.rect(DISPLAYSURF, WHITE, vline)

        for i in range(WINDOWHEIGHT // CELLSIZE):
            hline = pygame.Rect(1, i * CELLSIZE, WINDOWWIDTH, 1)
            pygame.draw.rect(DISPLAYSURF, WHITE, hline)

        # Draw all points
        for i, hcen in enumerate(hcenters):
            pygame.draw.circle(DISPLAYSURF, WHITE, hcen, RADIUS, 2)
            p_x, p_y = Dot(i + 1, hcen, ANGLE)

            pygame.draw.line(DISPLAYSURF, DARKGRAY, (p_x, p_y), (p_x + WINDOWWIDTH, p_y))
            for j, vcen in enumerate(vcenters):
                pygame.draw.circle(DISPLAYSURF, WHITE, vcen, RADIUS, 2)
                q_x, q_y = Dot(j + 1, vcen, ANGLE)
                cumulative_points.append((q_x, p_y))
                pygame.draw.line(DISPLAYSURF, DARKGRAY, (q_x, q_y), (q_x, q_y + WINDOWHEIGHT))

        for point in cumulative_points:
            pygame.draw.rect(DISPLAYSURF, WHITE, pygame.Rect(point[0], point[1], 2, 2))

        ANGLE += 0.01
        pygame.display.update()
        FPSCLOCK.tick(FPS)


main()
