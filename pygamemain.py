import random
from random import randint
import pygame as pg
import sys
import os



def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname).convert_alpha()
    image = pg.transform.scale(image, (75, 75))
    return image


W = 500
H = 500
WHITE = (255, 255, 255)
sc = pg.display.set_mode((W, H))
x, y = 0, 0

all_sprites = pg.sprite.Group()

# создадим спрайт
sprite = pg.sprite.Sprite()
# определим его вид
sprite.image = load_image("bomb.png")
# и размеры
sprite.rect = sprite.image.get_rect()


class Bomb(pg.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(all_sprites)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W - 51)
        self.rect.y = random.randrange(H - 51)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


for _ in range(20):
    Bomb(all_sprites)
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    sc.fill(WHITE)
    all_sprites.update(i)
    all_sprites.draw(sc)
    pg.display.update()
