"""
Результаты
Исследование официально объявляется завершённым.
Если убрать все предложения с отрицательной прибыльностью в пессимистичном сценарии, то останется всего три объекта,
где ожидаемая прибыль больше 500 тысяч в месяц:

173950.0                 – стоимость аренды в месяц
978                      – проходимость в час
Россия, Москва, Берсеневская набережная, 6с1
668874.0000000001        – прибыльность в среднем сценарии
35130.0                  – прибыльность в пессимистичном сценарии
----------
161500.0
1097
Россия, Москва, Болотная набережная, 11с1
801276.0000000002
90420.0
----------
150000.0
837
Россия, Москва, Большой Кисельный переулок, 5
550696.0
8320.0
----------

Этот список соответствует умеренному аппетиту к риску —
при выборе самых прибыльных объектов вы опирались на средние показатели.
Если заказчик готов рисковать, можно сделать такой же список для оптимистичного сценария —
взять не средние, а максимальные показатели магазинов. Если же готовность рисковать низкая — минимальные.

Правда, не стоит забывать о природе данных в основе расчётов.
Спрогнозировать прибыль позволил опыт существующих магазинов, поэтому полностью полагаться на такой прогноз нельзя.
На прибыльность нового магазина могут повлиять какие-нибудь новые, неучтённые факторы.
Да и в данных могли быть ошибки.

И всё же лучше основывать выбор на аналитике и прогнозах, чем надеяться на удачу.
Вы уже сделали больше, чем ждали Фил и Майя.

Последние штрихи
Ваш код может быть полезен не только в этом исследовании, но и в будущих проектах.
Но для этого не хватает одной детали.

Взгляните на свой проект:

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
        18 * 1/225 * 0.1 * 0.2 * 21000 * 30 - (realty_df['price'][index] +
        2 * 50000 * 1.43))

for index in range(len(filtered_objects_profits)):
    if filtered_objects_profits[index] > 500000:
        print(filtered_objects_price[index])
        print(filtered_objects_traffic[index])
        print(filtered_objects_address[index])
        print(filtered_objects_profits[index])
        print(filtered_objects_traffic[index] * 18 * 1/300 * 0.05 * 20000 * 0.2 * 30 -
        (filtered_objects_price[index] + 2 * 50000 * 1.43))
        print('----------')


Его особенность — множество числовых констант: 18, 0.2, 190000. 
В будущем использовать такой код окажется сложно. 
Вы только потратите время, вспоминая смысл этих чисел.
Для констант принято заводить переменные. 
Кода станет больше, но и понять его будет легче. 
Если в будущем захотите рассчитать прибыльность для магазина другой компании, 
достаточно будет подставить новые значения в переменные:
"""

min_required_area = 40  # минимальная требуемая площадь
max_affordable_price = 190000  # максимально допустимая арендная ставка
third_ring_radius = 6.7  # максимальное расстояние от центра

open_hours_number = 18  # количество рабочих часов в сутки
traffic2visitors_average_ratio = 1 / 225  # средняя доля посетителей от числа прохожих
traffic2visitors_pessimistic_ratio = 1 / 300  # минимальная доля посетителей от числа прохожих
visitors2purchases_average_ratio = 0.1  # средняя доля покупателей от числа посетителей
visitors2purchases_pessimistic_ratio = 0.05  # минимальная доля покупателей от числа посетителей
average_order_value = 21000  # средняя стоимость покупки
average_order_value_pessimistic = 20000  # минимальная стоимость покупки
trade_margin = 0.2  # наценка
days_in_months = 30  # количество рабочих дней в месяц

# множитель для расчёта прибыльности в среднем сценарии
income_multiplier_average = (open_hours_number *
                             traffic2visitors_average_ratio *
                             visitors2purchases_average_ratio *
                             average_order_value *
                             trade_margin *
                             days_in_months)

# множитель для расчёта прибыльности в пессимистичном сценарии
income_multiplier_pessimistic = (open_hours_number *
                                 traffic2visitors_pessimistic_ratio *
                                 visitors2purchases_pessimistic_ratio *
                                 average_order_value_pessimistic *
                                 trade_margin *
                                 days_in_months)

number_of_employees = 2  # количество продавцов
employee_salary = 50000  # зарплата продавца
tax_multiplier = 1.43  # множитель для расчёта зарплаты с налогами

# зарплатная часть расходов
addition_to_expenses = number_of_employees * employee_salary * tax_multiplier

# минимальная ожидаемая прибыль
min_expected_profits = 500000

import pandas

realty_df = pandas.read_csv('yandex_realty_data.csv')

filtered_objects_area = []
filtered_objects_price = []
filtered_objects_traffic = []
filtered_objects_address = []
filtered_objects_profits = []

for index in range(len(realty_df)):
    if (realty_df['floor'][index] == 1 and
        realty_df['area'][index] >= min_required_area and
        realty_df['price'][index] <= max_affordable_price and
        realty_df['commercial_type'][index] in ['FREE_PURPOSE', 'RETAIL'] and
        realty_df['distance'][index] <= third_ring_radius and
        realty_df['already_taken'][index] == 0 and
        realty_df['competitors'][index] <= 1):
        filtered_objects_area.append(realty_df['area'][index])
        filtered_objects_price.append(realty_df['price'][index])
        filtered_objects_traffic.append(realty_df['traffic'][index])
        filtered_objects_address.append(realty_df['address'][index])
        filtered_objects_profits.append(realty_df['traffic'][index] *
        income_multiplier_average - (realty_df['price'][index] +
        addition_to_expenses))

for index in range(len(filtered_objects_profits)):
    if filtered_objects_profits[index] > min_expected_profits:
        print(filtered_objects_price[index])
        print(filtered_objects_traffic[index])
        print(filtered_objects_address[index])
        print(filtered_objects_profits[index])
        print(filtered_objects_traffic[index] * income_multiplier_pessimistic -
        (filtered_objects_price[index] + addition_to_expenses))
        print('----------')

"""
Прямой путь к результату
И последнее. Вы решили проект на «чистом» Python — применяя в основном его базовые операции. 
Дополнительные библиотеки понадобились лишь дважды:
    pandas — чтобы открыть датасет,
    seaborn — чтобы нарисовать диаграммы.
На практике обычно применяют библиотеки для выполнения стандартных действий — таких как фильтрация данных. 
Если использовать все возможности pandas, код проекта уместится в несколько строк:
"""

import pandas
realty_df = pandas.read_csv('yandex_realty_data.csv')

realty_df['expenses'] = realty_df['price'] + 2 * 50000 * 1.43
realty_df['incomes_normal'] = realty_df['traffic'] * 18 * 1/225 * 0.1 * 21000 * 0.2 * 30
realty_df['incomes_pessimistic'] = realty_df['traffic'] * 18 * 1/300 * 0.05 * 20000 * 0.2 * 30
realty_df['profits_normal'] = realty_df['incomes_normal'] - realty_df['expenses']
realty_df['profits_pessimistic'] = realty_df['incomes_pessimistic'] - realty_df['expenses']

realty_df_filtered = realty_df[(realty_df['floor'] == 1) &
                               (realty_df['area'] >= 40) &
                               (realty_df['price'] <= 190000) &
                               realty_df['commercial_type'].isin(['FREE_PURPOSE', 'RETAIL']) &
                               (realty_df['distance'] <= 6.7) &
                               (realty_df['already_taken'] == 0) &
                               (realty_df['competitors'] <= 1) &
                               (realty_df['profits_normal'] > 500000) &
                               (realty_df['profits_pessimistic'] > 0)]

print(realty_df_filtered)