"""
Модель предсказания

На этапе уточнения вы сформулировали задачу так: «Определить, что даст более точный прогноз объёма урожая: предсказание площади посевов или урожайности».
Объём урожая (production) за определённый год (t) вычисляется как площадь засеянных в этом году полей (acres) умножить на урожайность (yield) за тот же год:

production_t = acres_t * yield_t

Самый точный прогноз получится, если предсказать и площадь посевов, и урожайность. Однако Герман может предсказать только один фактор, а второй планирует взять из данных за предыдущий год. Значит, есть две стратегии:
    1 - Предсказать площадь посевов, а урожайность взять за предыдущий год;
    2 - Предсказать урожайность, а площадь посевов взять за предыдущий год.

Какая даст более точный прогноз урожая? Ответив на этот вопрос, вы решите задачу.


Эффективность двух стратегий можно проверить на исторических данных из датасета:
«предсказать» объём урожая для каждого года и сравнить с реальными показателями.
Для простоты предположим, что Герман сможет в обоих случаях сделать идеальное предсказание.
Тогда если выбрать первый вариант — предсказать площадь посевов, а урожайность взять за предыдущий год, —
предсказанный объём урожая за определённый год будет равен
произведению реальной площади посевов (acres) за этот год (t) и прошлогодней урожайности (yield, t-1):

acres_t * yield_{t-1}

А во втором случае наоборот — произведению прошлогодней площади посевов и реальной урожайности за выбранный год:

acres_{t-1} * yield_t


Для 1980 года не получится сделать предсказания (В датасете представлены данные с 1980-го по 2019 год.)*
*Нет данных за предыдущий год — нечего подставить в формулу. Поэтому предсказаний будет не 40, а 39.
"""
print('     Task_1')
"""
1
Предскажите объёмы урожая по первой стратегии: 
умножьте площадь посевов за каждый год, кроме 1980-го, на урожайность за предыдущий год. 
Результат сохраните в список predict_acres и выведите его на экран.

"""
import pandas
data = pandas.read_csv('crops_usa.csv')

acres = list(data['Acres'])
production = list(data['Production'])
years = list(data['Year'])

acres_usa = []
production_usa = []

for year in range(1980, 2020):
    acres_one_year = []
    production_one_year = []
    for index in range(len(data)):
        if years[index] == year:
            acres_one_year.append(acres[index])
            production_one_year.append(production[index])
    acres_usa.append(sum(acres_one_year))
    production_usa.append(sum(production_one_year))

yield_usa = []

for index in range(len(production_usa)):
    yield_usa.append(production_usa[index] / acres_usa[index])

# ваш код здесь
predict_acres = []  # прогнозируем площадь посевов, а урожайность берем за предыдущий год;

for index in range(1, len(acres_usa)):
    predict_acres.append(acres_usa[index] * yield_usa[index - 1])

print(predict_acres)

"""
Результат
[2600878923.033124, 2721633803.8549137, 2450320219.5588646, 2508296608.330389, 2474296904.485375, 2310603452.3068776, 1911443825.2451458, 2098079727.2478693, 2118783738.7263656, 2047942143.6794362, 2476079184.044859, 2046388266.3528, 2465055983.383874, 2336037545.1723757, 2277497042.0475063, 2374763285.1907115, 2135083467.8916183, 2319669567.4884963, 2425142783.3670106, 2291347223.9244223, 2117124256.5029018, 1976485227.7224388, 1654412692.6953812, 2250209817.350863, 2068918634.9004092, 2107736490.1947074, 1907015581.679283, 2158188311.2140255, 2330266536.177437, 1969487862.1414168, 2231136438.0653744, 2030456355.9887247, 2290677767.0633345, 2157947601.874244, 1960645021.9032035, 1878872978.1268752, 2121449207.3589275, 1807556928.0378704, 1780401017.4213114]
"""
print('     Task_2')
"""
2
Теперь предскажите объёмы урожая, придерживаясь второй стратегии, — 
умножьте урожайность за каждый год, кроме 1980-го, на площадь посевов за предыдущий год. 
Результат сохраните в список predict_yield.
"""
# ваш код здесь
predict_yield = []  # прогнозируем урожайность, а площадь посевов берем за предыдущий год.

for index in range(1, len(acres_usa)):
    predict_yield.append(acres_usa[index - 1] * yield_usa[index])


print(predict_acres)
print(predict_yield)

"""
Результат
[2600878923.033124, 2721633803.8549137, 2450320219.5588646, 2508296608.330389, 2474296904.485375, 2310603452.3068776, 1911443825.2451458, 2098079727.2478693, 2118783738.7263656, 2047942143.6794362, 2476079184.044859, 2046388266.3528, 2465055983.383874, 2336037545.1723757, 2277497042.0475063, 2374763285.1907115, 2135083467.8916183, 2319669567.4884963, 2425142783.3670106, 2291347223.9244223, 2117124256.5029018, 1976485227.7224388, 1654412692.6953812, 2250209817.350863, 2068918634.9004092, 2107736490.1947074, 1907015581.679283, 2158188311.2140255, 2330266536.177437, 1969487862.1414168, 2231136438.0653744, 2030456355.9887247, 2290677767.0633345, 2157947601.874244, 1960645021.9032035, 1878872978.1268752, 2121449207.3589275, 1807556928.0378704, 1780401017.4213114]
[2549811575.1209617, 2829704781.484832, 2730554746.437404, 2503254056.316514, 2542151605.1499305, 2193272104.0862246, 2305201425.359644, 1820497483.9994507, 1741924439.3656595, 2714683629.1065793, 2183023836.2215767, 2386938493.1666183, 2398133526.770868, 2380994140.755377, 2224382162.9702597, 2093207789.468078, 2646857125.6319942, 2724996068.914176, 2411209861.4834676, 2232256602.6635118, 2049590081.0506122, 1582289553.6324148, 2275638048.4704137, 2247084155.824559, 2192657676.4428287, 1804630987.26759, 1945039354.8130994, 2387242909.285254, 2381089116.796855, 2425981155.2831626, 1932264141.7174864, 2210881235.559012, 2099216317.4123337, 2004742512.6229305, 2130996467.1903126, 2533605162.7623916, 1894541943.020933, 1815647895.2629929, 2033115866.1809645]
"""