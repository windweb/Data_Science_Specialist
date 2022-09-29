# Цикл с перебором индексов

# Вы научились писать циклы, в которых переменная цикла поочерёдно принимает значения из определённого списка:
print("VARIANT 1")

islands = ['Тенерифе', 'Мадейра', 'Бали', 'Бора-Бора', 'Галапагос', 'Куба']

for value in islands:
    print(value)
"""
Тенерифе
Мадейра
Бали
Бора-Бора
Галапагос
Куба 
"""
print()
# Это популярный и действенный способ, но есть и другой.
# Чтобы пройти по всем элементам списка и выполнить с ними какие-нибудь операции, можно обращаться к ним по индексам.
# Такой код эквивалентен программе выше:
print()
print("VARIANT 2")
islands = ['Тенерифе', 'Мадейра', 'Бали', 'Бора-Бора', 'Галапагос', 'Куба']

for index in [0, 1, 2, 3, 4, 5]:
    print(islands[index])
"""
Тенерифе
Мадейра
Бали
Бора-Бора
Галапагос
Куба 
"""
print()
# Переменная цикла принимает значения из нового списка — он хранит числа от 0 до 5:
for index in [0, 1, 2, 3, 4, 5]:
    print(index)
"""
0
1
2
3
4
5 
"""
islands = ['Тенерифе', 'Мадейра', 'Бали', 'Бора-Бора', 'Галапагос', 'Куба']
#                          ^          ^         ^          ^            ^         ^
#                          0          1         2          3            4         5

"""
Так в теле цикла поочерёдно происходит обращение к каждому элементу islands через переменную цикла: 
islands[index] — это сначала islands[0], 
то есть 'Тенерифе', затем islands[1], то есть 'Мадейра', 
и так далее вплоть до элемента islands[5], который соответствует значению 'Куба'.
"""

"""
Допустим, вы хотите пройти сразу по двум спискам и сложить их элементы попарно, всякий раз выводя сумму на экран. 
Не прибегая к индексам, сделать это будет сложно, ведь переменная цикла может принимать только одно значение за раз:
"""
first_list = [9, 18, 27, 36, 45, 54, 63, 72, 81]
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ответ
for index in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
    print(first_list[index] + second_list[index])