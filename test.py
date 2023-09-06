# a = None

# if a is None:
#     print("Переменная a пустая!")
# else:
#     print("В переменной a что-то есть!")

# ----------------------------------------------

# first = int(input("Введите первое число: "))
# second = int(input("Введите второе число: "))

# answer = (first*first)/second

# print(int(answer))

# ----------------------------------------------

a,b,c = map(float, input().split())
stroka = input()
print()
print(
    f"{a}, {b}, {c}",
    a+b+c, 
    a**b**c,
    stroka,
    sep="\n"
)