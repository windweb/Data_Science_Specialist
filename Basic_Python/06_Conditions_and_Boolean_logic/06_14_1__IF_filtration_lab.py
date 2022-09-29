print('     Task_1')
"""
Задача 1
Список visitors_age хранит возраст посетителей на входе в парк экстремальных развлечений.
Проследите, чтобы в парк попали только совершеннолетние.
Cоздайте список entrance_allowed и добавьте в него все числа от 18 и больше из списка visitors_age.
"""

visitors_age = [17, 10, 96, 30, 18, 82, 13, 84, 15, 41]

# создайте пустой список entrance_allowed
entrance_allowed = []
# пройдите циклом for по исходному списку
# проверьте, что число больше или равно 18
# если это так – положите его в список entrance_allowed
for age in visitors_age:
    if age >= 18:
        entrance_allowed.append(age)

print(entrance_allowed)


print('     Task_2')
"""
Задача 2
Посчитайте, сколько человек в итоге попадёт в парк.
Это не совсем фильтр: создавать новый список с отфильтрованными элементами не придётся. 
Вместо этого — увеличивайте значение переменной counter на 1 каждый раз, когда выполняется условие. 
Без цикла и if здесь всё равно не обойтись.
"""

visitors_age = [17, 10, 96, 30, 18, 82, 13, 84, 15, 41]

counter = 0

# ваш код здесь
for age in visitors_age:
    if age >= 18:
        counter += 1

print(counter)

print('     Task_3')
"""
Задача 3
Робот на складе крупного интернет-ритейлера собирает заказы. 
Помогите ему — добавьте в список order все элементы из списка storage, кроме подводной лодки.
"""

storage = ['коробка печенья', 'подводная лодка', 'краски', 'горшок для цветка', 'отвёртка', 'музыкальная пластинка', 'блокнот']

order = []

# ваш код здесь
for item in storage:
    if item != 'подводная лодка':
        order.append(item)

print(order)

print('     Task_4')
"""
Задача 4
Список julia_songs хранит уникальные идентификаторы песен, которым Юля поставила лайк в музыкальном сервисе. 
Список mary_songs — песен, которые понравились Маше.
Создайте плейлист, который понравится им обеим. 
Добавьте в список mary_julia_songs элементы, которые есть в обоих списках.
"""

julia_songs = [145678, 297863, 966387, 374981, 746397, 197638]
mary_songs = [576093, 197638, 736901, 297863, 374981, 871532]

mary_julia_songs = []

# ваш код здесь
for index in range(len(julia_songs)):
    if julia_songs[index] in mary_songs:
        mary_julia_songs.append(julia_songs[index])

print(mary_julia_songs)

print('     Task_5')
"""
Задача 5
В списке yellow_submarine_chorus некоторые значения повторяются.
Создайте список yellow_submarine_briefly, 
в котором каждый элемент исходного списка встречается только раз.
"""

yellow_submarine_chorus = ['we', 'all', 'live', 'in', 'a', 'yellow', 'submarine', 'yellow', 'submarine', 'yellow', 'submarine', 'we', 'all', 'live', 'in', 'a', 'yellow', 'submarine', 'yellow', 'submarine', 'yellow', 'submarine']

yellow_submarine_briefly = []

# ваш код здесь
for index in range(len(yellow_submarine_chorus)):
    if yellow_submarine_chorus[index] not in yellow_submarine_briefly:
        yellow_submarine_briefly.append(yellow_submarine_chorus[index])

print(yellow_submarine_briefly)

print('     Task_6')
"""
Задача 6
Робот в службе поддержки повышает приоритет всех обращений, на которые не было ответа больше 10 часов. 
Количество часов, прошедших со времени поступления каждой заявки, лежит в списке hours_passed.
Определите номера обращений, приоритет по которым следует повысить — если значение в hours_passed больше 10, 
сохраните его индекс в список high_priority.
"""
hours_passed = [9, 12, 8, 24, 35, 0, 15, 28]

high_priority = []

# ваш код здесь
for index in range(len(hours_passed)):
    if hours_passed[index] >= 10:
        high_priority.append(index)
print(high_priority)
# Зная индексы отфильтрованных элементов, с этими элементами можно совершать различные действия.
# Например, выводить на экран:
# for index in high_priority:
#     print(hours_passed[index])

print('     Task_7')
"""
Задача 7
Два списка описывают объекты недвижимости:
    prices — стоимость аренды в долларах,
    addresses — адреса помещений.
То есть аренда объекта по адресу addresses[index] стоит prices[index]. 
Составьте список адресов объектов, арендная ставка которых ниже 1000 долларов.
"""

prices = [1100, 999, 1000000, 80, 40000]
addresses = ['Россия, Москва, Берсеневская набережная, 6с1',
             'Россия, Москва, Болотная набережная, 11с1',
             'Россия, Москва, Романов переулок, 4',
             'Россия, Москва, Старая Басманная улица, 20к1',
             'Россия, Москва, Волгоградский проспект, 32к8']

addresses_with_low_price = []

# ваш код здесь
for index in range(len(prices)):
    if prices[index] < 1000:
        addresses_with_low_price.append(addresses[index])

print(addresses_with_low_price)

print('     Task_8')
"""
Задача 8
Теперь объект недвижимости описывают уже четыре списка:
    prices — цена,
    floors — этаж,
    distances — расстояние до центра города в километрах,
    addresses — адрес.
Создайте списки prices_filtered , floors_filtered, distances_filtered, addresses_filtered. 
С помощью фильтра найдите все объекты на первом этаже не дальше 15 км от центра города по ставке менее 1000 долларов. 
Объекты, которые находятся на расстоянии 15 км ровно, тоже нужно включить.
Сохраните данные о таких объектах: 
    цену — в prices_filtered, 
    этаж — во floors_filtered, 
    расстояние до центра — в distances_filtered, 
    адрес — в addresses_filtered.
"""

prices = [1100, 999, 80, 80, 40000]
floors = [10, 1, 1, 4, 30]
distances = [10, 3, 15, 31, 37]
addresses = ['Россия, Москва, Берсеневская набережная, 6с1',
					   'Россия, Москва, Болотная набережная, 11с1',
						 'Россия, Москва, Романов переулок, 4',
						 'Россия, Москва, Старая Басманная улица, 20к1',
						 'Россия, Москва, Волгоградский проспект, 32к8']

prices_filtered = []
floors_filtered = []
distances_filtered = []
addresses_filtered = []


for index in range(len(prices)):
    if (prices[index] < 1000 and
            floors[index] == 1 and
            distances[index] <= 15):  # напишите составное условие
        prices_filtered.append(prices[index])
        # напишите ваш код здесь
        floors_filtered.append(floors[index])
        distances_filtered.append(distances[index])
        addresses_filtered.append(addresses[index])

print(prices_filtered)
print(floors_filtered)
print(distances_filtered)
print(addresses_filtered)