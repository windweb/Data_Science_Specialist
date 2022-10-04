print('Task 1.')
"""
Task 1
Write a loop that outputs all elements of the elements list to the screen.

Задача 1
Напишите цикл, который выведет все элементы списка elements на экран.

"""
elements = [5018, 4.1, -1000, 'hello', 3665]

# ваш код здесь
for item in elements:
    print(item)


print('Task 2.')
"""
Задача 2
В начало и конец списка musicians случайно попали два художника.
Напишите цикл, который поочерёдно выведет на экран все элементы musicians, кроме первого и последнего.

Task 2
There are two artists in the beginning and end of the list of musicians by accident. 
Write a loop that will alternately display all but the first and last musicians.
"""
musicians = ['Ван Гог', 'Моцарт', 'Би-2', 'Земфира', 'Beatles', 'Луна', 'Розенбаум', 'Звери', 'Патрисия Каас', 'Сальвадор Дали']

# ваш код здесь
for item in range(1,(len(musicians)-1)):
    print(musicians[item])
"""
Если бы перед вами стояла обратная задача — вывести на экран только первый и последний элемент списка 
и сделать это непременно в цикле — решение могло быть таким:

for index in [0, 9]:
    print(musicians[index])
"""

print('Task 3.')
"""
Задача 3
Посчитайте средствами Python и выведите на экран количество элементов в списках halley_comet и moon_craters. 
Первый хранит годы появления кометы Галлея, а второй — названия крупных кратеров на видимой стороне Луны.

Task 3.
Calculate using Python and display the number of items in the lists halley_comet and moon_craters. 
The first one stores the years when Galley comet comet appeared, and the second one stores the names of large craters on the visible side of the Moon
"""

halley_comet = [66, 141, 218, 295, 374, 451, 530, 607, 684, 760, 837, 912, 989, 1066, 1145, 1222, 1301, 1378, 1456, 1531, 1607, 1682, 1759, 1835, 1910, 1986]

moon_craters = ['Fra Mauro', 'Tycho', 'Bailly', 'Longomontanus', 'Stadius', 'Rheita', 'Pitatus', 'Stöfler', 'Wargentin', 'Humboldt', 'Russell', 'Plinius', 'Aristarchus', 'Seleucus', 'Thebit', 'Janssen', 'Vendelinus', 'Metius', 'Schickard', 'Albategnius', 'Aristoteles', 'Piccolomini', 'Copernicus', 'Picard', 'Maginus', 'Clavius', 'Petavius', 'Moretus', 'Langrenus', 'Theophilus']

# ваш код здесь
print(len(halley_comet), len(moon_craters))

print('Task 4.')
"""
Задача 4
Список dangerous_animals хранит 9 значений. 
Напишите цикл, который выведет все элементы dangerous_animals на экран, применив функцию range().

Task 4
The list dangerous_animals stores 9 values. 
Write a loop that outputs all items of dangerous_animals using the range() function.
"""

dangerous_animals = ['волк', 'медведь', 'тигр', 'крокодил', 'леопард', 'бегемот', 'удав', 'тираннозавр', 'лев']

# ваш код здесь
for item in range(len(dangerous_animals)):
    print(dangerous_animals[item])

print('Task 5.')
"""
Задача 5
Защитите себя от хищников — сделайте их добрыми. 
Выведите на экран все значения списка dangerous_animals, предваряя каждый элемент словом 'добрый'.

Task 5
Protect yourself from predators - make them kind. 
Display all the values of the dangerous_animals list, prefacing each item with the word 'kind'.
"""
dangerous_animals = ['волк', 'медведь', 'тигр', 'крокодил', 'леопард', 'бегемот', 'удав', 'тираннозавр', 'лев']
for item in range(len(dangerous_animals)):
    print("добрый", dangerous_animals[item])
print('Task 6.')
"""
Задача 6
Объедините новое знание со старым — методом append() из предыдущей темы. 
При помощи цикла for создайте список zeros из ста нулей и выведите его на экран.

Task 6.
Use the for loop and append() method to create a list of one hundred zeros and display it on the screen. 

"""
zeros = []
#i = 0
for _ in range(100):
    zeros.append(0)
    # i += 1
# print(i, "i")
print(zeros)  # выводим список на экран

print('Task 7.')
"""
Задача 7
Список july_temperatures хранит дневные значения температуры в цельсиях за июль в Москве. 
Сделайте лето теплее — напишите цикл, который добавит по 10 градусов к каждому значению. 
Выведите изменённый список на экран.

Task 7
The list july_temperatures stores daily temperature values in celsius for July in Moscow. 
Make summer warmer - write a loop that adds 10 degrees to each value. 
Display the modified list on the screen.

"""

july_temperatures = [15, 17, 17, 13, 8, 12, 12, 12, 9, 15, 8, 10, 11, 9, 13, 9, 8, 11, 9, 16, 7, 12, 14, 10, 7, 16, 13, 12, 7, 12, 15]


