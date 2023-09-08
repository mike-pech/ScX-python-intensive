alphabet: dict[int|float|str|tuple|dict|None] = {
    1: 'A',
    2: 'B',
    3: 'C',         # Ключами могут быть лишь неизменяемые (то есть хэшируемые) типы данных: строки, кортежи, инты и т.д.
    4: 'D',
    'Z': "Last",
    1.1: "AAAAA",
    (1, 2, 3): 123,
    'bin': {
        1: 0x01,
        2: 0x10,
        3: 0x11,
    },
    None: 0,
}
# for pair in alphabet:
#     print(pair)                 # Возвращает НЕ ПАРЫ, а просто ключи, лол

# for key, value in alphabet.items():     # .keys() .values()
#     print(f"Ключ: Значение \n{key}   :   {value}")          #   Распаковка словарей

# letter = alphabet.get(1.2, 'Не нашёл')
# print(letter)

# binary = alphabet.get('bin', None)
# for value in binary().values():
#     print(value)

for_class_a = {
    'A': 1,
    'B': 2,
    'C': 3,
}

class A:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.key = value

a = A(**for_class_a)
print(a.key)