import numpy as np

A = np.array([
     [3, 4, 5],
     [0, 78, 6],
     [6, 34, 2]
])

C = np.zeros(len(A), len(A), dtype='float64')

    # Заполнение матрицы алгебраических дополнений
    # Цикл 1
    for i in range(len(C)):
        # Вложенный цикл 1
        for j in range(len(C)):
            # Расчёт дополнительного минора
            M = np.delete(A, i, 0)
            M = np.delete(A, j, 1)
            m = opr(M)

            # Заполнений i, j-го элемента матрицы алгебраических дополнений
            C[i, j] = np.power(-1, i+j) * m