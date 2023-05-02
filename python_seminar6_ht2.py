# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазон
# у (т.е. не меньше заданного минимума и не больше заданного
# максимума) 
 
def find_index(list: list, d: list) -> list:
    list_index = []
    for i in range(len(list)):
        if d[0] < list[i] < d[1]:
            list_index.append(i)
    return list_index
massive = [int(num) for num in input('Введите элементы массива: ').split()]
diap = [int(p) for p in input('Введите диапазон: ').split()]
print (f'Индексы элементов, входящх в диапазон -> {find_index(massive, diap)}')    