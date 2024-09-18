# 1.task
# Используя lambda, сложите два числа.
sum_two = lambda x, y: x + y
result = sum_two(5, 7)
print(result)

# 2.task
# Используя lambda, найдите максимальное из двух чисел.
max_of_two = lambda x, y: x if x > y else y
result = max_of_two(10, 15)
print(result)

# 3.task
# Используя lambda, проверьте, является ли число чётным.
is_even = lambda x: x % 2 == 0
result = is_even(8)
print(result)

# 4.task
# Используя lambda, соедините два слова в одну строку.
concat = lambda x, y: x + " " + y
result = concat("Hello", "World")
print(result)

# 5.task
# Используя lambda, преобразуйте список чисел в строки.
numbers = [1, 2, 3, 4, 5]
to_string = lambda x: str(x)
string_numbers = [to_string(num) for num in numbers]
print(string_numbers)
