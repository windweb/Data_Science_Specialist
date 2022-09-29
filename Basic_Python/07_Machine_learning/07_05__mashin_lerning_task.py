"""
Нужно определить, что даст более точный прогноз объёма урожая:
предсказание площади посевов или урожайности.
"""

import pandas

data = pandas.read_csv('crops_usa.csv')
print(data)

"""
Результат
      Year          State  State ANSI    Acres  Production
0     2019        ALABAMA           1   130000     6120000
1     2019        ARIZONA           4    34000     3432000
2     2019       ARKANSAS           5   110000     2600000
3     2019     CALIFORNIA           6   420000     7244000
4     2019       COLORADO           8  2150000    98000000
...    ...            ...         ...      ...         ...
1665  1980       VIRGINIA          51   317000    10582000
1666  1980     WASHINGTON          53  3320000   160220000
1667  1980  WEST VIRGINIA          54    12000      380000
1668  1980      WISCONSIN          55   119000     4365000
1669  1980        WYOMING          56   352000     8620000

[1670 rows x 5 columns]


[1670 rows x 5 columns]
В датасете пять столбцов:
    Year — год,
    State — название штата,
    State ANSI — код штата,
    Acres — количество посевов в акрах для определённого штата и года,
    Production — объём урожая для определённого штата и года в бушелях.
    
Урожайность и посевы
Вам предстоит оценить, что важнее предсказывать — площадь посевов или урожайность. 
С площадью понятно — она записана в столбце Acres.
"""

"""
Исследовательский анализ данных
Продолжаем исследовать данные из crops_usa.csv.
Во-первых, стоит проверить содержание столбцов Year и State — 
действительно ли в датасете представлены данные за все 40 лет и по всем штатам.
И, во-вторых, построить графики по существующим столбцам. 
Например, интересно посмотреть, насколько отличаются разные штаты по посевным площадям и объёму урожая. 
Лучше всего это позволит выявить столбчатая диаграмма.
"""

print('     Task_1')
"""
1/5.
Проверьте, за какие года есть данные в датасете. 
Создайте список years_unique, сохраните в нём уникальные значения из столбца Year и выведите этот список на экран. 
На следующей строчке выведите на экран длину списка years_unique.
"""

# создайте список years_unique
years_unique = []
# добавьте в него уникальные значения из Year
for index in range(len(data['Year'])):
    if data['Year'][index] not in years_unique:
        years_unique.append(data['Year'][index])

print(years_unique)
print(len(years_unique))  # выведите длину списка years_unique

"""
Результат
[2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980]
40
"""
print('     Task_2')
"""
2/5.
Теперь проделайте то же самое со штатами.
Создайте список states_unique и сохраните в нём уникальные значения из столбца State. 
Выведите на экран полученный список и его длину.
"""

# создайте список states_unique
states_unique = []
# добавьте в него уникальные значения из колонки State
for index in range(len(data['State'])):
    if data['State'][index] not in states_unique:
        states_unique.append(data['State'][index])

print(states_unique)
print(len(states_unique))  # выведите длину списка states_unique

"""
Результат
['ALABAMA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'DELAWARE', 'GEORGIA', 'IDAHO', 'ILLINOIS', 'INDIANA', 'KANSAS', 'KENTUCKY', 'MARYLAND', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VIRGINIA', 'WASHINGTON', 'WISCONSIN', 'WYOMING', 'FLORIDA', 'IOWA', 'LOUISIANA', 'NEVADA', 'WEST VIRGINIA']
42
"""
print('     Task_3')
"""
3/5.
Оценить различия в площади посевных площадей в разных штатах легче всего по столбчатой диаграмме: 
каждый столбец на ней будет соответствовать определённому штату, а его высота — количеству засеянных акров за год. 
Например, за 2019-й. Чтобы построить такую диаграмму, потребуются списки с координатами.
Создайте два списка: acres_2019 и states_2019. 
Они будут хранить площади посевных площадей и названия штатов. 
Напишите фильтр, который добавит в acres_2019 значения за 2019 год из списка acres, 
а в states_2019 — аналогичные значения из списка states.
"""

# преобразуем Acres, Year и State в списки
acres = list(data['Acres'])
years = list(data['Year'])
states = list(data['State'])

# создайте новые списки
acres_2019 = []
states_2019 = []
# отфильтруйте значения в acres и states по значению в year
for index in range(len(years)):
    if years[index] == 2019:
        acres_2019.append(acres[index])
        states_2019.append(states[index])

print(acres_2019)
print(states_2019)

"""
Резульат
[130000, 34000, 110000, 420000, 2150000, 60000, 150000, 1195000, 650000, 330000, 6900000, 460000, 345000, 540000, 1450000, 45000, 550000, 5450000, 1070000, 19000, 360000, 90000, 290000, 7505000, 500000, 4200000, 740000, 180000, 70000, 1500000, 280000, 4500000, 125000, 180000, 2260000, 195000, 125000]
['ALABAMA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'DELAWARE', 'GEORGIA', 'IDAHO', 'ILLINOIS', 'INDIANA', 'KANSAS', 'KENTUCKY', 'MARYLAND', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VIRGINIA', 'WASHINGTON', 'WISCONSIN', 'WYOMING']
"""

print('     Task_4')
"""
4/5.
Постройте столбчатую диаграмму, отражающую площадь посевов для каждого штата за 2019 год. 
По оси X разместите значения списка acres_2019, а по оси Y — states_2019.
"""

import seaborn

seaborn.barplot(x=acres_2019, y=states_2019)

print('     Task_5')
"""
5/5.
Интересно, соответствует ли распределению посевов объём урожая. 
Неужели 10% штатов выращивают 90% пшеницы?
Измените код — на этот раз поместите на столбчатую диаграмму 
по оси X значения столбца Production вместо Acres.


Преобразуйте столбец data['Production'] в список функцией list() 
и сохраните в переменной production. 
Затем создайте пустой список production_2019 
и добавьте в него значения из production за 2019 год. 
Проще всего это сделать, 
заменив два упоминания слова acres в фильтре на production.
"""
production = list(data['Production'])
production_2019 = []

for index in range(len(years)):
    if years[index] == 2019:
        production_2019.append(production[index])

seaborn.barplot(x=production_2019, y=states_2019)

"""
# итоговый код
import pandas
data = pandas.read_csv('crops_usa.csv')

production = list(data['Production'])
years = list(data['Year'])
states = list(data['State'])

production_2019 = []
states_2019 = []

for index in range(len(years)):
    if years[index] == 2019:
        production_2019.append(production[index])
        states_2019.append(states[index])

import seaborn

seaborn.barplot(x=production_2019, y=states_2019)

"""