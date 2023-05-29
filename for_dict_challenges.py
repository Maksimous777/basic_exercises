from collections import Counter
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

print('Задание 1')
qty_students = (Counter(student['first_name'] for student in students))
for student in qty_students:
    print(f'{student}: {qty_students[student]}')
print()


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

print('Задание 2')
most_common_student = Counter(student['first_name']
                              for student in students).most_common(1)
print(
    f'Самое частое имя среди учеников: {most_common_student[0][0]}\n')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

print('Задание 3')
for grade in range(len(school_students)):
    max_students = Counter(student['first_name']
                           for student in school_students[grade]).most_common(1)
    print(
        f'Самое частое имя в классе {grade + 1}: {max_students[0][0]}')
print()

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [
        {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [
        {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {
        'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
print('Задание 4')
for grade in school:
    male = 0
    female = 0
    for student in grade['students']:
        if is_male[student['first_name']]:
            male += 1
        else:
            female += 1
    print(
        f"Класс {grade['class']}: девочки {female}, мальчики {male}")
print()
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [
        {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [
        {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
print('Задание 5')
male = []
female = []
for grade in range(len(school)):
    male.append(0)
    female.append(0)
    for student in school[grade]['students']:
        if is_male[student['first_name']]:
            male[grade] += 1
        else:
            female[grade] += 1

most_male = school[male.index(max(male))]['class']
most_female = school[female.index(max(female))]['class']
print(
    f"Больше всего мальчиков в классе {most_male}")
print(
    f"Больше всего девочек в классе {most_female}")
