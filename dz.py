import sys
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('GUI Button')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)


class Button:
    def __init__(self, text, width, height, pos, elevation):
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        self.pressed = False
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#354B5E'

    def draw(self):
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            # print('Столкновение')
            self.top_color = '#D73B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                if self.pressed:
                    self.dynamic_elevation = self.elevation
                    print('Кнопка нажата')
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'


class ExitButton(Button):
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D73B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                if self.pressed:
                    self.dynamic_elevation = self.elevation
                    print('Выход')
                    self.pressed = False
                    pygame.quit()
                    sys.exit()
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'


button1 = Button('Нажми на меня', 200, 40, (150, 250), 6)
exitbutton = ExitButton('Выход', 200, 40, (150, 350), 6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('#DCDDD8')
    button1.draw()
    exitbutton.draw()

    pygame.display.update()
    clock.tick(60)
