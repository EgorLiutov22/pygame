import sys
import random

import pygame


class ParticleStar:
    def __init__(self, obj):
        self.particles = []
        self.surface = pygame.image.load('images/star.png').convert_alpha()
        self.width = self.surface.get_rect().width
        self.height = self.surface.get_rect().height
        self.obj = obj

    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x += particle[1]
                particle[0].y += particle[2]
                particle[3] -= 0.2
                screen.blit(self.surface, particle[0])

    def add_particles(self):
        pos_x = self.obj.rect.x - self.width / 2
        pos_y = self.obj.rect.y - self.height / 2
        direction_x = random.randint(-3, 3)
        direction_y = random.randint(-3, 3)
        lifetime = random.randint(4, 10)
        particle_rect = pygame.Rect(pos_x, pos_y, self.width, self.height)
        self.particles.append([particle_rect, direction_x, direction_y, lifetime])

    def delete_particles(self):
        particles_copy = [particle for particle in self.particles if particle[3] > 0]
        self.particles = particles_copy

    def clear(self):
        self.particles = []


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 50, 100)
        self.image = pygame.image.load('images/player.png')
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


pygame.init()

screen = pygame.display.set_mode((1280, 720))

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 40)

light = pygame.image.load('images/light.png')
light = pygame.transform.scale(light, (100, 50))
player = Player(400, 400)
light_on = False
left = False
right = False

stars = ParticleStar(player)

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
            stars.clear()
        if event.type == PARTICLE_EVENT:
            stars.add_particles()
        screen.fill(pygame.color.Color('Gray'))
        seep = pygame.surface.Surface((1280, 720))
        seep.fill(pygame.color.Color('Gray'))
        player.update(left, right)
        player.draw(screen)
        # stars.emit()
        if light_on:
            seep.blit(light, (player.rect.x, player.rect.y + 20))

            stars.emit()
        screen.blit(seep, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
