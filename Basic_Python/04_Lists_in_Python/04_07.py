"""
Посчитайте среднюю конверсию за год и доход от одной установки.
Для этого найдите сумму всех значений в столбце payments и разделите её на сумму значений в столбце installs.
Чтобы вычислить доход от одной установки, умножьте полученную конверсию на 600.
Выведите результаты на экран на разных строчках.
"""
import pandas
data = pandas.read_csv('app_stats.csv')

# ваш код здесь
summa_installs_year = sum(data['installs'])
summa_payments_year = sum(data['payments'])

print(summa_payments_year/summa_installs_year)  # выведите значение средней конверсии
print((summa_payments_year/summa_installs_year)*600)  # и сколько в среднем приносит одна установка