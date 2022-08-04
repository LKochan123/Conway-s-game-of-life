import pygame
pygame.font.init()

# Loading images
pixel10 = pygame.image.load('images/pixel_10.png')
pixel10b = pygame.image.load('images/pixel_10n.png')
pixel10g = pygame.image.load('images/pixel_10z.png')
pixel20 = pygame.image.load('images/pixel_20.png')
pixel20b = pygame.image.load('images/pixel_20n.png')
pixel20g = pygame.image.load('images/pixel_20z.png')
pixel30 = pygame.image.load('images/pixel_30.png')
pixel30b = pygame.image.load('images/pixel_30n.png')
pixel30g = pygame.image.load('images/pixel_30z.png')
start_button = pygame.image.load('images/Start-Button-Vector.png')
start_button_blue = pygame.image.load('images/start_button_blew.png')


# Text
choose_pixel_size = 'Choose pixel size of one cell'
warning = 'You must select one of the given cell size!'
welcome = 'Welcome in Conways Game of Life'

# Text font
text_choose_pixel = pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 23), choose_pixel_size, True, (0, 0, 0))
warning_text = pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 18), warning, True, (0, 0, 0))
welcome_text = pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 30), welcome, True, (0, 0, 0))