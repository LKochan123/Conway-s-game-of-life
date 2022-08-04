import pygame

# Colors
COLOR_BG = (10, 10, 10)
COLOR_ALIVE = (255, 255, 255)
COLOR_DIE = (170, 170, 170)
COLOR_GRID = (40, 40, 40)

# size of platform
M, N = 600, 600


class GameOfLife:

    def __init__(self, pixel_size):
        self.pixel = pixel_size
        self.n = N // pixel_size
        self.m = M // pixel_size

    def update(self, screen, cells, progress=False):
        pixel = self.pixel
        n, m = self.n, self.m

        updated_cells = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                neighbours = self.count_nei(cells, i, j)
                color = COLOR_BG if not cells[i][j] else COLOR_ALIVE

                if cells[i][j]:
                    if neighbours in [2, 3]:
                        updated_cells[i][j] = 1
                        if progress:
                            color = COLOR_ALIVE
                    else:
                        if progress:
                            color = COLOR_DIE
                else:
                    if neighbours == 3:
                        updated_cells[i][j] = 1
                        if progress:
                            color = COLOR_ALIVE
                    else:
                        if progress:
                            color = COLOR_DIE

                pygame.draw.rect(screen, color, (j * pixel, i * pixel, pixel - 1, pixel - 1))

        return updated_cells

    def count_nei(self, cells, i, j):
        n, m = self.n, self.m
        counter = 0

        for row in range(i-1, i+2):
            for col in range(j-1, j+2):
                if row < 0 or col < 0 or row == n or col == m or\
                        (row == i and col == j):
                    continue
                else:
                    if cells[row][col] == 1:
                        counter += 1

        return counter