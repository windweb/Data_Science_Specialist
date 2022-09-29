"""
Правильная конверсия
Если количество «рекламных» установок можно посчитать как разницу общего числа установок на «рекламной» и предшествующей неделях,
то аналогичным образом можно оценить и количество покупок, спровоцированных рекламой:
Взять количество покупок в неделю проведения рекламной кампании;
Вычесть из этого значения число покупок за предыдущую неделю.
Два этих показателя — количество «рекламных» установок и покупок —
позволят рассчитать конверсию только для тех пользователей,
которые скачали «Книжного грызуна» благодаря рекламной кампании.
А значит — проверить вторую гипотезу.
"""

"""
1.
Список campaign_weeks хранит номера недель, в которые проводились рекламные кампании. 
Они соответствуют индексам значений в списках payments и installs.
Для каждой недели в campaign_weeks посчитайте разницу между числом установок (installs) в эту неделю и в предыдущую. 
Чтобы обратиться к значению предыдущей недели, вычтите из индекса единицу прямо в квадратных скобках. 
Результаты сохраните в списке installs_from_ads, чтобы функция print() вывела их на экран.

1.
The campaign_weeks list stores the numbers of the weeks in which campaigns were run. 
They correspond to the index values in the payments and installs lists.
For each week in campaign_weeks, calculate the difference between the number of installations (installs) in that week and the previous week. 
To refer to the previous week's value, subtract one from the index directly in square brackets. 
Save the results to the installs_from_ads list for print() to display.
"""
import pandas
data = pandas.read_csv('app_stats.csv')

payments = list(data['payments'])  # список с числом платежей
installs = list(data['installs'])  # список с числом установок

campaign_weeks = [7, 9, 13, 15, 17, 19, 29, 31, 33, 45]

# ваш код здесь

previous_campaign_weeks = []
installs_from_ads = []
# print(installs)
for index in range(len(campaign_weeks)):
    previous_campaign_weeks.append(campaign_weeks[index] - 1)
    # print("!!!")
    # print(installs[campaign_weeks[index]])
    # print(installs[previous_campaign_weeks[index]])
    # print()
    installs_from = (installs[campaign_weeks[index]]) - (installs[previous_campaign_weeks[index]])
    # print(installs_from)
    # print("/!!!")
    installs_from_ads.append(installs_from)
    # installs_from_ads.append((payments[campaign_weeks[index]] - payments[campaign_weeks[previous_index]]))
# print(campaign_weeks, "campaign_weeks")
# print(previous_campaign_weeks, "previous_campaign_weeks")
print(installs_from_ads) # выводим результаты на экран