# Easy
from random import choice


COUNT_OF_FUNC_LAUNCHES = 0


def sum_of_numbers(pos_one, pos_two, pos_three, pos_four, *args, **kwargs):
    global COUNT_OF_FUNC_LAUNCHES
    COUNT_OF_FUNC_LAUNCHES += 1
    random_num_kwargs = choice(list(kwargs.values()))
    return pos_one + pos_two + pos_three + pos_four \
        + sum(args[:2]) + random_num_kwargs


for i in range(5):
    print(
        sum_of_numbers(
                    1, 2, 3, 4,
                    5, 6, 7, 8,
                    named_one=10, named_two=20, named_three=30)
    )

print(COUNT_OF_FUNC_LAUNCHES)
