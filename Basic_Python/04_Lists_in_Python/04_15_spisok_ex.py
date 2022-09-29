print('     Task 1/3')
"""
1.
Средствами библиотеки Pandas откройте файл app_stats.csv и сохраните его в переменной data.
Преобразуйте столбцы 'installs' и 'payments' в списки, сохраните их в соответствующих переменных.
Выведите installs и payments на экран.
"""

# импортируйте библиотеку pandas
import pandas
# откройте файл и сохраните его в переменной data
data = pandas.read_csv('app_stats.csv')
# создайте список installs из столбца 'installs'
installs = list(data['installs'])
# создайте список payments из колонки 'payments'
payments = list(data['payments'])
# выведите на экран installs
print(installs)
# выведите на экран payments
print(payments)

print('     Task 2/3')
"""
2/3.
Посчитайте и выведите на экран конверсию для каждой из последних восьми недель — 
разделите количество платежей на количество установок.
"""
# найдите конверсию для 8-й недели с конца
konversiya_8 = payments[-8] / installs[-8]
print(konversiya_8)
# найдите конверсию для 7-й недели с конца
konversiya_7 = payments[-7] / installs[-7]
print(konversiya_7)
# найдите конверсию для 6-й недели с конца
konversiya_6 = payments[-6] / installs[-6]
print(konversiya_6)
# найдите конверсию для 5-й недели с конца
konversiya_5 = payments[-5] / installs[-5]
print(konversiya_5)
# найдите конверсию для 4-й недели с конца
konversiya_4 = payments[-4] / installs[-4]
print(konversiya_4)
# найдите конверсию для 3-й недели с конца
konversiya_3 = payments[-3] / installs[-3]
print(konversiya_3)
# найдите конверсию для 2-й недели с конца
konversiya_2 = payments[-2] / installs[-2]
print(konversiya_2)
# найдите конверсию для 1-й недели с конца
konversiya_1 = payments[-1] / installs[-1]
print(konversiya_1)

print('     Task 3/3')
"""
3/3.
Посчитайте средний доход от одной установки для каждой недели: 
умножьте недельные конверсии на стоимость платной версии «Книжного грызуна» — 600 рублей.
"""
x = 600
print(payments[-8] / installs[-8] * x)  # умножьте результат на 600
print(payments[-7] / installs[-7] * x)  # умножьте результат на 600
print(payments[-6] / installs[-6] * x)  # умножьте результат на 600
print(payments[-5] / installs[-5] * x)  # умножьте результат на 600
print(payments[-4] / installs[-4] * x)  # умножьте результат на 600
print(payments[-3] / installs[-3] * x)  # умножьте результат на 600
print(payments[-2] / installs[-2] * x)  # умножьте результат на 600
print(payments[-1] / installs[-1] * x)  # умножьте результат на 600