from buttons_and_pictures import *
from starting_view import *
from game_code import *
import pygame
import time

pygame.init()
window = pygame.display.set_mode((800, 600))


# Starting view
def main():

    # Help variables
    run = True

    # Need global variable to use it in other section
    global clicked_10, clicked_20, clicked_30
    clicked_10, clicked_20, clicked_30 = False, False, False

    # Buttons and images to choose pixel size
    pixel_size_10 = Button(140, 250, pixel10, 0.15, pixel10b)
    pixel_10_green = Image(140, 250, pixel10g, 0.15)
    pixel_size_20 = Button(340, 250, pixel20, 0.15, pixel20b)
    pixel_20_green = Image(340, 250, pixel20g, 0.15)
    pixel_size_30 = Button(540, 250, pixel30, 0.15, pixel30b)
    pixel_30_green = Image(540, 250, pixel30g, 0.15)
    start_game_of_live = Button(280, 400, start_button, 0.15, start_button_blue)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill((217, 112, 74))
        window.blit(welcome_text, (160, 50))
        window.blit(text_choose_pixel, (230, 110))
        pixel_size_10.draw()
        pixel_size_20.draw()
        pixel_size_30.draw()
        start_game_of_live.draw()

        # In this section you can choose pixel size and it change color to green
        if pixel_size_10.tick() or clicked_10:
            if clicked_20 or clicked_30:
                clicked_20, clicked_30 = False, False
            else:
                clicked_10 = True
                pixel_10_green.draw()

        if pixel_size_20.tick() or clicked_20:
            if clicked_10 or clicked_30:
                clicked_10, clicked_30 = False, False
            else:
                clicked_20 = True
                pixel_20_green.draw()

        if pixel_size_30.tick() or clicked_30:
            if clicked_10 or clicked_20:
                clicked_10, clicked_20 = False, False
            else:
                clicked_30 = True
                pixel_30_green.draw()

        if start_game_of_live.tick():
            if clicked_10 or clicked_20 or clicked_30:
                conways_game()
            else:
                window.blit(warning_text, (215, 500))

        pygame.display.update()


def conways_game():

    # Help variables
    run, progress, temp = True, False, False
    pixel_size = ''

    if clicked_10:
        pixel_size = 10
    if clicked_20:
        pixel_size = 20
    if clicked_30:
        pixel_size = 30

    n, m = N // pixel_size, M // pixel_size
    cells = [[0] * m for _ in range(n)]
    GofL = GameOfLife(pixel_size)

    window.fill((40, 40, 40))
    pygame.draw.line(window, (12, 104, 173), (600, 0), (600, 600), 1)  # blue line
    # pixel_size_10.draw()

    GofL.update(window, cells)
    pygame.display.flip()
    pygame.display.update()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # We can start and stop animation
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    progress = not progress
                    GofL.update(window, cells)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if x < 600:
                    cells[y // pixel_size][x // pixel_size] = 1
                    GofL.update(window, cells)
                    pygame.display.update()

        if progress:
            cells = GofL.update(window, cells, True)
            pygame.display.update()

        time.sleep(0.001)


if __name__ == "__main__":
    main()