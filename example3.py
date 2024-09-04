import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((640, 320))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = 100


light = pygame.image.load('light.png')
light = pygame.transform.scale(light, (100, 50))
player = Player()
light_on = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            light_on = True
        if event.type == pygame.KEYUP and event.key == pygame.K_f:
            light_on = False
        screen.fill(pygame.color.Color('Gray'))
        seep = pygame.surface.Surface((640, 320))
        seep.fill(pygame.color.Color('Gray'))
        if light_on:
            seep.blit(light, (player.rect.x, player.rect.y + 20))
        screen.blit(seep, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