# your code is here
for item in range(len(july_temperatures)):  # Для изменения значений исходного списка, пишем цикл с перебором по индексам.
    july_temperatures[item] += 10  # В теле цикла прибавим 10 к каждому элементу july_temperatures.
                                   # Используем оператор для сложения с присвоением +=.
print(july_temperatures)

"""
Другой вариант решения:

i = 0
for item in july_temperatures:
    july_temperatures[i] = july_temperatures[i] + 10
    i += 1
print(july_temperatures)

"""
print('Task 8.')
"""
Задача 8
Циклы работают не только со списками, но и со строками.
Объедините две строки: 'В еиоен' и 'ывлклпы'.
Для этого объявите переменную final_string с пустой строкой. 
Затем создайте цикл, в теле которого пропишите две инструкции: 
    в первой поочерёдно добавляйте к значению final_string символы из first_string, 
    во второй — символы из second_string. 
Заметьте, что исходные строки одинаковой длины — индексация совпадает.

Task 8.
Cycles work not only with lists but also with strings.
Combine two strings: 'V eioen' and 'yvlklpy'. 
To do that, declare a variable final_string with an empty string. 
Then create a loop in the body of which you write two instructions: 
    in the first one in turn add to the value of final_string characters from first_string, 
    in the second one - characters from second_string. 
Note that source strings are the same length - indexing is the same.

"""

first_string = 'Yuaeget'
second_string = 'o r ra.'

# your code is here
final_string = ''
for item in range(0, len(first_string)):
    final_string = final_string + first_string[item]
    final_string =final_string + second_string[item]
print(final_string)  # display the result on the screen


print('Task 1.')
"""
Oбъявите переменную final_string и сохраните в ней пустую строку (''). 
Затем создайте цикл с итерацией по индексам. 
В скобках range() укажите len(first_string), а в теле цикла напишите две строчки: 
final_string = final_string + first_string[...] и final_string = final_string + second_string[...], 
где вместо ... — имя переменной цикла. 
Удачное название переменной в циклах с перебором по индексам — index.
"""

"""
Buttercups and Other Flowers
The developers of the Buttercups and Other Flowers gardening app have assessed your knowledge of lists and 
cycles and invited you to work with their data. Help them estimate your earnings and 
calculate conversion rates by solving eight more challenges.

Task 1.
To begin, write a loop that counts and displays the earnings of "Buttercups and Other Flowers" from the app's sales for each month.
The list "payers" stores the number of users who bought the paid version of the "Buttercups and Other Flowers" app in each month of the last year. 
The price of the app is recorded in the "purchase_amount" variable - $5.
"""

payers = [75, 48, 65, 68, 74, 67, 71, 65, 90, 85, 79, 81]
purchase_amount = 5  # сумма покупки в долларах
for item in range(0, len(payers)):
    val = payers[item] * purchase_amount
    print(val)

print('Task 2.')
"""
Задача 2
В предыдущем задании вы написали цикл, который вывел на экран заработок «Лютиков и других цветочков» 
от продаж платной версии приложения за каждый месяц. 
Теперь напишите цикл, который сохранит эти данные в отдельный список — "monthly_income".

Task 2.
In the previous problem, you wrote a loop that outputs the earnings of "Buttercups and other flowers" 
from the sales of the paid version of the application for each month. 
Now write a loop that saves this data into a separate list - "monthly_income".
"""

payers = [75, 48, 65, 68, 74, 67, 71, 65, 90, 85, 79, 81]
purchase_amount = 5  # сумма покупки в долларах

# создайте список monthly_income
monthly_income = []
# напишите цикл, который заполнит monthly_income значениями
for item in range(0, len(payers)):
    income = payers[item] * purchase_amount
    monthly_income.append(income)
print(monthly_income)  # выводим новый список на экран

print('Task 3.')
"""
Задача 3
«Лютики и цветочки» доверили вам больше данных. 
Список installs хранит количество установок приложения за каждый месяц, начиная с января; 
список payers — помесячное число пользователей, купивших платную версию; 
список months — названия месяцев.
Подготовьте небольшой отчёт. Выведите данные на экран в таком формате:

Январь | установок: 5018 | покупок: 75
Февраль | установок: 4312 | покупок: 48
"""

installs = [5018, 4312, 4208, 3665, 3957, 4912, 5074, 5165, 4704, 4447, 4189, 4371]
payers = [75, 48, 65, 68, 74, 67, 71, 65, 90, 85, 79, 81]
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
for item in range(12):
    print(f"{months[item]} | установок: {installs[item]} | покупок: {payers[item]}")


print('Task 4.')
"""
Задача 4
Само по себе количество установок и покупок приложения мало о чём говорит. 
Рассчитайте конверсию — разделите каждый элемент списка payers на соответствующий элемент списка installs и выведите результат на экран.

Task 4
The number of installations and purchases of an application is not much of an indicator by itself. 
Calculate the conversion rate: 
divide each item in the "payers" list by the corresponding item in the "installs" list and display the result.
"""
installs = [5018, 4312, 4208, 3665, 3957, 4912, 5074, 5165, 4704, 4447, 4189, 4371]
payers = [75, 48, 65, 68, 74, 67, 71, 65, 90, 85, 79, 81]
for item in range(len(payers)):
    conversion_rate = payers[item] / installs[item]
    print(conversion_rate)
