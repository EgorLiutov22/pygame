import pygame

pygame.init()

pygame.mixer.music.load('1.ogg')

W, H = 500, 300
sc = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60
pygame.mixer.music.play(-1)
flPause = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    clock.tick(FPS)