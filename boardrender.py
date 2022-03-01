#create board
from bomb import Bomb

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

    #rendering
    def render(self, sc, map):
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
