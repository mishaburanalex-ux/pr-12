"""
Практична робота 12 — покращена версія
Обчислення НСД та НСК (алгоритм Евкліда через %), обробка від'ємних і нульових значень,
підтримка запуску через аргументи командного рядка або інтерективно.
Виконав: Буран Михайло
"""
import argparse
import sys


def gcd(a: int, b: int) -> int:
    """Повертає найбільший спільний дільник (НСД) для цілих a та b.
    Алгоритм Евкліда через ділення. gcd(0,0) визначено як 0.
    """
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return 0
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Повертає найменше спільне кратне (НСК) для a та b.
    Якщо один з аргументів 0 — НСК = 0.
    """
    a_abs, b_abs = abs(a), abs(b)
    g = gcd(a_abs, b_abs)
    if g == 0:
        return 0
    return (a_abs // g) * b_abs  # без переповнення: спочатку ділимо


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Обчислення НСД та НСК (Практична робота 12)")
    parser.add_argument("A", nargs="?", type=int, help="Перше ціле число A")
    parser.add_argument("B", nargs="?", type=int, help="Друге ціле число B")
    return parser.parse_args(argv[1:])


def interactive_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Будь ласка, введіть коректне ціле число.")


def main(argv=None):
    if argv is None:
        argv = sys.argv
    args = parse_args(argv)

    if args.A is None or args.B is None:
        print("Введіть два числа (можна також передати як аргументи командного рядка).")
        A = interactive_input("Введіть перше число A: ")
        B = interactive_input("Введіть друге число B: ")
    else:
        A, B = args.A, args.B

    print("\nПрактична робота 12. Обчислення НСД та НСК (покращена версія)")
    print("=" * 50)
    print(f"Вхідні числа: A = {A}, B = {B}")

    g = gcd(A, B)
    print(f"\nНСД({A}, {B}) = {g}")

    l = lcm(A, B)
    print(f"НСК({A}, {B}) = {l}")

    # Розв'язання задач з практичної (приклади)
    print("\n" + "=" * 50)
    print("ПРИКЛАДИ")
    print("=" * 50)

    # Задача 1: 60 цукерок і 45 яблук
    candies, apples = 60, 45
    g1 = gcd(candies, apples)
    print(f"\nЗадача 1: {candies} цукерок і {apples} яблук → НСД = {g1}")
    print(f"Можна зібрати {g1} подарунків (по {candies//g1} цукерок і {apples//g1} яблука)")

    # Задача 2: теплоходи 10 і 18 діб
    ship1, ship2 = 10, 18
    l_ships = lcm(ship1, ship2)
    print(f"\nЗадача 2: періоди {ship1} і {ship2} діб → зустрінуться через {l_ships} діб")

    print("\n" + "=" * 50)
    print("ВИСНОВОК:")
    print("Алгоритм Евкліда через ділення (%) працює набагато швидше за віднімання,")
    print("особливо для великих чисел.")
    print("=" * 50)


if __name__ == "__main__":
    main()
