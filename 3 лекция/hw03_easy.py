# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
fruits = ["яблоко", "банан", "киви", "арбуз"]
a = len(fruits)
for i in range(a):
    print(str(i + 1) + '{:>15}'.format(fruits[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
b = {'a', 'b', 'c', 'c', 'a', 'e'}
d = {'a', 'b', 'c', 'd'}
c = b - d
print(list(c))


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

my_list = [2, 7, 5, 6, 9, 15]
new_list = []
for i in my_list:
    if i % 2 == 0:
        new_list.append(i / 4)
    else:
        new_list.append(i * 2)
print(new_list)