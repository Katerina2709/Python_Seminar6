# Задача 30. Заполните массив элементами арифметической про
# грессии. Её первый элемент, разность и кол
# ичество элементов нужно 
# ввести с клавиатуры. Формула для получения n-го
# члена прогрессии: 
#        an = a1 + (n-1) * d.
# Каждое число вводится с новой ст
 
def arithmetic(a, d, n):
    list = [a]
    for i in range(1,n):
        list.append(a + i*d)
    return list
num1 = int(input('Введите первое число арифметической прогрессии: '))
dif = int(input('Введите разность арифметической прогрессии:  ')) 
kol = int(input('Введите количество членов арифметической прогрессии: '))
print (arithmetic(num1, dif, kol))    