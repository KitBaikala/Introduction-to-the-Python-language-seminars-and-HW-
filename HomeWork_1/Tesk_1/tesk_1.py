# Tesk_1
# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.
# (проверяется автотестом)
# Пример:

# n = 123 -> res = 6 (1 + 2 + 3)

# n = 100 -> res = 1 (1 + 0 + 0)

# Мое решение
# n = 123
# res = n % 10 + (n // 10) % 10 + n // 100
# print(res)


# решение в автотесте
# n1 = n // 100 # Нахождение первой цифры числа
# n2 = (n % 100) // 10 # Нахождение второй цифры числа
# n3 = n % 10 # Нахождение третьей цифры числа
# res = n1 + n2 + n3
