# Task 1

# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом.
# Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, 
# чтобы все монетки лежали одной и той же стороной вверх.
# Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, 
# если i-я монетка лежит гербом вверх, и равно 1, 
# если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - минимальное количество монеток, 
# которые нужно перевернуть.

# Пример использования На входе:
# coins = [0, 1, 0, 1, 1, 0]
# На выходе:
# 3

# main/ver
# coins = [0, 1, 0, 1, 1, 0]
# orel, reshka = 0, 0
# for i in coins:
#     if i == 0:
#         orel += 1
#     elif i == 1: 
#         reshka += 1       
# if orel <= reshka:
#     print(orel)
# else:
#     print(reshka)

# версия автотеста
# count_zero = 0
# count_one = 0

# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1

# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)