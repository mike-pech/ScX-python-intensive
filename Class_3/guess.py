def my_personal_sum(x: int | float, y: int) -> int:     # Функция запрашивает x и y и возвращает целочисленное значение (это просто тайпхинтинг). x может быть как интом, так и флоатом.
    return x + y
print(my_personal_sum(8, 9))