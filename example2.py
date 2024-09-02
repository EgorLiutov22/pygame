import pygame
import time

pygame.init()
display_surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Text')

font = pygame.font.SysFont(None, 40)
text = 'PyGame!'
img = font.render(text, True, (255, 0, 0))
rect = img.get_rect()
rect.topleft = (20, 20)
cursor = pygame.Rect(rect.topright, (3, rect.height))


while True:
    # display_surface.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(text) > 0:
                    text = text[:-1]
            else:
                text += event.unicode

            img = font.render(text, True, (255, 0, 0))
            rect.size = img.get_size()
            cursor.topleft = rect.topright
            if time.time() % 1 > 0.5:
                pygame.draw.rect(display_surface, (255, 0, 0), cursor)

    display_surface.blit(img, rect)

    pygame.display.update()

# pygame.quit()
