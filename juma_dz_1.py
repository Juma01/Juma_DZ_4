# 1. Реализовать скрипт,
# в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)  # Выработка в часах
    salary = float(salary)  # Ставка у.е в час
    bonus = float(bonus)  # Премия
    res = time * salary + bonus
    print(f"\n\tЗаработная плата сотрудника {res}")
except ValueError:
    print("ValueError: not enough values to unpack ")
    print("\tВведите цифры")
