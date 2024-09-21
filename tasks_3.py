# 1.task
# Умножьте все элементы списка на 3.
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 3, numbers))
print(result)

# 2.task
# Преобразуйте все строки в списке в верхний регистр.
strings = ["hello", "world", "python"]
result = list(map(lambda s: s.upper(), strings))
print(result)

# 3.task
# Сложите соответствующие элементы двух списков.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))
print(result)

# 4.task
# Создайте список, где каждое число является результатом возведения 2 в степень этого числа.
numbers = [0, 1, 2, 3, 4]
result = list(map(lambda x: 2 ** x, numbers))
print(result)

# 5.task
# Создайте список словарей, где каждый словарь содержит числовое значение и его квадрат. Примените map для создания списка этих словарей из списка чисел.
numbers = [1, 2, 3, 4, 5]
create_dict = lambda x: {'number': x, 'square': x ** 2}
result = list(map(create_dict, numbers))
print(result)

# 6.task
# Создайте список кортежей, где каждый кортеж содержит строку и её длину из списка со стоками. Используйте map для создания этого списка из списка строк.
strings = ["apple", "banana", "cherry"]
get_length_tuple = lambda s: (s, len(s))
result = list(map(get_length_tuple, strings))
print(result)
