# Hard
from random import choice

# def wrapped():
#     COUNT_RUN_SUM_OF_NUMBERS = 0
#     def sum_of_numbers(pos_one, pos_two, pos_three, pos_four, *args,
#                        **kwargs):
#         global COUNT_RUN_SUM_OF_NUMBERS
#         COUNT_RUN_SUM_OF_NUMBERS += 1
#         random_num_kwargs = choice(list(kwargs.values()))
#         return pos_one + pos_two + pos_three + pos_four \
#             + sum(args[:2]) + random_num_kwargs
#     return sum_of_numbers

# result_run_wrapped = wrapped()
# print(result_run_wrapped)

# print(
#     result_run_wrapped(
#                 1, 2, 3, 4,
#                 5, 6, 7, 8,
#                 named_one=10, named_two=20, named_three=30)
#     ) # Будет работать как и раньше, без обёртки :)

"""
Если перенести глобальный счётчик в функцию wrapped,то будем падать
с ошибкой NameError: name 'COUNT_RUN_SUM_OF_NUMBERS' is not defined

После внесения глобальной переменной в функцию, она стала локальной
для этой функции, поэтому global COUNT_RUN_SUM_OF_NUMBERS не может
найти её в глобальном пространстве имён
Исправим даунную ошибку, закомментируем предыдущйи код и напишем новый

"""


def wrapped():
    COUNT_RUN_SUM_OF_NUMBERS = 0

    def sum_of_numbers(pos_one, pos_two, pos_three, pos_four, *args, **kwargs):
        nonlocal COUNT_RUN_SUM_OF_NUMBERS
        COUNT_RUN_SUM_OF_NUMBERS += 1
        random_num_kwargs = choice(list(kwargs.values()))
        return pos_one + pos_two + pos_three + pos_four \
            + sum(args[:2]) + random_num_kwargs

    return sum_of_numbers


result_run_wrapped = wrapped()
print(result_run_wrapped)

for i in range(5):
    print(
        result_run_wrapped(
                    1, 2, 3, 4,
                    5, 6, 7, 8,
                    named_one=10, named_two=20, named_three=30)
        )

"""
Чтобы переменная была видна внутри обёрнутой функции,
нужно написать nonlocal COUNT_RUN_SUM_OF_NUMBERS
Теперь переменная COUNT_RUN_SUM_OF_NUMBERS создаст не новое
значение в своём локальном пространстве имён функции sum_of_numbers,
а возьмёт значение из оборачиваемой функции wrapped

"""
