profit = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Рентабельность фирмы составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit - costs / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")