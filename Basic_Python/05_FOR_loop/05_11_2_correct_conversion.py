"""
2.
Теперь оценим количество «рекламных» покупок.
Допишите цикл из предыдущего задания:
для каждой недели в campaign_weeks посчитайте разницу между числом платежей (payments) в эту неделю и в предыдущую.
Результаты сохраните в списке payments_from_ads — тогда print() выведет их на экран.

2.
Now estimate the number of "promotional" purchases.
Complete the loop from the previous task:
for each week in campaign_weeks, calculate the difference between the number of payments in that week and the previous week.
Save the results to payments_from_ads list - then print() will display them.
"""

import pandas

data = pandas.read_csv('app_stats.csv')

payments = list(data['payments'])  # список с числом платежей
installs = list(data['installs'])  # список с числом установок

campaign_weeks = [7, 9, 13, 15, 17, 19, 29, 31, 33, 45]

installs_from_ads = []

# создайте список payments_from_ads
payments_from_ads = []

for week_number in campaign_weeks:
    installs_from_ads.append(installs[week_number] - installs[week_number - 1])
    # ваш код здесь
    payments_from_ads.append(payments[week_number] - payments[week_number - 1])

print(payments_from_ads)  # выводим результаты на экран