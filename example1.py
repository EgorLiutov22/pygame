import pygame
import math

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)
pygame.display.set_caption("Движение машины")
road_image = pygame.image.load('road_texture.png')
background = pygame.transform.smoothscale(road_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
window.blit(background, (0, 0))
car_image = pygame.image.load('car_128.png').convert_alpha()


class CarSprite(pygame.sprite.Sprite):
    def __init__(self, car_image, x, y, rotations=360):
        pygame.sprite.Sprite.__init__(self)
        self.rot_img = []
        self.min_angle = (360 / rotations)
        for i in range(rotations):
            rotated_image = pygame.transform.rotozoom(car_image, 360 - 90 - (i * self.min_angle), 1)
            self.rot_img.append(rotated_image)
        self.min_angle = math.radians(self.min_angle)
        self.image = self.rot_img[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.reversing = False
        self.heading = 0
        self.speed = 0
        self.velocity = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(x, y)

    def accelerate(self, amount):
        if not self.reversing:
            self.speed += amount
        else:
            self.speed -= amount

    def brake(self):
        self.speed /= 2
        if abs(self.speed) < 0.1:
            self.speed = 0

    def reverse(self):
        self.speed = 0
        self.reversing = not self.reversing

    def turn(self, angle_degrees):
        self.heading += math.radians(angle_degrees)
        image_index = int(self.heading / self.min_angle) % len(self.rot_img)
        if self.image != self.rot_img[image_index]:
            x, y = self.rect.center
            self.image = self.rot_img[image_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    def update(self):
        self.velocity.from_polar((self.speed, math.degrees(self.heading)))
        self.position += self.velocity
        self.rect.center = (round(self.position[0]), round(self.position[1]))


black_car = CarSprite(car_image, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
car_sprites = pygame.sprite.Group()
car_sprites.add(black_car)


clock = pygame.time.Clock()
done = False
while not done:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True
       elif event.type == pygame.VIDEORESIZE:
           WINDOW_WIDTH = event.w
           WINDOW_HEIGHT = event.h
           window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)
           background = pygame.transform.smoothscale(road_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
       elif event.type == pygame.KEYUP:
           if event.key == pygame.K_h:
               print('meep-meep')
           elif event.key == pygame.K_r:
               print('resersing')
               black_car.reverse()
           elif event.key == pygame.K_UP:
               print('accelerate')
               black_car.accelerate(0.5)
           elif event.key == pygame.K_DOWN:
               print('brake')
               black_car.brake()

   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT]:
       black_car.turn(-1.8)
   if keys[pygame.K_RIGHT]:
       black_car.turn(1.8)

   car_sprites.update()
   window.blit(background, (0, 0))
   car_sprites.draw(window)
   pygame.display.flip()
   clock.tick_busy_loop(60)

pygame.quit()
