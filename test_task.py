from collections import deque
from time import perf_counter
from os import system
from random import randint


def is_even(value):
    '''Не повторять дома. Опасно для ПК.
        Асимптотика O(n/2).
        Оптимальное решение это modulus остаток от деления на 2 (0 или 1)
        В Python используется snake_case, isEven нам чуждо!
    '''
    while value > 0:
        value -= 2
    return True if value == 0 else False


class CircleFIFO(object):
    def __init__(self, *args):
        '''создает локальный атрибут fifo содержащий элементы из args'''
        self.__fifo = list(*args)

    def get_item(self):
        '''Выдает первый элемент структуры данных и помещает его в конец структуры данных'''
        r = self.__fifo.pop(0)
        self.__fifo.append(r)
        return r

    def __len__(self):
        return len(self.__fifo)


class CirleFIFO2(object):
    def __init__(self, *args):
        self.__d = deque(args)

    def get_item(self):
        self.__d.rotate(-1)
        return self.__d[-1]

    def __len__(self):
        return len(self.__d)


'''Очевидно, что предпочтительней использовать второй кольцевой буффер, 
так как он использует двуконечную очередь, 
инструмент написанный на С и включенный в стандартную библиотеку. 
Все что включено в стандартную библиотеку оптимизировано и зачастую дает 
лучшие результаты.
'''
def quick_sort(lst):
    '''Быстрая сортировка использует подход разделяй и властвуй. 
    	Quicksort
        Runtime	7.03 seconds	
        Instructions	8.94 billion
        Cycles	11.2 billion
        IPC	0.8
        Сам Python использует сортировку timsort, которая комбинирует в 
        себе несколько сортировок и оптимизирована
        '''
    if len(lst) == 1 or len(lst) == 0:
       return lst
    else:
        pivot = lst[0]
        i = 0
        for j in range(len(s)-1):
            if lst[j+1] < pivot:
               lst[j+1],lst[i+1] = lst[i+1],lst[j+1]
               i += 1
        lst[0],lst[i] = lst[i],lst[0]
        first_part = quick_sort(lst[:i])
        second_part = quick_sort(lst[i+1:])
        first_part.append(lst[i])
        return first_part + second_part


if __name__ == '__main__':

    assert is_even(11) == False, '11 нечетное число'
    assert is_even(100) == True, '100 четное число'

    ring_b_data = tuple(range(1000))
    s1 = perf_counter()
    c = CircleFIFO(ring_b_data)
    for i in range(0, len(c) * 2):
        print(c.get_item())
    res1 = perf_counter() - s1

    s2 = perf_counter()
    c2 = CirleFIFO2(ring_b_data)
    for i in range(0, len(c2) * 2):
        print(c2.get_item())
    res2 = perf_counter() - s2

    system('clear')  # works on *nix systems. 'cls' on windows
    print(f'Time using list as data structure {res1}, time using deque {res2}')
