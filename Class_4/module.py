def greet(name):
    return f"Hello, {name}!"

y = 'stroka'

if __name__ == '__main__':          # Dunder -- double under
    # print('cho-to-to')              # Allows you to border the inner methods of the file from usage out of it (as an external module)
    x = 42
    print("Locals:")
    print("y exists in locals" if 'y' in locals() else "Nope.")     # Проверка на существование локальной переменной