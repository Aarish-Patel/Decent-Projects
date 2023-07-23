import pygame as pg

pg.init()
LENGTH = 900
BREADTH = 900
screen = None
running = False
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
tx = 0
ty = 0
highlighted = True
column = 1
row = 1
num = "0"
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

gridperma = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],

             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],

             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def draw_temp():
    global grid, screen, LENGTH, BREADTH, GREY
    FONT = pg.font.Font('freesansbold.ttf', 32)
    for r in range(9):
        for c in range(9):
            if grid[r][c] != 0:
                # print(grid[r][c])
                textsurface = FONT.render(str(grid[r][c]), False, GREY)
                screen.blit(textsurface, (c * BREADTH / 9 + 75, r * LENGTH / 9 + 65))


def draw_perma():
    global gridperma, screen, LENGTH, BREADTH, GREY, BLACK
    FONT = pg.font.Font('freesansbold.ttf', 64)
    for r in range(9):
        for c in range(9):
            if gridperma[r][c] != 0:
                # print(gridperma[r][c])
                text = FONT.render(str(gridperma[r][c]), False, BLACK)
                screen.blit(text, (c * BREADTH / 9 + 35, r * LENGTH / 9 + 25))


# def grid():
#     global gridperma


def main():
    global running, screen, BLACK, RED, column, row, num, grid
    screen = pg.display.set_mode((LENGTH, BREADTH))
    pg.display.set_caption("Sudoku")
    running = True
    while running:
        screen.fill((255, 255, 255))
        draw_temp()
        draw_perma()
        for event in pg.event.get():
            # checking whether the event is exit()
            if event.type == pg.QUIT:
                # exiting the loop by making the loop control variable false
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    column = column - 1
                    if column <= 0:
                        column = 9
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    column = column + 1
                    if column > 9:
                        column = 1
                if event.key == pg.K_UP or event.key == pg.K_w:
                    row = row - 1
                    if row <= 0:
                        row = 9
                if event.key == pg.K_DOWN or event.key == pg.K_s:
                    row = row + 1
                    if row > 9:
                        row = 1
                if event.key == pg.K_1 or event.key == pg.K_KP1:
                    grid[row - 1][column - 1] = 1
                if event.key == pg.K_2 or event.key == pg.K_KP2:
                    grid[row - 1][column - 1] = 2
                if event.key == pg.K_3 or event.key == pg.K_KP3:
                    grid[row - 1][column - 1] = 3
                if event.key == pg.K_4 or event.key == pg.K_KP4:
                    grid[row - 1][column - 1] = 4
                if event.key == pg.K_5 or event.key == pg.K_KP5:
                    grid[row - 1][column - 1] = 5
                if event.key == pg.K_6 or event.key == pg.K_KP6:
                    grid[row - 1][column - 1] = 6
                if event.key == pg.K_7 or event.key == pg.K_KP7:
                    grid[row - 1][column - 1] = 7
                if event.key == pg.K_8 or event.key == pg.K_KP8:
                    grid[row - 1][column - 1] = 8
                if event.key == pg.K_9 or event.key == pg.K_KP9:
                    grid[row - 1][column - 1] = 9
                if event.key == pg.K_RETURN:
                    gridperma[row - 1][column - 1] = grid[row - 1][column - 1]
                    grid[row - 1][column - 1] = 0
                if event.key == pg.K_BACKSPACE:
                    grid[row - 1][column - 1] = 0
                if event.key == pg.K_ESCAPE or event.key == pg.K_DELETE:
                    gridperma[row - 1][column - 1] = grid[row - 1][column - 1]
                if event.key == pg.K_n:
                    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],

                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],

                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for i in range(9):
            if i % 3 != 0:
                pg.draw.line(screen, BLACK, ((LENGTH / 9) * i, 0), ((LENGTH / 9) * i, BREADTH), 5)
                pg.draw.line(screen, BLACK, (0, (BREADTH / 9) * i), (LENGTH, (BREADTH / 9) * i), 5)
            else:
                pg.draw.line(screen, BLACK, ((LENGTH / 9) * i, 0), ((LENGTH / 9) * i, BREADTH), 10)
                pg.draw.line(screen, BLACK, (0, (BREADTH / 9) * i), (LENGTH, (BREADTH / 9) * i), 10)

        if highlighted:
            pg.draw.line(screen, RED, (LENGTH / 9 * (column - 1), BREADTH / 9 * row),
                         (LENGTH / 9 * (column - 1), BREADTH / 9 * (row - 1)), 7)
            pg.draw.line(screen, RED, (LENGTH / 9 * column, BREADTH / 9 * row),
                         (LENGTH / 9 * column, BREADTH / 9 * (row - 1)), 7)
            pg.draw.line(screen, RED, (LENGTH / 9 * column, BREADTH / 9 * row),
                         (LENGTH / 9 * (column - 1), BREADTH / 9 * row), 7)
            pg.draw.line(screen, RED, (LENGTH / 9 * column, BREADTH / 9 * (row - 1)),
                         (LENGTH / 9 * (column - 1), BREADTH / 9 * (row - 1)), 7)

        pg.display.update()

        # print(grid)
        # print(gridperma)


main()
