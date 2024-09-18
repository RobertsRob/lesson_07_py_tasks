# 1.task
# Создайте кортеж с числами и найдите максимальное и минимальное значение.
numbers = (3, 8, 2, 10, 6)
max_value = max(numbers)
min_value = min(numbers)
print(max_value, min_value)

# 2.task
# Создайте множество с числами и добавьте в него новое число.
numbers_set = {1, 2, 3, 4}
numbers_set.add(5)
print(numbers_set)

# 3.task
# Создайте словарь с именами и возрастами, получите возраст одного человека "безопасно" по его имени.
people = {"Alice": 25, "Bob": 30, "Charlie": 22}
age = people.get("Bob")
print(age)

# 4.task
# Создайте два множества и найдите их пересечение.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
print(intersection)

# 5.task
# Создайте два множества и найдите их объединение.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)

# 6.task
# Создайте кортеж с числами и проверьте, являются ли все числа в кортеже положительными.
numbers = (3, 5, 8, 10)
all_positive = all(n > 0 for n in numbers)
print(all_positive)

# 7.task
# Создайте кортеж с числами и найдите индекс числа 7.
numbers = (1, 3, 7, 9, 7, 11)
index_of_seven = numbers.index(7)
print(index_of_seven)

# 8.task
# Создайте словарь с именами студентов и их оценками. Найдите среднюю оценку.
students = {"Alice": 85, "Bob": 90, "Charlie": 88}
average_grade = sum(students.values()) / len(students)
print(average_grade)

# 9.task
# Создайте множество чисел и удалите из него все чётные числа.
numbers_set = {1, 2, 3, 4, 5, 6, 7, 8}
numbers_set = {num for num in numbers_set if num % 2 != 0}
print(numbers_set)

# 10.task
# Создайте кортеж с числами и отсортируйте его по убыванию, удалив при этом дубликаты. Вывести надо кортеж.
numbers = (4, 7, 2, 7, 3, 9, 4)
unique_sorted_numbers = tuple(sorted(set(numbers), reverse=True))
print(unique_sorted_numbers)

# 11.task
# Создайте множество строк, оставьте только те строки, которые начинаются с гласной буквы.
words_set = {"apple", "banana", "orange", "grape", "avocado"}
vowels = {"a", "e", "i", "o", "u"}
filtered_set = {word for word in words_set if word[0].lower() in vowels}
print(filtered_set)

# 12.task
# Создайте кортеж с несколькими числами, проверьте, являются ли все числа в кортеже нечётными.
numbers = (1, 3, 5, 7, 9)
all_odd = all(num % 2 != 0 for num in numbers)
print(all_odd)

# 13.task *
# Создайте словарь с именами сотрудников и их заработной платой. Найдите сотрудников, чьи зарплаты выше среднего, и выведите их имена с процентной разницей относительно средней зарплаты.
employees = {"John": 50000, "Sara": 70000, "Mike": 55000, "Anna": 80000, "Tom": 45000}

average_salary = sum(employees.values()) / len(employees)
above_average = {}

for name, salary in employees.items():
    if salary > average_salary:
        percentage_difference = ((salary - average_salary) / average_salary) * 100
        above_average[name] = percentage_difference

print(f"Средняя зарплата: {average_salary}")
for name, diff in above_average.items():
    print(f"{name} получает на {diff:.2f}% больше средней зарплаты.")

# 14.task *
# Создайте словарь, где ключами будут имена студентов, а значениями — их оценки за несколько предметов (список). Посчитайте среднюю оценку каждого студента и выведите имена студентов, у которых средняя оценка выше 70.
students = {
    "Alice": [85, 90, 78],
    "Bob": [60, 65, 70],
    "Charlie": [90, 92, 88],
    "Dave": [50, 55, 60]
}

above_average_students = {}

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade > 70:
        above_average_students[name] = average_grade

for name, avg_grade in above_average_students.items():
    print(f"{name} имеет среднюю оценку {avg_grade:.2f}, что выше 70.")
