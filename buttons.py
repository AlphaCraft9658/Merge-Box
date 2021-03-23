import os
try:
    os.system("python -m pip install pygame")
    import pygame
except:
    print("Error with importing/installing required libraries. Try to install pygame manually.")
else:
    try:
        os.system("python -m pip install colorama")
        import colorama
        from colorama import Fore, Back, Style
    except:
        print("Error with importing/installing required libraries. Try to install colorama manually.")
    else:
        print("All libraries imported/installed successfully!")

pygame.init()
if __name__ == "__main__":
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption("Pygame Button Test")
    icon = pygame.image.load("img/icon.png")
    pygame.display.set_icon(icon)
click = pygame.mixer.Sound("aud/sounds/plastic click.wav")
buttons = []


# define class for clickable buttons
class Button:
    # don't forget to import pygame to use this system yourself
    # pass arguments this way: ((button x, button y, button width, height), (border width, radius), ((button r, g, b),/
    # (button hover r, g, b), (button click r, g, b), (border r, g, b), (border hover r, g, b), (border click r, g, b))/
    # (text, (text r, g, b), size, font), event
    # pass a separate declared function or a lambda for "event" to make it work the way you want
    def __init__(self, screen, box: tuple[int, int, int, int] = (0, 0, 100, 50), border: tuple = (5, 5),
                 colors: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]] =
                 ((225, 225, 225), (200, 200, 200),
                 (180, 180, 180), (180, 180, 180),
                 (170, 170, 170), (130, 130, 130)),
                 text: tuple[str, tuple[int, int, int], int, str] = ("", (0, 0, 0), 0, ""), click_event=(lambda: print("Button Pressed"))):
        self.screen = screen
        self.x = box[0]
        self.y = box[1]
        self.w = box[2]
        self.h = box[3]
        self.border_width = border[0]
        self.border_radius = border[1]
        self.color = colors[0]
        self.hover_color = colors[1]
        self.click_color = colors[2]
        self.border_color = colors[3]
        self.border_hover_color = colors[4]
        self.border_click_color = colors[5]
        self.text = text[0]
        self.text_color = text[1]
        self.text_size = text[2]
        self.text_font = text[3]
        self.clicked = False
        self.hover = False
        self.click_event = click_event
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        buttons.append(self)

    def render(self):
        if self.clicked:
            pygame.draw.rect(self.screen, self.click_color, (self.x, self.y, self.w, self.h))
            pygame.draw.rect(self.screen, self.border_click_color, (self.x, self.y, self.w, self.h), self.border_radius)
        elif self.hover:
            pygame.draw.rect(self.screen, self.hover_color, self.rect)
            pygame.draw.rect(self.screen, self.border_hover_color, self.rect, self.border_radius)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)
            pygame.draw.rect(self.screen, self.border_color, self.rect, self.border_radius)
        font = pygame.font.SysFont(self.text_font, self.text_size)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        self.screen.blit(text, text_rect)


def button_check(ev):  # pass event of the event checking loop to function and put function into event loop
    for b in buttons:
        if b.rect.collidepoint(pygame.mouse.get_pos()):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                b.clicked = True
                click.play()
                b.click_event()
            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                b.clicked = False
        else:
            b.clicked = False
        if b.rect.collidepoint(pygame.mouse.get_pos()):
            b.hover = True
        else:
            b.hover = False


def render_buttons():  # use somewhere after screen reset and before screen update
    for b in buttons:
        b.render()


if __name__ == "__main__":
    button = Button((500, 250, 200, 100), text=("Test", (0, 0, 0), 70, "Sans-Serif"))
    button2 = Button((350, 250, 100, 50), text=("Test123", (0, 0, 0), 36, "Sans-Serif"), click_event=(lambda: print("Test123")))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            button_check(event)

        screen.fill((0, 0, 0))
        render_buttons()
        pygame.display.update()
        pygame.time.Clock().tick(60)
    pygame.quit()
