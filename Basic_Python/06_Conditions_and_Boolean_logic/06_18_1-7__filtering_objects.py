"""Фильтрация объектов
После изучения датасета список критериев немного изменился.
Теперь он включает в себя не только этаж, площадь, расположение, стоимость аренды и количество конкурентов поблизости,
но также назначение помещения и его доступность для аренды.

Список критериев
    floor — 1,
    area — не меньше 40 м²,
    price — не больше 190 000 ₽,
    commercial_type — FREE_PURPOSE либо RETAIL,
    distance — не больше 6.7 км,
    already_taken — 0,
    competitors — не больше 1.

Чтобы получить список формально подходящих помещений для нового магазина, вам предстоит отфильтровать весь датасет.
Это можно сделать в три шага
    Написать программу для проверки одного объекта;
    Обобщить код, чтобы проверить сразу все объекты;
    Сохранить результаты в новый список.
"""

print('     Task 1/7')
"""
1/7.
Проверьте, соответствует ли первый объект требованию «помещение на первом этаже» — 
то есть равно ли значение столбца floor в первой строке единице.
Столбцы датасета работают как списки, поэтому обратиться к первому элементу можно по индексу: 
realty_df['floor'][0].
"""
import pandas

realty_df = pandas.read_csv('yandex_realty_data.csv')

# напишите условие в скобках print()
print(realty_df['floor'][0] == 1)

print('     Task 2/7')
"""
2/7.
Напишите остальные проверки для первого объекта. 
Если объявление не соответствует критериям, сравнение должно вернуть False.
Проверки поместите в скобках функции print().
"""

realty_df = pandas.read_csv('yandex_realty_data.csv')

# первый этаж
print(realty_df['floor'][0] == 1)

# area — не меньше 40
print(realty_df['area'][0] >= 40)

# price — не больше 190000
print(realty_df['price'][0] <= 190000)

# commercial_type — либо FREE_PURPOSE, либо RETAIL
print((realty_df['commercial_type'][0] == 'FREE_PURPOSE') or (realty_df['commercial_type'][0] == 'RETAIL'))

# distance не больше 6.7
print(realty_df['distance'][0] <= 6.7)

# already_taken равен 0
print(realty_df['already_taken'][0] == 0)

# competitors – не больше 1
print(realty_df['competitors'][0] <= 1)

print('     Task 3/7')
"""
3/7.
Теперь научите программу работать с любым объектом, а не только с первым. 
Перепишите код так, чтобы он брал индекс объекта из переменной index.
"""

realty_df = pandas.read_csv('yandex_realty_data.csv')

index = 5

# первый этаж
print(realty_df['floor'][index] == 1)

# площадь — не меньше 40 кв. м
print(realty_df['area'][index] >= 40)

# цена — не больше 190000
print(realty_df['price'][index] <= 190000)

# тип помещения — либо FREE_PURPOSE, либо RETAIL
print(realty_df['commercial_type'][index] in ['FREE_PURPOSE', 'RETAIL'])

# расстояние от центра — не больше 6.7 км
print(realty_df['distance'][index] <= 6.7)

# помещение не занято, already_taken равно 0
print(realty_df['already_taken'][index] == 0)

# не больше одного конкурента поблизости
print(realty_df['competitors'][index] <= 1)

print('     Task 4/7')
"""
4/7.
Ваш код поочерёдно проверяет объект по каждому критерию. 
Но Филу подойдут только те объекты, которые соответствуют сразу всем условиям:
"""

realty_df = pandas.read_csv('yandex_realty_data.csv')

index = 5
# проверьте соответствие всем условиям сразу
print((realty_df['floor'][index] == 1 and
       realty_df['area'][index] >= 40 and
       realty_df['price'][index] <= 190000 and
       realty_df['commercial_type'][index] in ['FREE_PURPOSE', 'RETAIL'] and
       realty_df['distance'][index] <= 6.7 and
       realty_df['already_taken'][index] == 0 and
       realty_df['competitors'][index] <= 1))

print('     Task 5/7')
"""
5/7.
Если «обернуть» проверку условий в конструкцию if, вы сможете выполнять разные действия в зависимости от того, подходит ли объект по всем критериям.
Напишите код, который выводит на экран сообщение 'Объект подходит', если все условия верны, и 'Объект не подходит' — в обратном случае.
"""

realty_df = pandas.read_csv('yandex_realty_data.csv')

index = 3  # проверим другой объект

# замените print() конструкцией if-else
if (realty_df['floor'][index] == 1 and
    realty_df['area'][index] >= 40 and
    realty_df['price'][index] <= 190000 and
    realty_df['commercial_type'][index] in ['FREE_PURPOSE', 'RETAIL'] and
    realty_df['distance'][index] <= 6.7 and
    realty_df['already_taken'][index] == 0 and
    realty_df['competitors'][index] <= 1) == True:
    print('Объект подходит')
else:
    print('Объект не подходит')

print('     Task 6/7')
"""
6/7.
Сохранять сразу всю информацию о подходящих помещениях из датасета, включая этажность и год постройки здания, смысла нет. 
Для прогнозирования прибыльности магазина и принятия решения об аренде достаточно будет данных из четырёх столбцов:
    area — площадь,
    price — цена,
    traffic — проходимость,
    address — адрес.
Мы создали список для каждого из этих параметров. 
Допишите программу, чтобы при выполнении всех условий она пополняла списки соответствующими данными.
"""

realty_df = pandas.read_csv('yandex_realty_data.csv')

# списки для важных параметров
filtered_objects_area = []
filtered_objects_price = []
filtered_objects_traffic = []
filtered_objects_address = []

index = 3  # это объявление соответствует всем требованиям

if (realty_df['floor'][index] == 1 and
        realty_df['area'][index] >= 40 and
        realty_df['price'][index] <= 190000 and
        realty_df['commercial_type'][index] in ['FREE_PURPOSE', 'RETAIL'] and
        realty_df['distance'][index] <= 6.7 and
        realty_df['already_taken'][index] == 0 and
        realty_df['competitors'][index] <= 1):
    # пополните список filtered_objects_area
    filtered_objects_area.append(realty_df['area'][index])
    # пополните список filtered_objects_price
    filtered_objects_price.append(realty_df['price'][index])
    # пополните список filtered_objects_traffic
    filtered_objects_traffic.append(realty_df['traffic'][index])
    # пополните список filtered_objects_address
    filtered_objects_address.append(realty_df['address'][index])

print(filtered_objects_area,
      filtered_objects_price,
      filtered_objects_traffic,
      filtered_objects_address)  # выводим все списки на экран

print('     Task 7/7')
"""
7/7.
Последний шаг — пройти по всем объектам и проверить условия для каждого. 
Для этого «оберните» if циклом for с перебором по индексам.
"""

realty_df = pandas.read_csv('yandex_realty_data.csv')

filtered_objects_area = []
filtered_objects_price = []
filtered_objects_traffic = []
filtered_objects_address = []

# напишите цикл, который пройдёт по всем индексам датасета
for index in range(len(realty_df['address'])):
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

print(len(filtered_objects_area))  # узнаем, сколько объявлений сохранил фильтр
