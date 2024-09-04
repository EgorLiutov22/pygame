import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 50, 100)
        self.image = pygame.image.load('player.png')
        self.xvel = 0

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, left, right):
        if left:
            self.xvel -= 3

        if right:
            self.xvel += 3
        if not (left or right):
            self.xvel = 0
        self.rect.x += self.xvel


light = pygame.image.load('light.png')
light = pygame.transform.scale(light, (100, 50))
player = Player(400, 400)
light_on = False
left = False
right = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            light_on = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            left = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            right = True

            # если отпущена клавиша - меняем переменную
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            left = False
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            right = False
        if event.type == pygame.KEYUP and event.key == pygame.K_f:
            light_on = False
        screen.fill(pygame.color.Color('Gray'))
        seep = pygame.surface.Surface((1280, 720))
        seep.fill(pygame.color.Color('Gray'))
        player.update(left, right)
        player.draw(screen)
        if light_on:
            seep.blit(light, (player.rect.x, player.rect.y + 20))
        screen.blit(seep, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
