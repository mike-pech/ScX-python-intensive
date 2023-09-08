# Это константа. Написана КАПСОМ на snake_case
AGE_OF_CONSENT = 16

# Всё должно быть функциями

def do(stuff: str) -> str:
    return 'something'

AGE_OF_CONSENT += 1         # Почему-то работает, лол

a = 21                      # просто переменная на уровне высоком уровне

if __name__ == '__main__':
    a = 12
    do(stuff=str(AGE_OF_CONSENT))