# Конверсия небольшая, зато стабильная: приложение покупает примерно каждый сотый скачавший его.


print('Task 5.')
"""
Задача 5
Снова рассчитайте конверсию по месяцам, но на этот раз сохраните результат в отдельном списке — conversions.

Task 5.
Again calculate the conversion rate by months, but this time save the result in a separate list - "conversions".

"""
installs = [5018, 4312, 4208, 3665, 3957, 4912, 5074, 5165, 4704, 4447, 4189, 4371]
payers = [75, 48, 65, 68, 74, 67, 71, 65, 90, 85, 79, 81]

conversions = []

# напишите код здесь
for item in range(len(payers)):
    conversion_rate = payers[item] / installs[item]
    conversions.append(conversion_rate)
print(conversions)  # выводим новый список на экран


print('Task 6.')
"""
Задача 6
«Лютики и другие цветочки» отдали вам данные за всё время существования приложения. 
Теперь списки installs и payers хранят информацию о числе установок и заплативших пользователей за многие месяцы — 
за сколько именно, вы не знаете.
Напишите цикл, который рассчитает конверсию по всем месяцам и сохранит результат в списке conversions, 
применяя функцию len(). Выведите этот список на экран.


Task 6.
"Buttercups and other flowers" gave you the data for the whole time of the app's existence. 
Now the "installs" and "payers" lists keep information about the number of installs and paid users for many months - 
for how many you don't know.
Write a loop that calculates conversions for all months and stores the result in the "conversions" list using the "len()" function. 
Print that list on the screen.
"""

installs = [5018, 4312, 4208, 3665, 3957, 4912, 5074, 5165, 4704, 4447, 4189, 4371, 4823, 4594, 4755, 4743, 5134, 4119, 4333, 4698, 4442, 4012, 4698, 5001, 4440, 4873, 4975, 3978, 3909, 4567, 4169, 5212, 4189, 4001, 3933, 3961, 3955, 4036, 4267, 5251, 5026, 4675, 4128, 4074, 4366, 5044, 4672, 4258]

payers = [75, 48, 65, 68, 74, 67, 71, 65, 90, 85, 79, 81, 87, 61, 73, 77, 76, 70, 79, 61, 63, 67, 89, 65, 73, 71, 78, 73, 61, 85, 62, 86, 80, 79, 68, 76, 87, 85, 71, 65, 75, 70, 61, 83, 65, 86, 61, 71]

# создайте список conversions
conversions = []
# напишите цикл
for item in range(len(payers)):
    conversion_rate = payers[item] / installs[item]
    conversions.append(conversion_rate)
print(conversions)
# выведите conversions на экран

print('Task 7.')
"""
Задача 7
Узнайте, сколько всего денег «Лютики и другие цветочки» заработали на покупках приложения пользователями. 
Посчитайте доходы за каждый месяц и сохраните полученные значения в отдельный список, а затем сложите их и выведите результат на экран.
Список payers хранит помесячное количество заплативших пользователей, а purchase_amount — цену приложения в долларах.

Task 7.
Find out how much money Buttercups and Other Flowers made from users' purchases of the application. 
Count the income for each month and save the values to a separate list, then add them up and display the result.
The "payers" list stores the monthly number of users who paid, and "purchase_amount" stores the price of the app in dollars.
"""

payers = [75, 48, 65, 68, 74, 67, 71, 65, 90, 85, 79, 81, 87, 61, 73, 77, 76, 70, 79, 61, 63, 67, 89, 65, 73, 71, 78, 73, 61, 85, 62, 86, 80, 79, 68, 76, 87, 85, 71, 65, 75, 70, 61, 83, 65, 86, 61, 71]
purchase_amount = 5
payers_all = []
for item in range(len(payers)):
    payers_list = payers[item] * purchase_amount
    payers_all.append(payers_list)
print(sum(payers_all))

print('Task 8.')
"""
Задача 8
Теперь рассчитайте среднемесячный доход «Лютиков и других цветочков». 
Результат сохраните в переменной average_income и выведите на экран.

Task 8.
Now calculate the average monthly income of "Buttercups and other flowers". 
Save the result in the variable "average_income" and display it on the screen.
"""
payers = [75, 48, 65, 68, 74, 67, 71, 65, 90, 85, 79, 81, 87, 61, 73, 77, 76, 70, 79, 61, 63, 67, 89, 65, 73, 71, 78, 73, 61, 85, 62, 86, 80, 79, 68, 76, 87, 85, 71, 65, 75, 70, 61, 83, 65, 86, 61, 71]
purchase_amount = 5

# create a list
payers_all = []
# write a loop
for item in range(len(payers)):
    payers_list = payers[item] * purchase_amount
    payers_all.append(payers_list)

# find the sum
# divide the sum by the number of elements
average_income = sum(payers_all) / len(payers)


print(average_income)  # print the average on the screen


