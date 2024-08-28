import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG = 52, 78, 91

font = pygame.font.SysFont('arialblack', 30)
TEXT_COL = 255, 255, 255


def draw_text(text, font, text_col, x, y, surface) -> None:
    img = font.render(text, True, text_col)
    surface.blit(img, (x, y))


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Главное меню')
resume_img = pygame.image.load('buttons/button_resume.png').convert_alpha()
options_img = pygame.image.load('buttons/button_options.png').convert_alpha()
quit_img = pygame.image.load('buttons/button_quit.png').convert_alpha()
video_img = pygame.image.load('buttons/button_video.png').convert_alpha()
audio_img = pygame.image.load('buttons/button_audio.png').convert_alpha()
keys_img = pygame.image.load('buttons/button_keys.png').convert_alpha()
back_img = pygame.image.load('buttons/button_back.png').convert_alpha()

resume_button = Button(304, 125, resume_img, 1)
options_button = Button(297, 250, options_img, 1)
quit_button = Button(336, 375, quit_img, 1)
video_button = Button(226, 75, video_img, 1)
audio_button = Button(225, 200, audio_img, 1)
keys_button = Button(246, 325, keys_img, 1)
back_button = Button(332, 450, back_img, 1)

screen.fill(BG)
menu_state = 'main'
game_pause = False
run = True
while run:
    screen.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_pause = not game_pause

    if game_pause:
        if menu_state == 'main':
            if resume_button.draw(screen):
                game_pause = False
            elif options_button.draw(screen):
                menu_state = 'options'
            elif quit_button.draw(screen):
                run = False
        elif menu_state == 'options':
            if video_button.draw(screen):
                print('Vidio options')
            elif audio_button.draw(screen):
                print('audio options')
            elif keys_button.draw(screen):
                print('Keys options')
            elif back_button.draw(screen):
                menu_state = 'main'

    else:
        draw_text("Нажмите пробел для паузы", font, TEXT_COL, 160, 250, screen)

    pygame.display.update()

pygame.quit()
