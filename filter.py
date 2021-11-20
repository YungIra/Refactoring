from PIL import Image
import numpy as np
from itertools import product


def get_middle(i, j):
    """Возвращает среднее значение для пикселя(i, j) размера sizeX,sizeY

       :param i: номер строки
       :type i: int
       :param j: номер столбца
       :type j: int

       :rtype: float
       :return: среднее значение
       >>>:get_middle(14,5)
       19.0
       >>>:get_middle(100,209)
       182.0
       >>>:get_middle(5,70)
       20.0
       """
    s = 0
    for n, n1 in product(range(i, i + sizeX), range(j, j + sizeY)):
        for a in range(0, len(matrix[int(n)][int(n1)])):
            if n >= x or n1 >= y:
                break
            s += int(matrix[int(n)][int(n1)][a])
    return int(s // (sizeX * sizeY)) / 3


def get_color(i, j):
    """Заполняет матричное представление изображения размера sizeX,sizeY числовыми значениями цветов
    с градацией серого gradation для соседей пикселя

        :param i: номер строки
        :type i: int
        :param j: номер столбца
        :type j: int
        """
    s = get_middle(i, j)
    step = 255 / gradation
    for n, n1 in product(range(i, i + sizeX), range(j, j + sizeY)):
        for a in range(0, 3):
            if n >= x or n1 >= y:
                break
            matrix[n, n1][a] = int(s // step) * step


def get_mosaic():
    """Заполняет матричное представление изображения размера sizeX,sizeY числовыми значениями цветов
    с градацией серого gradation

        :param i: номер строки
        :type i: int
        :param j: номер столбца
        :type j: int
        """
    [[get_color(i, j) for j in range(0, y, sizeY)] for i in range(0, x, sizeX)]
    res = Image.fromarray(matrix)
    res.save(newImg)


print('Введите имя исходного изображения')
img = Image.open(input())
matrix = np.array(img)
x = len(matrix)
y = len(matrix[1])
print('Введите имя нового изображения')
newImg = input()
print('Введите высоту мозайки')
sizeX = int(input())
print('Введите ширину мозайки')
sizeY = int(input())
print('Введите количество градаций серого')
gradation = int(input())
get_mosaic()
