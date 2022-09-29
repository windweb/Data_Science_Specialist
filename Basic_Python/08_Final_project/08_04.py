"""
Сегментация пользователей
В предыдущем уроке вы выяснили, что пользователи разделены на три сегмента:
Segment 0, Segment 1 и Segment 2.
Больше всего строк — в Segment 0,
меньше всего — в Segment 2.
Но как понять, что объединяет пользователей каждого сегмента?
"""

"""
А какие ещё столбцы есть в этом датасете?

Вот полный список:
customer_id — уникальные идентификаторы клиентов;
interval — период: 'До внедрения роботов' или 'После внедрения роботов';
score — оценка пользователя после обращения в службу поддержки;
duration — продолжительность общения с поддержкой;
promo — получил ли пользователь промокод: 1 — да, 0 — нет;
robocats — количество робокотов у пользователя на момент обращения.
"""
"""
Гипотеза что сегменты коррелируются со столбцом robocats.

Как проверить гипотезу «пользователи разделены на сегменты по количеству купленных робокотов»? 
Что может исказить подсчёты?
Чтобы проверить гипотезу «пользователи разделены на сегменты по количеству робокотов из столбца robocats», 
можно посчитать среднее количество робокотов для каждого сегмента. 
Проблема здесь состоит в том, что один и тот же клиент может обращаться в поддержку множество раз и 
в перерыве между обращениями покупать робокотов. 
При этом отследить наиболее актуальное обращение не получится — 
в таблице нет точного времени для каждого обращения, только 'До внедрения роботов' и 'После внедрения роботов'. 
Тем не менее для ваших целей — выявить разницу в количестве робокотов между сегментами — точные значения и не нужны. 
Достаточно усреднить количество робокотов по всем обращениям внутри каждого сегмента.
"""

"""
Задание 1
Посчитайте общее количество робокотов в каждом сегменте и 
выведите полученные значения на экран на разных строках по порядку: 
нулевой сегмент, первый, второй.
"""
import pandas

data = pandas.read_csv('support_data.csv')

segment = list(data['segment'])
robocats = list(data['robocats'])  # преобразуйте столбец 'robocats' в список

cats = 0
# перебор индексов строк таблицы
for index in range(len(data)):
    if segment[index] == 'Segment 0':
        cats += robocats[index]
print(cats)

cats = 0
# вычисление для Segment 1
for index in range(len(data)):
    if segment[index] == 'Segment 1':
        cats += robocats[index]
print(cats)


cats = 0
# вычисление для Segment 2
for index in range(len(data)):
    if segment[index] == 'Segment 2':
        cats += robocats[index]
print(cats)


"""
Результат
0
2468
3964

Даже общее количество робокотов по сегментам уже кое о чём говорит! 
Пользователи нулевого сегмента пока не стали счастливыми обладателями робокота, 
в то время как во втором сегменте робокотов больше всего.
"""

"""
Задание 2
Чтобы найти средние показатели, в каждом сегменте разделите количество робокотов на количество обращений. 
Выведите полученные значения на экран на отдельных строках в обычном порядке: 
нулевой, первый, второй.
"""

cats = 0  # переменная для накопления количества робокотов
counter = 0  # переменная-счётчик для количества записей с Segment 0
# ваш код для Segment 0
for index in range(len(data)):
    if segment[index] == 'Segment 0':
        cats += robocats[index]
        counter += 1
print(cats / counter)


cats = 0
counter = 0
# ваш код для Segment 1
for index in range(len(data)):
    if segment[index] == 'Segment 1':
        cats += robocats[index]
        counter += 1
print(cats / counter)

cats = 0
counter = 0
# ваш код для Segment 2

for index in range(len(data)):
    if segment[index] == 'Segment 2':
        cats += robocats[index]
        counter += 1
print(cats / counter)

