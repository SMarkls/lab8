from prettytable import PrettyTable
from datetime import datetime
import sorts
import random as rd

N = 32000  # длина последовательности
sortedList = [x for x in range(2000, 2000 + N)] # ограничение в 2000 выбрано просто так. можно изменить
randList = [x * 0 + rd.randint(2000, 2000 + N) for x in range(N)]
reversedList = sortedList[:]
reversedList.reverse()

sortedListDefault = sortedList.copy() # создание копий изначальных массивов.
randListDefault = randList.copy()
reversedListDefault = reversedList.copy()


def Check(A): # функция, проверяющая отсортирован ли массив
    B = A.copy()
    B.sort()
    return A == B


mytable = PrettyTable()
mytable.field_names = ['Метод', 'Отсортированная', 'Случайная', 'Отсортированная в обратном порядке']


Time1 = datetime.now()
lists = sorts.bubble(sortedList)
Time1 = datetime.now() - Time1
if not Check(lists):
    Time1 = 'ОШИБКА'
Time2 = datetime.now()
lists = sorts.bubble(randList)
Time2 = datetime.now() - Time2
if not Check(lists):
    Time2 = 'ОШИБКА'
Time3 = datetime.now()
lists = sorts.bubble(reversedList)
Time3 = datetime.now() - Time3
if not Check(lists):
    Time3 = 'ОШИБКА'
mytable.add_row(['Пузырьком', Time1.total_seconds(), Time2.total_seconds(), Time3.total_seconds()])

sortedList = sortedListDefault.copy()
randList = randListDefault.copy()
reversedList = reversedListDefault.copy()

Time1 = datetime.now()
lists = sorts.insertion(sortedList)
Time1 = datetime.now() - Time1
if not Check(lists):
    Time1 = 'ОШИБКА'
Time2 = datetime.now()
lists = sorts.insertion(randList)
Time2 = datetime.now() - Time2
if not Check(lists):
    Time2 = 'ОШИБКА'
Time3 = datetime.now()
lists = sorts.insertion(reversedList)
Time3 = datetime.now() - Time3
if not Check(lists):
    Time3 = 'ОШИБКА'
mytable.add_row(['Простымми Вставками', Time1.total_seconds(), Time2.total_seconds(), Time3.total_seconds()])

sortedList = sortedListDefault.copy()
randList = randListDefault.copy()
reversedList = reversedListDefault.copy()

Time1 = datetime.now()
lists = sorts.quicksort(sortedList)
Time1 = datetime.now() - Time1
if not Check(lists):
    Time1 = 'ОШИБКА'
Time2 = datetime.now()
lists = sorts.quicksort(randList)
Time2 = datetime.now() - Time2
if not Check(lists):
    Time2 = 'ОШИБКА'
Time3 = datetime.now()
lists = sorts.quicksort(reversedList)
Time3 = datetime.now() - Time3
if not Check(lists):
    Time3 = 'ОШИБКА'
mytable.add_row(['Быстрая сортировка', Time1.total_seconds(), Time2.total_seconds(), Time3.total_seconds()])

sortedList = sortedListDefault.copy()
randList = randListDefault.copy()
reversedList = reversedListDefault.copy()

Time1 = datetime.now()
sortedList.sort()
Time1 = datetime.now() - Time1
lists = sortedList[:]
if not Check(lists):
    Time1 = 'ОШИБКА'
Time2 = datetime.now()
randList.sort()
Time2 = datetime.now() - Time2
lists = randList[:]
if not Check(lists):
    Time2 = 'ОШИБКА'
Time3 = datetime.now()
reversedList.sort()
Time3 = datetime.now() - Time3
lists = reversedList[:]
if not Check(lists):
    Time3 = 'ОШИБКА'
mytable.add_row(['Встроенная сортировка', Time1.total_seconds(), Time2.total_seconds(), Time3.total_seconds()])


f = open('output.txt', 'w')
f.write(str(mytable))
