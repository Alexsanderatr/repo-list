a = int(input("Введите количество км ппробежки  первого дня  "))
b = int(input(" желаемый результат в км "))
days = 1
while a < b:
        a = a + 0.1 * a
        days += 1
print(f"  {days} день")
