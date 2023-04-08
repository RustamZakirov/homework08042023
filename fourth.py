# Напишите программу, которая на вход принимает число (N), 
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

a = int (input("Введите число: "))
if a == 0: print("нет чисел")
elif a > 0:
    if a % 2 == 0:
        while (a > 0):
            print(f"{a}\t ", end="")
            a -= 2
    elif a % 2 == 1:
        a = a - 1
        while (a > 0):
            print(f"{a}\t ", end="")
            a -= 2
elif a < 0:
    if a % 2 == 0:
        while (a < 0):
            print(f"{a}\t ", end="")
            a += 2
    elif a % 2 == 1:
        a = a + 1
        while (a < 0):
            print(f"{a}\t ", end="")
            a += 2
        