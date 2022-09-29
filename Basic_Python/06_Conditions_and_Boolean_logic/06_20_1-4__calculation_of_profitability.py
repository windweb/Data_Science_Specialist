"""
Расчёт прибыльности
Лучшее помещение для магазина — то, которое принесёт больше всего прибыли.
Чтобы отыскать его, нужно рассчитать ожидаемую прибыльность всех 94 подходящих объектов недвижимости из датасета и
выбрать самые перспективные.
"""
"""
===================================
Данные от магазинов
    От 5% до 15% посетителей совершают покупку.
    Средняя стоимость покупки — от 20 до 22 тысяч рублей.
    Наценка на робокотов — 20%.
    Магазин работает 18 часов в сутки.
    В магазине посменно работают 2 продавца.
    Зарплата продавца — 50 000 рублей + 43% налогов.

Ожидаемая выручка:
https://pictures.s3.yandex.net/resources/les123_1606406662.jpg

Ожидаемые расходы
https://pictures.s3.yandex.net/resources/d-1_1606406731.jpg

Ожидаемая прибыльность
https://pictures.s3.yandex.net/resources/d_1606406743.jpg

traffic * 18 * 1/225 * 0.1 * 21000 * 0.2 * 30 - (price + 2 * 50000 * 1.43)

"""
print('     Task 1/4')
"""
1/4.
Ваш фильтр создаёт четыре списка с ключевыми параметрами помещения. 
Мы добавили ещё один — filtered_objects_profits. 
Сохраните в нём прогноз прибыли, рассчитанный по формуле: 
traffic * 18 * 1/225 * 0.1 * 21000 * 0.2 * 30 - (price + 2 * 50000 * 1.43). 
Затем выведите максимальное значение из этого списка на экран. 
Для этого примените функцию max(), указав в её скобках название списка — filtered_objects_profits.
"""

import pandas

realty_df = pandas.read_csv('yandex_realty_data.csv')

filtered_objects_area = []
filtered_objects_price = []
filtered_objects_traffic = []
filtered_objects_address = []
filtered_objects_profits = []  # новый список для прибыльности

for index in range(len(realty_df)):
    if (realty_df['floor'][index] == 1 and
            realty_df['area'][index] >= 40 and
            realty_df['price'][index] <= 190000 and
            realty_df['commercial_type'][index] in ['FREE_PURPOSE', 'RETAIL'] and
            realty_df['distance'][index] <= 6.7 and
            realty_df['already_taken'][index] == 0 and
            realty_df['competitors'][index] <= 1):
        filtered_objects_area.append(realty_df['area'][index])
        filtered_objects_price.append(realty_df['price'][index])
        filtered_objects_traffic.append(realty_df['traffic'][index])
        filtered_objects_address.append(realty_df['address'][index])
        filtered_objects_profits.append(realty_df['traffic'][index] *
        18 * 1/225 * 0.1 * 21000 * 0.2 * 30 - (realty_df['price'][index] + 2 * 50000 * 1.43))  # добавьте расчёт прибыли

print(max(filtered_objects_profits))  # выведите максимальную прибыльность среди отфильтрованных объектов

print('     Task 2/4')
"""
2/4.
Вы нашли максимальную прибыльность среди подходящих объектов. 
Теперь определите, какому объявлению соответствует этот показатель.
Для этого пройдите по списку filtered_objects_profits и сравните его значения с максимальным. 
Если они совпадут — выведите на экран индекс объекта.
"""

max_profit = max(filtered_objects_profits) # максимальная прибыль

# выведите индекс объекта с максимальной прибылью
for index_profit in range(len(filtered_objects_profits)):
    if filtered_objects_profits[index_profit] == max_profit:
        print(index_profit)

print('     Task 3/4')
"""
3/4.
Одного объекта мало — Филу нужно представить несколько лучших вариантов.
Найдите все объекты, потенциальная прибыльность которых больше 500 тысяч рублей, 
и выведите на экран всю сохранённую информацию по ним: 
площадь, стоимость аренды, проходимость, адрес и прогноз прибыли.
"""

import pandas

realty_df = pandas.read_csv('yandex_realty_data.csv')

filtered_objects_area = []
filtered_objects_price = []
filtered_objects_traffic = []
filtered_objects_address = []
filtered_objects_profits = []

for index in range(len(realty_df)):
    if (realty_df['floor'][index] == 1 and
        realty_df['area'][index] >= 40 and
        realty_df['price'][index] <= 190000 and
        realty_df['commercial_type'][index] in ['FREE_PURPOSE', 'RETAIL'] and
        realty_df['distance'][index] <= 6.7 and
        realty_df['already_taken'][index] == 0 and
        realty_df['competitors'][index] <= 1):
        filtered_objects_area.append(realty_df['area'][index])
        filtered_objects_price.append(realty_df['price'][index])
        filtered_objects_traffic.append(realty_df['traffic'][index])
        filtered_objects_address.append(realty_df['address'][index])
        filtered_objects_profits.append(realty_df['traffic'][index] *
        18 * 1/225 * 0.1 * 21000 * 0.2 * 30 - (realty_df['price'][index] +
        2 * 50000 * 1.43))

for index_profit_more_500k in range(len(filtered_objects_profits)):
    if filtered_objects_profits[index_profit_more_500k] >= 500000:  # допишите новое условие
        print(filtered_objects_area[index_profit_more_500k]) # выведите данные из filtered_objects_area
        print(filtered_objects_price[index_profit_more_500k]) # данные из filtered_objects_price
        print(filtered_objects_traffic[index_profit_more_500k]) # теперь из filtered_objects_traffic
        print(filtered_objects_address[index_profit_more_500k]) # из filtered_objects_address
        print(filtered_objects_profits[index_profit_more_500k]) # и filtered_objects_profits
        print('----------')


print('     Task 3/4')
"""
4/4.
Казалось бы, задача решена: список можно нести Филу, а потом и Майе. 
Однако всё не так просто. 
Формула для прогноза прибыли основана на средних показателях существующих магазинов — 
а реальные могут оказаться ниже.
Если взять за основу не средние параметры, а минимальные, финальный результат может измениться. 
Формула точно изменится. 
Вместо каждого 225-го посетителя — каждый 300-й, вместо каждого 10-го покупателя — каждый 20-й, 
а вместо среднего чека в 21 000 рублей — 20 000 рублей:
traffic * 18 * 1/300 * 0.05 * 20000 * 0.2 * 30 - (price + 2 * 50000 * 1.43)

Добавьте к выводу на экран минимальную ожидаемую прибыль для каждого из пяти лучших объектов.
"""
for index_profit_more_500k in range(len(filtered_objects_profits)):
    if filtered_objects_profits[index_profit_more_500k] >= 500000:  # допишите новое условие
        print(filtered_objects_area[index_profit_more_500k]) # выведите данные из filtered_objects_area
        print(filtered_objects_price[index_profit_more_500k]) # данные из filtered_objects_price
        print(filtered_objects_traffic[index_profit_more_500k]) # теперь из filtered_objects_traffic
        print(filtered_objects_address[index_profit_more_500k]) # из filtered_objects_address
        print(filtered_objects_profits[index_profit_more_500k]) # и filtered_objects_profits
        print('----------')
        print(filtered_objects_traffic[index_profit_more_500k] *
        18 * 1/300 * 0.01 * 20000 * 0.2 * 30 - (filtered_objects_price[index_profit_more_500k] +
        2 * 50000 * 1.43))  # добавьте пессимистичную оценку прибыльности
        print('----------')

# Передайте функции print() новую формулу.
# Переменные для неё возьмите из списков filtered_objects_traffic и filtered_objects_price.