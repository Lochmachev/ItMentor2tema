# Написать программу для генерации случайных чисел в заданном диапазоне.
# Если пользователь ввел недопустимые границы диапазона (например, меньше нуля),
# программа должна вывести ошибку и попросить ввести диапазон заново.
# Информация об ошибках должна быть записана в лог.

import random
import logging

logging.basicConfig(level=logging.INFO,
                    filename='my_logging.log',
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    encoding = 'utf-8',
                    filemode='w')

def generator():
    a = int(input('Введите нижнею границу диапазона : '))
    b = int(input('Введите верхнею границу диапазона : '))
    try:
        if a >= 0 and a < b and b <= 100:
            x = random.randint (a, b)
            print('Случайное число : ',x)
        else:
            raise ValueError ('Диапазон чисел от 0 до 100 !!!')

    except Exception:

        logging.info('Диапазон чисел от 0 до 100 !!!')

        print('Неверные данные...')
        generator()
generator(),
