def FizzBuzz(N):
    three = ((2*3 + 3*(N//3-1))/2)*(N//3)       # formula of the sum: ((2*a1 + difference*(number_of_elements-1))/2)*number_of_elements  
    five = ((2*5 + 5*(N//5-1))/2)*(N//5)        # N is parsed for each set through whole division since every a-th number of the 1--N progression is divisible by a
    fifteen = ((2*15 + 15*(N//15-1))/2)*(N//15)

    three -= fifteen
    five -= fifteen
    result = three + five

    return int(result)

print(FizzBuzz(int(input())))