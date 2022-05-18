import time

'''Создадим новый список используя генератор списка'''

'''Добавляем условие для фильтрации'''
number = [1,2,3,4,5,6,7,8,9]
gen = [
    i
    for i in number
    if i % 2 == 0
    ]
print(gen)

'''Добавляем обработку элемента в выражении'''
number = [1,2,3,4,5,6,7,8,9]
gen = [i*2 for i in number if i % 2 == 0]
print(gen)

string = ['Nur', 'Bissenov', 'Murzabekovich']
gen = [len(i) for i in string]
print(gen)

'''Ветвление выражения'''
number = [1,2,3,4,5,6,7,8,9]
gen = [i if i < 0 else i ** 2 for i in number]
gen2 = [i if i < 0 else i ** 2 for i in number if i % 2 == 0]
gen3 = [[i if i < 0 else i ** 2] for i in number]

print('gen:->',gen)
print('gen2:->',gen2)
print('gen3:->',gen3)

'''Аналоги в виде цикла for и в виде функций'''
numbers = range(10)
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]
print(squared_evens)

'''Выражения-генераторы'''
'''выдают элемент по-одному, не загружая в память сразу всю коллекцию.'''
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_gen = (i for i in list_a) # выражение-генератор
my_gen2 = sum(i for i in list_a)
print(next(my_gen)) # -2 - получаем очередной элемент генератора
print(next(my_gen)) # -1 - получаем очередной элемент генератора
print(my_gen2)

'''Создание коллекций из выражения-генератора с помощью функций list(), tuple(), set(), frozenset()'''
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_list = list(i for i in list_a)
print(my_list)

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_list = tuple(i for i in list_a)
print(my_list)

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_list = set(i for i in list_a)
print(my_list)

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_list = frozenset(i for i in list_a)
print(my_list)


'''Генератор словаря (dictionary comprehension)
переворачивание словаря'''
dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
dict_abc2 = {'name': 'Nurbolat', 'surname': 'Bissenov', 'age': 29, 'city': 'almaty'}
dict_123 = {v: k for k, v in dict_abc.items()}
dict_info = {k: v for k, v in dict_abc2.items()}
print(dict_123)  # {1: 'a', 2: 'b', 3: 'd'}
print(dict_info)     # Обратите внимание, мы потеряли "с"! Так как значения были одинаковы,
                     # то когда они стали ключами, только последнее значение сохранилось.


'''Словарь из списка'''
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
dict_1 = dict((x, x ** 2) for x in list_a if x > 0)
dict_2 = {i: i * 2 for i in list_a if i > 0}
print(dict_1)
print(dict_2)

''' Генерация строк'''
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
# используем генератор прямо в .join() одновременно приводя элементы к строковому типу
str = ','.join(str(i ** 2) for i in list_a if i > 0)
print(str)

'''Периодичность и частичный перебор'''
'''выберем в генераторе списка каждый третий элемент из исходного списка:'''
time = time.time()
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
enumerate = [x for i,x in enumerate(list_a,1) if i % 3 == 0] #enumerate(iterator, start) — начинает считать с значения start.
                                                             # Удобно, например, если нам надо считать с 1, а не 0.

#enumerate = [(x,i) for i,x in enumerate(list_a,1) if i % 3 == 0] # Проиллюстрируем работу с индексами:
#enumerate_2 = [x for i,x in enumerate(list_a) if x % 3 == 0]
print(enumerate)
elapsed_time = time
print(elapsed_time)

def powers_of_two(n):
    return [2**x for x in range(n+1)]
print(powers_of_two(2))


n = int(input())
mass = []
for i in range(n):
    number = int(input())
    mass.append(number)
for a in mass:
    print(a)