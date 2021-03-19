import os
try:
    os.system("pip install pygame")
    import pygame
except:
    print("Error with importing/installing required libraries. Try to install pygame manually.")
else:
    print("All libraries successfully imported/installed!")

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Pygame Button Test")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)
click = pygame.mixer.Sound("aud/sounds/plastic click.wav")
buttons = []


# define class for clickable buttons
class Button:
    def __init__(self, x, y, w, h, border_width=5, border_radius=5, color=(255, 255, 255), border_color=(200, 200, 200), click_color=(225, 225, 225), click_border_color=(175, 175, 175), text="", text_color=(0, 0, 0), text_size=24):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.border_width = border_width
        self.border_radius = border_radius
        self.color = color
        self.border_color = border_color
        self.click_color = click_color
        self.click_border_color = click_border_color
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        buttons.append(self)

    def render(self):
        if not self.clicked:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
            pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.w, self.h), self.border_radius)
        else:
            pygame.draw.rect(screen, self.click_color, (self.x, self.y, self.w, self.h))
            pygame.draw.rect(screen, self.click_border_color, (self.x, self.y, self.w, self.h), self.border_radius)


def button_click_check(ev): # pass event of the event checking loop to funcion and put function into event loop
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


button = Button(500, 250, 100, 50)
button2 = Button(350, 250, 100, 50)
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
