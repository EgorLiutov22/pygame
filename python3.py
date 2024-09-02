import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

display_screen = pygame.display.set_mode((500, 500))

base_font = pygame.font.Font(None, 40)

user_text = ''

input_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color("lightskyblue")
color_passive = pygame.Color("gray15")
color = color_passive

active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[0:-1]
            else:
                user_text += event.unicode

    display_screen.fill((0, 0, 0))

    if active:
        color = color_active
    else:
        color = color_passive

    pygame.draw.rect(display_screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    display_screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)
    pygame.display.flip()
    clock.tick(60)
