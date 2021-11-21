import sys
sys.path.append('C:\\temp\py\\rep2\\kbrezhnev\\capitalize')

from capitalize import capit


if capit('hello') != 'Hello':
    raise Exception('Функция работает неверно!')
elif capit('') != '':
    raise Exception('Функция работает неверно с пустой строкой!')
else:
    print('Тесты пройдены!')