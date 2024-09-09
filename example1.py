import random

import pygame, sys


class ParticlePrinciple:
    def __init__(self):
        self.particles = []
        self.size = 12

    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x -= 1
                pygame.draw.rect(screen, particle[1], particle[0])
            self.draw_nyancat()

    def add_particles(self, offset, color):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1] + offset
        particle_rect = pygame.Rect(pos_x - self.size / 2, pos_y - self.size / 2, self.size, self.size)
        self.particles.append((particle_rect, color))

    def delete_particles(self):
        particles_copy = [particle for particle in self.particles if particle[0].x > 0]
        self.particles = particles_copy

    def draw_nyancat(self):
        nyan_rect = nyan_surface.get_rect(center=pygame.mouse.get_pos())
        screen.blit(nyan_surface, nyan_rect)


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

nyan_surface = pygame.image.load('images/nyan_cat.png').convert_alpha()
PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 40)
# particle1 = ParticlePrinciple()
particle2 = ParticlePrinciple()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            # particle1.add_particles()
            particle2.add_particles(-30, pygame.Color('Red'))
            particle2.add_particles(-18, pygame.Color('Orange'))
            particle2.add_particles(-6, pygame.Color('Yellow'))
            particle2.add_particles(6, pygame.Color('Green'))
            particle2.add_particles(18, pygame.Color('Blue'))
            particle2.add_particles(30, pygame.Color('Purple'))

    screen.fill((30, 30, 30))
    # particle1.emit()
    particle2.emit()
    pygame.display.update()
    clock.tick(120)
