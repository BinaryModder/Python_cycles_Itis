from math import pow


def main():
    x_start = float(input("Введите x начальное: "))
    x_end = float(input("Введите x конечное: "))
    dx = float(input("Введите положительный шаг dx: "))

    x = x_start
    print("X  |  Y")
    while x <= x_end:
        if x < -4:
            y = float(-2)
        elif x <= 0:
            y = 0.25 * x
        elif x <= 2:
            y = pow(x, 2)
        else:
            y = 5 - 0.5 * x

        print(f"{x} | {y}")
        x += dx


if __name__ == "__main__":
    main()
