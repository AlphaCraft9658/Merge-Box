from buttons import *
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Merge-Box")
icon = pygame.image.load("img/icon.png")
button1 = Button(screen, (0, 0, 100, 50))
button1.rect.center = (screen.get_width() / 2, screen.get_height() / 2)


def reset_window():
    screen.fill((0, 0, 0))


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        reset_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            button_check(event)

        render_buttons()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
