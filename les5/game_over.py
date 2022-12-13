import pygame
import os
import sys

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Picture(pygame.sprite.Sprite):
    def __init__(self, *groop):
        super().__init__(*groop)
        self.image = load_image('game_over.png')
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self, x, y):
        global now
        if x <= 0:
            self.rect.x = x
            self.rect.y = y


def main():
    pygame.init()
    size = 600, 300
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    FPS = 60
    heroes = pygame.sprite.Group()
    pic = Picture(heroes)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pic.update(pic.rect.x + 3.3, pic.rect.y)
        screen.fill((50, 2, 0))
        heroes.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
