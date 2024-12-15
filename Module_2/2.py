import random
num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = int(input("Введите число из первой вставки: "))
result = ''
for i in range(1, n):
    for j in range(1, n):
        if i >= j:
            continue
        else:
            k = n % (i + j)
            if k == 0:
                result = result + str(i) + str(j)
print("Пароль (вторая вставка): ", result)
















