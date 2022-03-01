# добовляем нужные бтблиотеки
from pprint import pprint
import pygame
import sys
import os
import time
import random
import sqlite3

from loadimg import load_image

# проверка на победу
# true and flase выиграл  и проиграл соответсвенно
from all_checkers import winchecker

absoluterecord = 1000000000000
absolute = "record"

# созаем базу данных если ее нет
db = sqlite3.connect("server.db")
sql = db.cursor()
sql.execute("""CREATE
                TABLE 
                IF NOT EXISTS
                users (
                name TEXT,
                record BIGINT)""")

db.commit()
sql.execute("SELECT name from users")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO "
                f"users "
                f"VALUES(?, ?)"
                , (absolute,
                   absoluterecord))
    db.commit()
else:
    pass

FPS = 50
# счет в игре
r = 0

# arial
font_name = pygame.font.match_font('arial')


# счет в игре
def draw_text(surf,
              text,
              size,
              x,
              y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text,
                               False,
                               pygame.Color("BLACK"))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,
                        y)
    surf.blit(text_surface,
              text_rect)


# доп выход из игры
def terminate():
    pygame.quit()
    sys.exit()


# рекорд
maxscore = sql.execute("""SELECT record
                        FROM users
                         WHERE name 
                         LIKE 'record' """).fetchall()
maxscore = maxscore[0][0]
print(maxscore)


