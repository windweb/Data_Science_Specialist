"""
Ошибки предсказаний

Чтобы оценить, насколько успешны две стратегии,
осталось сравнить предсказанные в соответствии с ними объёмы урожая за каждый год и реальные исторические данные.
Проще всего это сделать, вычтя предсказания из правильных ответов.
Тогда победит та стратегия, где разница окажется меньше.
"""
print('     Task_1')
"""
1.
Вычислите ошибки предсказаний для первой стратегии — площадь посевов реальная, а урожайность прошлогодняя.

Создайте список error_acres и добавьте в него разницу реального и 
предсказанного объёма урожая за каждый год, кроме 1980-го. 
Чтобы не запутаться с индексами, не создавайте отдельный список для предсказаний, как в предыдущем уроке. 
Вместо этого сразу вычитайте произведение реальной площади посевов и 
прошлогодней урожайности из реального объёма урожая за определённый год.

Затем постройте столбчатую диаграмму, на которой 
по оси X отмечены года, начиная с 1981-го, а по оси Y — значения error_acres.

"""
import pandas

data = pandas.read_csv('crops_usa.csv')

acres = list(data['Acres'])
production = list(data['Production'])
years = list(data['Year'])

acres_usa = []
production_usa = []

for year in range(1980, 2020):
    acres_one_year = []
    production_one_year = []
    for index in range(len(data)):
        if years[index] == year:
            acres_one_year.append(acres[index])
            production_one_year.append(production[index])
    acres_usa.append(sum(acres_one_year))
    production_usa.append(sum(production_one_year))

yield_usa = []

for index in range(len(production_usa)):
    yield_usa.append(production_usa[index] / acres_usa[index])
years_numbers = list(range(1980, 2020))

# ваш код здесь
error_acres = []
for index in range(1, len(yield_usa)):
    error_acres.append(production_usa[index] - acres_usa[index] * yield_usa[index - 1])

import seaborn

seaborn.barplot(x=years_numbers[1:], y=error_acres)

# Результат
# Первая стратегия — площадь посевов предсказана, а урожайность прошлогодняя:
# https://pictures.s3.yandex.net/resources/Untitled_-_2020-10-22T210646.773_1603390014.png

print('     Task_2')
"""
2
Проделайте то же самое для второй стратегии — площадь посевов прошлогодняя, а урожайность настоящая. 
Результаты сохраните в списке error_yield. 
Затем постройте столбчатую диаграмму, на которой по оси X отмечены года, 
начиная с 1981-го, а по оси Y — значения error_yield.
"""
# ваш код здесь
error_yield = []

for index in range(1, len(yield_usa)):
    error_yield.append(production_usa[index] - acres_usa[index - 1] * yield_usa[index])

seaborn.barplot(x=years_numbers[1:], y=error_yield)

# Результат
# Вторая стратегия — урожайность предсказана, а площадь посевов прошлогодняя:
# https://pictures.s3.yandex.net/resources/Untitled_-_2020-10-22T210702.372_1603390030.png

"""
Промежуточный ВЫВОД
В обоих стратегиях ошибки  разнонаправленные, однако масштаб графика во второй стратегии меньше. => 
=> Вторая стратегия более правдива
"""

"""
 Среднее арифметическое всех отклонений по модулю — это среднее абсолютное отклонение. 
 На английском — mean absolute error, то есть MAE. Формула расчёта MAE выглядит так:
https://pictures.s3.yandex.net/resources/mae_1603390532.png
"""
"""
Функция abs()
Для вычисления модуля в Python есть готовая функция — abs(). 
Ей можно передать любое число, а она вернёт его абсолютное значение, то есть модуль:
"""

print('     Task_3')
"""
3
Применяя функцию abs(), получите абсолютные значения ошибок из списка error_acres и 
сохраните результат в новом списке — error_abs_acres.
"""

import pandas

data = pandas.read_csv('crops_usa.csv')

# преобразуем столбцы датасета в списки
acres = list(data['Acres'])
production = list(data['Production'])
years = list(data['Year'])

acres_usa = []  # общая площадь посевов за каждый год
production_usa = []  # общий объём урожая за каждый год

for year in range(1980, 2020):
    acres_one_year = []
    production_one_year = []
    for index in range(len(data)):
        if years[index] == year:
            acres_one_year.append(acres[index])
            production_one_year.append(production[index])
    acres_usa.append(sum(acres_one_year))
    production_usa.append(sum(production_one_year))

yield_usa = []  # общая урожайность за каждый год
for index in range(len(production_usa)):
    yield_usa.append(production_usa[index] / acres_usa[index])
years_numbers = list(range(1980, 2020))

error_acres = []  # ошибки первой модели, предсказана площадь посевов
for index in range(1, len(production_usa)):
    error_acres.append(production_usa[index] - acres_usa[index] * yield_usa[index - 1])

error_yield = []  # ошибки второй модели, предсказана урожайность
for index in range(1, len(production_usa)):
    error_yield.append(production_usa[index] - acres_usa[index - 1] * yield_usa[index])

# ваш код здесь

error_abs_acres = []  # модули ошибок первой модели

for value in error_acres:
    error_abs_acres.append(abs(value))


print(error_acres)
print(error_abs_acres)  # выводим списки на экран


print('     Task_4')
"""
4
Модули ошибок есть — теперь можно считать среднее. 
Разделите сумму всех значений списка error_abs_acres на его длину и выведите результат на экран.
"""

print(sum(error_abs_acres) / len(error_abs_acres))  # MAE первой модели


print('     Task_5')
"""
5
Вычислите среднее абсолютное отклонение для второй модели. 
Создайте список error_abs_yield и добавьте в него модули значений списка error_yield. 
Затем разделите сумму всех значений списка error_abs_yield на его длину и выведите результат на экран.
"""

error_abs_yield = []  # модули ошибок второй модели

for value in error_yield:
    error_abs_yield.append(abs(value))

print(sum(error_abs_yield) / len(error_abs_yield))  # MAE второй модели

"""
Результат
209394344.66107476
110396388.66393325
"""
"""
ВЫВОД
Средняя ошибка во второй стратегии почти в два раза меньше, чем в первой. 
Значит, графики не обманули — Герману и правда лучше предсказывать урожайность. 
Исследование готово!
"""
