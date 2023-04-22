# Medium
def sum_of_numbers(summand_one, summand_two,
                   summand_three, summand_four, *args):
    return summand_one + summand_two + summand_three + summand_four + sum(args)


print(sum_of_numbers(1, 2, 3, 4, 5, 5, 5, 5))  # сработает :)

# print(sum_of_numbers(1))

"""
Если в функцию прокинуть только 1 аргумент, то падаем с ошибкой,
так как позицонные аргументы надо передавать обязательно

"""

# print(sum_of_numbers(1, 2, 3, 4, summand_one=1))

"""
Если в функцию прокинуть только аргумент позиционно и по ключу,
то падаем с ошибкой, так как аргумент не может принять несколько значений

"""

# tuple_for_example = tuple(range(1, 11))
# print(sum_of_numbers(*tuple_for_example))

"""
Если в функцию прокинуть только распаковку кортежа,
то каждый позиционный аргумент примет своё значение,
а остальные уйдут в args.

Если прокинуть в функции кортеж с числом элементов меньше числа
позиционных аргументов в функции, то упадём с ошибкой

"""

dct_for_example = {
    "summand_one": 1,
    "summand_two": 2,
    "summand_three": 3,
    "summand_four": 4,
}

# print(sum_of_numbers(*dct_for_example))

"""
В данном случае упадём с ошибкой, нельзя распаковать словарь оператором
упаковки/распаковки iterable object

"""
# print(sum_of_numbers(**dct_for_example))

"""
В данном случае код выполнится, данный оператор как раз сущесвтует для
упаковки и распаковки словарей
Само собой, только если имя ключа словаря будет совпадать
с именем позиционного аргумента

"""
