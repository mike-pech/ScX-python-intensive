n = int(input("Введите число: \n"))

def guess_root(number: int) -> int | str:
    for guess in range(number+1):
        if number == guess**2:
            return guess
    return None

print(guess_root(n) if guess_root(n) is not None else "Сложна, не могу")