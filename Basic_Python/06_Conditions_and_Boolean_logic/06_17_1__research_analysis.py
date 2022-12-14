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
1.
Диаграммы рассеяния очень удобны для изучения картографических данных: 
две оси координат становятся широтой и долготой, а точки — объектами на карте.
Постройте диаграмму рассеяния, на которой по оси X расположены данные из колонки longitude, а по оси Y — latitude.
"""
import pandas
import seaborn

realty_df = pandas.read_csv('yandex_realty_data.csv')

# постройте диаграмму рассеяния
seaborn.scatterplot(x=realty_df['longitude'], y=realty_df['latitude'])