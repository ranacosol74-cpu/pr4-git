LIMIT = 15


def read_order():
    while True:
        answer = input("Порядок матрицы n: ").strip()
        if not answer.isdigit():
            print("  Нужно целое положительное число.")
        elif not 1 <= int(answer) <= LIMIT:
            print(f"  Порядок должен быть от 1 до {LIMIT}.")
        else:
            return int(answer)


def read_row(number, size):
    while True:
        items = input(f"Строка {number}: ").replace(",", ".").split()
        if len(items) != size:
            print(f"  В строке должно быть {size} чисел, введено {len(items)}.")
            continue
        try:
            return [float(item) for item in items]
        except ValueError:
            print("  В строке есть значение, которое не является числом.")


def read_matrix(n):
    print(f"Введите {n} строк по {n} чисел через пробел.")
    return [read_row(i + 1, n) for i in range(n)]


def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def show(title, matrix):
    print(title)
    for row in matrix:
        print("".join(f"{value:8.2f}" for value in row))


def main():
    n = read_order()
    matrix = read_matrix(n)
    show("Исходная матрица:", matrix)
    show("Транспонированная матрица:", transpose(matrix))


if __name__ == "__main__":
    main()
