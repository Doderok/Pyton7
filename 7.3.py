def power(a, n):
    if n % 2 == 0:
        return int(a**(n/2)*a**(n/2))
    elif n == 0:
        return 1
    else:
        return int(a**(n-1)*a)
a = int(input("Введите число: "))
n = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(a, n))