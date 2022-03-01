import pygame
import os
import sys

#для создания surface
#ввиде картинки
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с"
              f" изображением '{fullname}"
              f"' не найден")
        sys.exit()
    image = pygame.image.load(fullname).convert_alpha()
    image = pygame.transform.scale(image, (90, 90))
    return image