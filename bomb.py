import pygame
from loadimg import load_image
from main import all_sprites


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, image, defimage):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        self.image = load_image(defimage)
        self.image_boom = load_image(image)
        super().__init__(all_sprites)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    #обновление всех спрайиов
    def update(self, *args):
        global map
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos) and\
                map[(args[0].pos[1] - 150 - args[0].pos[1] // 90 * 3) // 90][
            (args[0].pos[0] - 10 - args[0].pos[0] // 90 * 3) // 90][1] != 2:
            # print(args[0])
            i = (args[0].pos[0] - 10 - args[0].pos[0] // 90 * 3) // 90
            j = (args[0].pos[1] - 150 - args[0].pos[1] // 90 * 3) // 90
            # print(i, j)
            # print(map)

            map[j][i][1] = 1
            self.image = pygame.transform.scale(self.image_boom, (90, 90))