# конечный экран
def end():
    global r
    a = random.randint(0,
                       1)
    if a == 0:
        a = ""
    else:
        a = "1"
    if r < maxscore:
        fon = pygame.transform.scale \
            (load_image('endwinpic' + \
                        a + '.jpg'),
             (575,
              720))
        intro_text = ["Вы побили рекорд!",
                      "Мои поздравления",
                      "ваш новыый рекорд:" + str(r)]
        sql.execute("""UPDATE users
                                    SET record = ?
                                    WHERE name LIKE 'record'
                                    """, (r,)).fetchall()
        db.commit()

    else:
        fon = pygame.transform.scale(load_image('endlosepic' + \
                                                a + '.jpg'), (575, 720))
        intro_text = ["Вы не побили рекорда!",
                      "Очень жаль",
                      "ваш счет:"
                      " " + str(r),
                      "ваш рекорд: "
                      "" + str(maxscore)]

    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 100
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    intro_text = "сыграть еще раз"

    font = pygame.font.Font(None, 30)
    text_coord = 630
    string_rendered = font.render(intro_text, 2, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 360
    screen.blit(string_rendered, intro_rect)

    intro_text = "выйти"

    text_coord = 630
    string_rendered = font.render(intro_text, 2, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 150
    screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if event.pos[1] >= 592 \
                        and event.pos[0] >= 372 \
                        and event.pos[0] <= 545 \
                        and event.pos[1] <= 654:
                    global m
                    global map
                    r = -1
                    m = []
                    map = [[], [], [], [], [], []]
                    for i in range(1, 19):
                        m.append(i)
                        m.append(i)
                    random.shuffle(m)
                    c = 0
                    for i in m:
                        if len(map[c]) == 6:
                            c += 1
                        map[c].append([i, 0])
                    r = 0
                    # начинаем игру
                    return
                elif event.pos[1] >= 599 \
                        and event.pos[0] >= 44 \
                        and event.pos[0] <= 252 \
                        and event.pos[1] <= 658:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


def start_screen():
    intro_text = "играть"

    fon = pygame.transform.scale(load_image('nach.png'), (575, 720))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 630
    string_rendered = font.render(intro_text, 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 450
    screen.blit(string_rendered, intro_rect)

    intro_text = "выйти"

    text_coord = 630
    string_rendered = font.render(intro_text, 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 150
    screen.blit(string_rendered, intro_rect)

    if maxscore == 1000000000000:
        intro_text = "Рекорд: " + "неизвестен"
    else:
        intro_text = "Рекорд: " + str(maxscore)

    text_coord = 50
    string_rendered = font.render(intro_text, 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    intro_rect.x = 50
    screen.blit(string_rendered, intro_rect)

    intro_text = ["Правила игры:",
                  "Здравствуйте, уважаемый игрок,",
                  "в игре за минимальное количество попыток",
                  "нужно ракрыть все пары карточек",
                  "УДАЧНОЙ ИГРЫ!"]

    font = pygame.font.Font(None, 30)
    text_coord = 100
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if event.pos[1] >= 592 \
                        and event.pos[0] >= 372 \
                        and event.pos[0] <= 545 \
                        and event.pos[1] <= 654:
                    return  # начинаем игру
                elif event.pos[1] >= 599 \
                        and event.pos[0] >= 44 \
                        and event.pos[0] <= 252 \
                        and event.pos[1] <= 658:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


# просто чекер
def check(m):
    c = 0
    for i in m:
        for j in i:
            if j[1] == 1:
                c += 1
    if c != 2:
        return True
    else:
        return False


# проверка
# на
# similarity

def checksimilar(m):
    global r
    a = 0
    b = 0
    global map
    for i in m:
        for j in i:
            if j[1] == 1 \
                    and a == 0:
                a = j[0]
            elif j[1] == 1:
                b = j[0]
    if a == 0 or b == 0:
        return "a"
    elif a == b:
        for i in range(6):
            for j in range(6):
                if map[i][j][1] == 1:
                    map[i][j][1] = 2
        r += 1
        return "b"
    else:
        r += 1
        return "c"


z = 0

# важные переменные
# для создания
# быза данных
clock = pygame.time.Clock()
m = []
map = [[], [], [], [], [], []]

for i in range(1, 19):
    m.append(i)
    m.append(i)

random.shuffle(m)
random.shuffle(m)

c = 0

for i in m:
    if len(map[c]) == 6:
        c += 1
    map[c].append([i, 0])

# для себя
pprint(map)
pygame.init()
size = width, height = 575, 720
screen = pygame.display.set_mode(size)

# для создания surface
# ввиде картинки


all_sprites = pygame.sprite.Group()

# создадим спрайт
sprite = pygame.sprite.Sprite()

# определим его вид
sprite.image = load_image("ss.jpg")

# и размеры
sprite.rect = sprite.image.get_rect()


# основной класс
# спрайта
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

    # обновление всех спрайиов
    def update(self, *args):
        global map
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos) and \
                map[(args[0].pos[1] - 150 - args[0].pos[1] // 90 * 3) // 90][
                    (args[0].pos[0] - 10 - args[0].pos[0] // 90 * 3) // 90][1] != 2:
            # print(args[0])
            i = (args[0].pos[0] - 10 - args[0].pos[0] // 90 * 3) // 90
            j = (args[0].pos[1] - 150 - args[0].pos[1] // 90 * 3) // 90
            # print(i, j)
            # print(map)

            map[j][i][1] = 1
            self.image = pygame.transform.scale(self.image_boom, (90, 90))


# доп спрайт
class Car(pygame.sprite.Sprite):
    image = load_image("doppic.jpg")
    image = pygame.transform.scale(image, (555, 555))

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


# create board
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

    # rendering
    def render(self, sc):
        left = self.left
        top = self.top
        cell_size = self.cell_size
        for j in range(self.height):
            for i in map[j]:
                if i[1] == 2:
                    Bomb(top, left, "pic" + str(i[0]) + ".jpg",
                         "pic" + str(i[0]) +
                         ".jpg")
                else:
                    Bomb(top, left,
                         "pic" + str(i[0]) +
                         ".jpg", "ss.jpg")
                top += cell_size + 3
            left += cell_size + 3
            top = self.top

    def ret(self):
        return [self.top, self.left, self.cell_size]


a = 0

# main stuff
if __name__ == '__main__':
    running = True

    # запускаем оснву
    start_screen()

    # поле 6 на 6
    board = Board(6, 6)
    board.set_view(10, 150, 90)
    running = True
    board.render(screen)
    screen.fill((119, 221, 119))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        all_sprites.update(event)
        all_sprites.draw(screen)
        pygame.display.update()
        screen.fill((119, 221, 119))
        draw_text(screen, "Совершенно попыток: "
                  + str(r), 18, 575 / 2, 10)

        if checksimilar(map) == "c":
            pygame.time.wait(300)
            for i in range(6):
                for j in range(6):
                    if map[i][j][1] == 1:
                        map[i][j][1] = 0
            board.render(screen)

        if winchecker(map):
            end()
