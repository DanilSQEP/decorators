# Medium 2-4
from random import choice

COUNT_RUN_SUM_OF_NUMBERS = 0
COUNT_RUN_MULTIPLY_OF_NUMBERS = 0
COUNT_RUN_DIFFERENCE_OF_NUMBERS = 0
COUNT_RUN_PRINT_POT_IS_ALIVE = 0


def wrapped():
    def sum_of_numbers(pos_one, pos_two, pos_three, pos_four, *args, **kwargs):
        global COUNT_RUN_SUM_OF_NUMBERS
        COUNT_RUN_SUM_OF_NUMBERS += 1
        random_num_kwargs = choice(list(kwargs.values()))
        return pos_one + pos_two + pos_three + pos_four \
            + sum(args[:2]) + random_num_kwargs
    return sum_of_numbers


def multiply_of_num(a, b):
    global COUNT_RUN_MULTIPLY_OF_NUMBERS
    COUNT_RUN_MULTIPLY_OF_NUMBERS += 1
    return a * b


def difference_of_num(a, b):
    global COUNT_RUN_DIFFERENCE_OF_NUMBERS
    COUNT_RUN_DIFFERENCE_OF_NUMBERS += 1
    return a - b


def print_pot_is_alive():
    global COUNT_RUN_PRINT_POT_IS_ALIVE
    COUNT_RUN_PRINT_POT_IS_ALIVE += 1
    print("ГОРШОК ЖИВ! РОЦК")


# for i in range(5):
#     sum_of_numbers(
#                 1, 2, 3, 4,
#                 5, 6, 7, 8,
#                 named_one=10, named_two=20, named_three=30)
#     multiply_of_num(2, 3)
#     difference_of_num(2, 3)
#     print_pot_is_alive()

result_run_wrapped = wrapped()
print(result_run_wrapped)

'''
Будет выведено <function sum_of_numbers.<locals>.inner at 0x7f0aaa607d00>
Адрес функции, которая была объявлена внутри функции wrapped
Произойдёт замыкание функции sum_of_numbers

'''

print(
    result_run_wrapped(
                1, 2, 3, 4,
                5, 6, 7, 8,
                named_one=10, named_two=20, named_three=30)
    )  # Будет работать как и раньше, без обёртки :)
