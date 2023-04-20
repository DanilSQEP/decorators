# Easy
def multiplying_the_row(row, multiplication):
    multiplied_row = ""
    while multiplication != 0:
        if multiplication % 2 == 0:
            multiplied_row += row.upper()
        else:
            multiplied_row += row
        multiplication -= 1
    return multiplied_row


a = multiplying_the_row
print(a)

"""
Если в переменную записать функцию без вызова, то
на экран выведется результат того, что теперь переменная
является функцией и её адрес

"""

print(a('test', 3))
