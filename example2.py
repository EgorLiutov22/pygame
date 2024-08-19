import pygame
from pygame import QUIT


class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image


pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')
sprite_sheet_image = pygame.image.load('dino.png').convert_alpha()

BG = (50, 50, 50)
sprite_sheet = SpriteSheet(sprite_sheet_image)
animation_list = []
animation_steps = [4, 6, 3, 4]
action = 0
step_counter = 0
for animation in animation_steps:
   temp_img_list = []
   for _ in range(animation):
       temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK))
       step_counter += 1
   animation_list.append(temp_img_list)


run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0

    screen.fill(BG)
    last_update = pygame.time.get_ticks()
    animation_cooldown = 500
    frame = 0
    if frame >= len(animation_list[action]):
        frame = 0

    screen.blit(animation_list[action][frame], (0, 0))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time



    pygame.display.update()

pygame.quit()
