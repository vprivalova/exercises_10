import random


class NavalBattle:
    playing_field = []

    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def show():
        internal_list = []
        for elem in NavalBattle.playing_field:
            internal_list.append([])
            for i in range(len(elem)):
                if elem[i] == 0 or elem[i] == 1:
                    internal_list[-1].append('~')
                else:
                    internal_list[-1].append(elem[i])

        for elem in internal_list:
            print(''.join([str(j) for j in elem]))

    def shot(self, x, y):
        if len(NavalBattle.playing_field) == 0:
            print('игровое поле не заполнено')
        else:
            if NavalBattle.playing_field[y - 1][x - 1] == self.symbol or NavalBattle.playing_field[y - 1][x - 1] == 'o':
                print('ошибка')
            else:
                if NavalBattle.playing_field[y - 1][x - 1] == 0:
                    print('мимо')
                    NavalBattle.playing_field[y - 1][x - 1] = 'o'
                else:
                    print('попал')
                    NavalBattle.playing_field[y - 1][x - 1] = self.symbol

    @classmethod
    def new_game(cls):
        cls.playing_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        direction = ['вертикальный', 'горизонтальный']
        dir_quadro = random.choice(direction)
        if dir_quadro == 'вертикальный':
            done = False
            while done is not True:
                x_quadro = random.randint(0, 9)
                y_quadro = random.randint(0, 9)
                if (y_quadro + 1 < 9) and (y_quadro + 2 < 9) and (y_quadro + 3 <= 9):

                    cls.playing_field[y_quadro][x_quadro] = '1'
                    cls.playing_field[y_quadro + 1][x_quadro] = '1'
                    cls.playing_field[y_quadro + 2][x_quadro] = '1'
                    cls.playing_field[y_quadro + 3][x_quadro] = '1'
                    done = True
        else:
            done = False
            while done is not True:
                x_quadro = random.randint(0, 9)
                y_quadro = random.randint(0, 9)
                if (x_quadro + 1 < 9) and (x_quadro + 2 < 9) and (x_quadro + 3 <= 9) :

                    cls.playing_field[y_quadro][x_quadro] = '1'
                    cls.playing_field[y_quadro][x_quadro + 1] = '1'
                    cls.playing_field[y_quadro][x_quadro + 2] = '1'
                    cls.playing_field[y_quadro][x_quadro + 3] = '1'
                    done = True

        for _ in range(2):
            dir_triple= random.choice(direction)
            if dir_triple == 'вертикальный':
                done = False
                while done is not True:
                    x_triple = random.randint(0, 9)
                    y_triple = random.randint(0, 9)
                    if (y_triple + 1 < 9) and (y_triple + 2 <= 9) and (cls.playing_field[y_triple][x_triple] == 0) and (
                            cls.playing_field[y_triple + 1][x_triple] == 0) and (
                            cls.playing_field[y_triple + 2][x_triple] == 0):

                        cls.playing_field[y_triple][x_triple] = '1'
                        cls.playing_field[y_triple + 1][x_triple] = '1'
                        cls.playing_field[y_triple + 2][x_triple] = '1'
            else:
                done = False
                while done is not True:
                    x_triple = random.randint(0, 9)
                    y_triple = random.randint(0, 9)
                    if (x_triple + 1 < 9) and (
                            x_triple + 2 <= 9) and (cls.playing_field[y_triple][x_triple] == 0) and (
                            cls.playing_field[y_triple][x_triple + 1] == 0) and (
                            cls.playing_field[y_triple][x_triple + 2] == 0):

                        cls.playing_field[y_triple][x_triple] = '1'
                        cls.playing_field[y_triple][x_triple + 1] = '1'
                        cls.playing_field[y_triple][x_triple + 2] = '1'

            for _ in range(3):
                dir_double = random.choice(direction)
                if dir_double == 'вертикальный':
                    done = False
                    while done is not True:
                        x_double = random.randint(0, 9)
                        y_double = random.randint(0, 9)
                        if (y_double + 1 <= 9) and (cls.playing_field[y_double][x_double] == 0) and (
                                cls.playing_field[y_double + 1][x_double] == 0):
                            cls.playing_field[y_double][x_double] = '1'
                            cls.playing_field[y_double + 1][x_double] = '1'
                else:
                    done = False
                    while done is not True:
                        x_double = random.randint(0, 9)
                        y_double = random.randint(0, 9)
                        if (x_double + 1 <= 9) and (cls.playing_field[y_double][x_double] == 0) and (
                                cls.playing_field[y_double][x_double + 1] == 0):
                            cls.playing_field[y_double][x_double] = '1'
                            cls.playing_field[y_double][x_double + 1] = '1'

            for _ in range(4):
                done = False
                while done is not True:
                    x_single = random.randint(0, 9)
                    y_single = random.randint(0, 9)
                    if cls.playing_field[y_single][x_single] == 0:
                        cls.playing_field[y_single][x_single] = '1'


player1 = NavalBattle('#')
player1.shot(6, 2)
NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1, 1)
player1.shot(1, 1)
NavalBattle.new_game()
NavalBattle.show()
