# new_name: str = input("Input name: \n")
# greetings: str = "hello, bob"

# print(greetings)

# greetings: str = (
#     greetings[:-3] + new_name       # Удаляем "bob" при помощи слайсинга, и конкатенируем с другой строкой
# )

# print(greetings)
# new_name: str = input("Input another name: \n")

# greetings: str = \
#     greetings.replace("bob", new_name)

# print(greetings)

# river: str = 'mmmmmississippi'

# print(river.lstrip('misp'))         # Осторожно! Удаляет все инстанции перечисленных символов вплоть до символов, которые не встречаются в аргументах

# comment: str = '<!---dsa dsa das---!>'

# print(comment.strip("<>!-").split())        # Если надо разделить строчку на слова, предварительно избавившись от ненужных символов слева и справа

# PEP8 improting
import string       # Native Python libraries
                    # !!! --- Mind the spacing --- !!!
# import pip        # Downloadable libraries

# import local      # local APIs

# numbers:  str = string.digits    # Строка numbers состоит из чисел десятичной системы
# sentence: str = 'hel321lo b123ob, h1231ow a2re y321ou _0123456789_'

# for number in numbers:
#     sentence = sentence.replace(number, '')

# print(sentence)

# sentence = "Hello Bob! Are you bob? BOB!!!"
# sentence = sentence.lower()

# while True:
#     bob_index = sentence.find("bob")
#     if bob_index == -1:
#         break
#     else:
#         sentence = (sentence[:bob_index] + "Gregory" + sentence[bob_index + len("bob"):])
#         print(sentence)

_list: list = [1,2,3]
_srting: str = "1,2,3"
_tuple: tuple = (1,2,3)

_list[-1] = 5

print(_list, _srting, _tuple)

changing_tuple = (
    [1, 2],
    [2, 3],
    [3, 4],
)

changing_tuple[1][1] = 5        # так как кортежи хранят внутри себя ссылки на дргугие объекты а не сами объекты, мы можем поменять такие объяекты

print(changing_tuple)