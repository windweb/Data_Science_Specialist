"""Исследовательский анализ
При изучении датасета вы увидели, что некоторых данных в нём не хватает, а некоторые — не соответствуют вашим целям.
Это предстоит учесть при фильтрации данных.
Осталось четыре потенциально важных столбца:
    longitude — долгота,
    latitude — широта,
    distance — расстояние,
    traffic — проходимость.
Здесь анализа на уровне самих значений будет уже недостаточно.
Смысл этих колонок станет понятнее, если для каждой построить диаграмму рассеяния."""

"""
2.
Столбец distance хранит расстояние. 
Но расстояние до чего?
Это может быть центр города или произвольная точка на карте, от которой Яндекс.Недвижимость ведёт отсчёт.
Исследуйте это. Добавьте параметр hue, чтобы изменить цвет точек в соответствии со значениями столбца distance.
"""
import pandas
import seaborn

realty_df = pandas.read_csv('yandex_realty_data.csv')

# добавьте параметр hue
seaborn.scatterplot(x=realty_df['longitude'], y=realty_df['latitude'], hue=realty_df['distance'])
