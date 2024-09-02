import pygame

display_surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Text')
pygame.font.init()
font1 = pygame.font.SysFont('Tahoma', 50)
font2 = pygame.font.SysFont('Impact', 40)
text1 = font1.render('Text1', True, (0, 255, 0))
text2 = font2.render('Text2', True, (0, 255, 0))
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect1.center = (250, 250)
textRect2.center = (250, 300)


while True:
    display_surface.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    display_surface.blit(text1, textRect1)
    display_surface.blit(text2, textRect2)

    pygame.display.update()

# pygame.quit()
