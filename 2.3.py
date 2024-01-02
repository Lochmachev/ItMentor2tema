# Написать программу для нахождения среднего арифметического списка чисел.
# Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка),
# программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.
# Информация об ошибках должна быть записана в лог.

import logging
import statistics

logging.basicConfig(level=logging.INFO,
                    filename='my_logging.log',
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    encoding = 'utf-8',
                    filemode='w')
def sr_ar ():
    try:
        a = list(map(int,input('Введите числа : ').split()))
        print('Средее арифметическое списка - ', statistics.mean(a))

    except ValueError:
        logging.info('Неверные данные.')
        print('Неверные данные, попробуйте ещё раз : ')
        sr_ar()
sr_ar()