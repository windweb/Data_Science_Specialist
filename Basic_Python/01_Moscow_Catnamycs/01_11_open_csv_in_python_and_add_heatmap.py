import pandas
import seaborn  # Чтобы создать тепловую карту в Python, подключите библиотеку seaborn.

data = pandas.read_csv('polomki.csv', index_col='Магазин')

print(seaborn.heatmap(data))

data['Неделя 14'] = data['Неделя 14'] * 100  # 1. Умножьте на 100 все значения столбца 'Неделя 14' и перезапишите его.

print(data['Неделя 14'])  # 2. Выведите обновлённый столбец 'Неделя 14' из таблицы с поломками на экран.

print(seaborn.heatmap(data))  # 3. Убедитесь, что с таблицей всё в порядке. \
                              #    Выведите всю таблицу с поломками на экран и проверьте,
                              #    что данные в последнем столбце обновлены.

"""
Результат
https://pictures.s3.yandex.net/resources/jupiter_2_2880_1638523363.png
"""

