import pygame
import sys
import os

import random

m = []
for i in range(1, 19):
    m.append(i)
    m.append(i)
#random.shuffle(m)
print(m)

map = {}
for i in range(len(m)):
    map[m[i]] = 0
map = {}

pygame.init()
size = width, height = 720, 720
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname).convert_alpha()
    image = pygame.transform.scale(image, (75, 75))
    return image


all_sprites = pygame.sprite.Group()

# создадим спрайт
sprite = pygame.sprite.Sprite()
# определим его вид
sprite.image = load_image("bomb.png")
# и размеры
sprite.rect = sprite.image.get_rect()


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        self.image = load_image("bomb.png")
        self.image_boom = load_image(image)
        super().__init__(all_sprites)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 5
        self.top = 5
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, top, left, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, sc):
        left = self.left
        top = self.top
        cell_size = self.cell_size
        for i in range(self.width):
            for j in range(self.height):
                print(str(m[i * 5 + j]))
                Bomb(top, left, "pic" + str(m[i * 5 + j+1]) + ".jpg")
                left += cell_size - 1
            top += cell_size - 1
            left = self.left

    def ret(self):
        return [self.top, self.left, self.cell_size]


if __name__ == '__main__':
    running = True
    # поле 5 на 7
    board = Board(6, 6)
    board.set_view(60, 100, 75)
    running = True
    board.render(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        all_sprites.update(event)
        all_sprites.draw(screen)
        pygame.display.update()