"""
Результат
0.0
1.0
9.93483709273183

Почти десять робокотов на клиента в последнем сегменте! Кто-то очень любит котиков.
"""
"""
Полученные значения лучше визуализировать — например на столбчатой диаграмме.
"""
"""
Задание 3
Соберите среднее количество робокотов по каждому сегменту из предыдущей задачи в один список. 
В другом списке перечислите названия сегментов через запятую: 
'Segment 0', 'Segment 1', 'Segment 2'. 
Затем импортируйте seaborn и вызовите функцию barplot(), 
передав ей список со средними показателями как x и список с названиями сегментов как y.
"""

import pandas
import seaborn

data = pandas.read_csv('support_data.csv')

segment = list(data['segment'])
robocats = list(data['robocats'])

# ваш код здесь
spisok = []
other_spisok = ['Segment 0', 'Segment 1', 'Segment 2']

cats = 0
counter = 0
for index in range(len(data)):
    if segment[index] == 'Segment 0':
        cats += robocats[index]
        counter += 1
spisok.append(cats / counter)

cats = 0
counter = 0
# ваш код для Segment 1
for index in range(len(data)):
    if segment[index] == 'Segment 1':
        cats += robocats[index]
        counter += 1
spisok.append(cats / counter)

cats = 0
counter = 0
# ваш код для Segment 2

for index in range(len(data)):
    if segment[index] == 'Segment 2':
        cats += robocats[index]
        counter += 1
spisok.append(cats / counter)

seaborn.barplot(x=spisok, y=other_spisok)

"""
Похоже, гипотеза подтвердилась: 
пользователи действительно разделены на сегменты по количеству купленных ими робокотов. 
Пользователи нулевого сегмента пока не приобрели ни одного робокота, 
первого — наслаждаются обществом одного робокота, 
второго — завели уже порядка десяти робокотов. 

Осталось дать им «говорящие» названия:

Обычные клиенты     VIP-клиенты     Потенциальные клиенты
Segment 1           Segment 2       Segment 0

"""

"""
Оптимизация кода
В этом и предыдущем уроках вы создали несколько фильтров: 
два по столбцу interval и три по столбцу segment. 
Это можно было сделать разными способами — написав по циклу для каждого сегмента или применив конструкцию if-elif. 
Если вы предпочли первый вариант, то могли заметить, что код в основном повторяет сам себя:
"""

import pandas
import seaborn

data = pandas.read_csv('support_data.csv')

segment = list(data['segment'])
robocats = list(data['robocats'])

means = []  # пустой список для сбора средних показателей

# считаем среднее для нулевого сегмента:
cats = 0  # общее число робокотов
counter = 0  # количество обращений
for index in range(len(data)):
    if segment[index] == 'Segment 0':
        cats +=robocats[index]
        counter += 1
means.append(cats / counter) # добавляем среднее в means

# то же самое для первого сегмента:
cats = 0
counter = 0
for index in range(len(data)):
    if segment[index] == 'Segment 1':
        cats += robocats[index]
        counter += 1
means.append(cats / counter)

# и для второго:
cats = 0
counter = 0
for index in range(len(data)):
    if segment[index] == 'Segment 2':
        cats += robocats[index]
        counter += 1
means.append(cats / counter)

names = ['Segment 0', 'Segment 1', 'Segment 2']
seaborn.barplot(x=means, y=names)

"""
В таком случае удобнее написать вложенный цикл, с которым вы впервые познакомились в предыдущей теме. 
Вот как это может выглядеть:
"""

import pandas
import seaborn

data = pandas.read_csv('support_data.csv')

segment = list(data['segment'])
robocats = list(data['robocats'])

# список сегментов, чтобы цикл мог пройти по ним
names = ['Segment 0', 'Segment 1', 'Segment 2']

# список, в который будем складывать средние значения
means = []

# внешний цикл по названиям сегментов
for name in names:
    # код внутри - почти то же, что было раньше
    cats = 0
    counter = 0
    # внутренний цикл
    for index in range(len(data)):
        # в этой строке заменили название сегмента на переменную цикла
        if segment[index] == name:
            cats += robocats[index]
            counter += 1
    means.append(cats / counter)

# код достаточно написать один раз
# цикл повторит его столько раз, сколько нужно

seaborn.barplot(x=means, y=names)