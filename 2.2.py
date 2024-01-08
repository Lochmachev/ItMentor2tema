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
    logging.info(f'Введены числа a: {a} ; b: {b}')
    if a < 0 or a > b or b > 100:
        raise Exception ('Диапазон чисел от 0 до 100 !!!')

    else:
        x = random.randint(a, b)
        print('Случайное число : ', x)
        logging.info(f'Выведено случайное число - {x}')

try:
    generator()
except Exception:
    logging.warning('Диапазон чисел от 0 до 100 !!!')
    print('Попробуйте ещё раз')
