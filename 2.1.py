# Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0.
# Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю
# попробовать еще раз с другими коэффициентами. При выполнении скрипта в лог должна записываться
# информация о успехе или неудаче операции.

import math
import logging

logging.basicConfig(level=logging.INFO,
                    filename='my_logging.log',
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    encoding = 'utf-8',
                    filemode='w')
def kvyr():
    try:
        a = int(input("Введите значение a= "))
        b = int(input("Введите значение b= "))
        c = int(input("Введите значение c= "))
        D = b ** 2 - 4 * a * c
        print('Дискриминанта равна : ',D)
        if D == 0:
            x1 = -b / (2 * a)
            print('Уровнение имеет один корень. ')
            logging.info('Найден один корень. ')
        else:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            print('Первый корень = ',x1)
            print('Второй корень = ',x2)
            logging.info('Корни найдены')

    except (ValueError ,ZeroDivisionError):
        logging.warning('Уравнение не имеет корней. ')
        print('Ошибка ! Попробуйте с другими коэффициентами.')
        #kvyr()
kvyr()

# kvyr - kvadratnoe yravnenie
