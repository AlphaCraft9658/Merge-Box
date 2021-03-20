import os
from time import sleep
try:
    os.system("pip install pygame")
    import pygame
except:
    print("Error with importing/installing required libraries. Try to install pygame manually.")
else:
    try:
        os.system("pip install colorama")
        import colorama
        from colorama import Fore, Back, Style
    except:
        print("Error with importing/installing required libraries. Try to install colorama manually.")
    else:
        print("All libraries imported/installed successfully!")

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Pygame Button Test")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)
click = pygame.mixer.Sound("aud/sounds/plastic click.wav")
buttons = []


# define class for clickable buttons
# pass arguments this way: ((button x, button y, button width, height), (border width, radius), ((button r, g, b),/
# (button hover r, g, b), (button click r, g, b), (border r, g, b), (border hover r, g, b), (border click r, g, b))/
# (text, (text r, g, b), size, font)
class Button:
    def __init__(self, box=(0, 0, 10, 50), border=(5, 5), colors=((225, 225, 225), (200, 200, 200), (180, 180, 180), (180, 180, 180), (170, 170, 170), (130, 130, 130)), text=("", (0, 0, 0), 0, "")):
        if not (type(box) == tuple and len(box) == 4 and [True for i in box if type(i) == int]):
            if not (type(border) == tuple and len(border) == 2 and [True for i in border if type(i) == int]):
                if not (type(colors) == tuple and len(colors) == 6 and [True for i in [n for n in [v for v in colors]] if type(i) == int]):
                    if not (type(text) == tuple and type(text[0]) == str and type(text[1]) == tuple and [True for i in text[1] if type(i) == int] and type(text[2]) == int and type(text[3]) == str and (text[3] in pygame.font.get_fonts() or text[3] == "")):
                        print(f"{Fore.RED}=== invalid button construction! ===")
                        pygame.quit(); sleep(3)
                        exit()
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
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        buttons.append(self)

    def render(self):
        if not self.clicked:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
            pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.w, self.h), self.border_radius)
        else:
            pygame.draw.rect(screen, self.click_color, (self.x, self.y, self.w, self.h))
            pygame.draw.rect(screen, self.border_click_color, (self.x, self.y, self.w, self.h), self.border_radius)


def button_click_check(ev): # pass event of the event checking loop to function and put function into event loop
    for b in buttons:
        if b.rect.collidepoint(pygame.mouse.get_pos()):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                b.clicked = True
                click.play()
            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                b.clicked = False
        else:
            b.clicked = False


def render_buttons():
    for b in buttons:
        b.render()


button = Button((500, 250, 100, 50))
button2 = Button((350, 250, 100, 50))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        button_click_check(event)

    screen.fill((0, 0, 0))
    render_buttons()
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()
