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


class Hero(pygame.sprite.Sprite):
    def __init__(self, *groop):
        super().__init__(*groop)
        self.image = load_image('cap.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y


def main():
    pygame.init()
    size = 300, 300
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    FPS = 60
    heroes = pygame.sprite.Group()
    hero = Hero(heroes)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_DOWN]:
                    hero.update(hero.rect.x, hero.rect.y + 10)
                if key[pygame.K_UP]:
                    hero.update(hero.rect.x, hero.rect.y - 10)
                if key[pygame.K_RIGHT]:
                    hero.update(hero.rect.x + 10, hero.rect.y)
                if key[pygame.K_LEFT]:
                    hero.update(hero.rect.x - 10, hero.rect.y)
        screen.fill((200, 255, 255))
        heroes.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
