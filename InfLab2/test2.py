import numpy as np

# Поиск определителя
def opr(A):
    # Глубокое копирование исходной матрицы
    C = np.copy(A)
    C = C.astype('float64')

    #  Коэффициент, стоящий перед матрицей
    K = 1

    # Цикл 1
    for j in range(len(C)-1):
        # Устранение нулей на главной диагонали
        i = j + 1
        # Вложенный цикл 1
        while C[j, j] == 0:
            C[j:j+1] += C[i:i+1]
            print(i)
            print(j)
            print(C)
            i += 1
            print(i)
            print()
        
        # Вынос элемента на главной диагонали за определитель
        K *= C[j, j]

        # Формирование единицы на главной диагонали
        C[j:j+1] = C[j:j+1]*(1/C[j, j])

        # Обнуление элементов под главной диагональю
        # Вложенный цикл 2
        for i in range(j+1, len(C)):
            C[i:i+1] += -(C[j:j+1])*C[i, j]
        
    # Элемент в правом нижнем углу является определителем
    return K*C[len(C)-1, len(C)-1]

# Поиск обратной матрицы
def obr(A):
    # Задание матрицы алгебраических дополнений
    C = np.zeros((len(A), len(A)), dtype='float64')

    # Заполнение матрицы алгебраических дополнений
    # Цикл 1
    for i in range(len(C)):
        # Вложенный цикл 1
        for j in range(len(C)):
            # Расчёт дополнительного минора
            M = np.delete(A, i, 0)
            M = np.delete(M, j, 1)
            m = opr(M)

            # Заполнений i, j-го элемента матрицы алгебраических дополнений
            C[i, j] = np.power(-1, i+j) * m

    return (1/opr(A))*np.transpose(C)

A = np.array([
    [0, 1, 0, 0, -1],
    [0, 0, -1, 1, 0],
    [0, -34, 0, 4, 0],
    [0, 0, 3, 0, 8],
    [6, 0, 3, 4, 0]
])
print(opr(A))