# Напишите программу, которая по заданному номеру 
# четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

a = int (input("Введите номер четверти: "))
if a < 1: print("Введите число более 0")
elif a > 4: print("введите число менее 5")
elif a == 1: print("X > 0, Y > 0")
elif a == 2: print("X < 0, Y > 0")
elif a == 3: print("X < 0, Y < 0")
elif a == 4: print("X > 0, Y < 0")