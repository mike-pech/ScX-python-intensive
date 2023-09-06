# numbers: list = [
#     1, 2, 3, 4, 5, 6, 7, 8, 9
# ]

# for n in numbers:
#     if n % 7 == 0:
#         print(f"Число {n} делится на 7")
#     elif n % 5 == 0:
#         print(f"Число {n} делится на 5")
#     else:
#         print(f"Число {n} не делится ни на 5, ни на 7")

# word: str = input("Введите слово: \n")
# vovel: str = "aeiouy"
# vovel_count =  0

# for character in word:
#     if character in vovel:
#         vovel_count += 1
# print(vovel_count)

# def FizzBuzz(n):
#     sum_3_5 = 0
#     sum_3 = 0
#     sum_5 = 0
#     for i in range(1, n+1):
#         if n % 3 == 0 and n % 5 == 0:
#             sum_3_5 += i
#         elif n % 3 == 0:
#             sum_3 += i
#         elif n % 5 == 0:
#             sum_5 += i
#     return sum_5, sum_3, sum_3_5

# print(*FizzBuzz(int(input())))

# --------------    QUESTIONABLE CODE DECISIONS. DO NOT TRY THIS AT HOME!    ----------------

# i = 0
# # 
# # while i <= 10:
# #     print(i)
# #     i += 1
# # else:
# #     print("A'ight, stop!")
# # 
# for i in range(11):
#     print(i)
# else:
#     print("A'ight, stop!")