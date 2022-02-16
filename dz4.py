num = int(input("Введите целое положительное число "))
max_num = 0
while num > 0:
    num =num // 10
    if num % 10 > max_num:
        max_num = num % 10
    if num > 9:
        continue
    else:
        print(max_num)
        break