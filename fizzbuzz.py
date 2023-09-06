def FizzBuzz(N):
    three = ((2*3 + 3*(N//3-1))/2)*(N//3)       # Формула суммы членов арифм. прогрессии: ((2*a1 + d*(n-1))/2)*n  
    five = ((2*5 + 5*(N//5-1))/2)*(N//5)        # N подгонятеся для каждого множества, т.к. каждый i-й член прогрессии от 1 до N делится на i
    fifteen = ((2*15 + 15*(N//15-1))/2)*(N//15)

    three -= fifteen
    five -= fifteen     # Удаляем пересечение из обоих сумм
    result = three + five  

    return int(result)

print(FizzBuzz(int(input())))