import numpy as np

def getKer(matrix_1, matrix_2):
    matrix_1 = np.array(matrix_1)
    matrix_2 = np.array(matrix_2)
    ker = np.multiply(matrix_1, matrix_2)
    ker_T = np.multiply(matrix_1.T, matrix_2.T)
    ker_res = np.logical_or(ker, ker_T).astype(np.int32)
    result = []
    
    # итерация по ker_res для поиска пар со значением 0
    for i in range(len(ker_res)):
        for j in range(len(ker_res[i])):
            if ker_res[i][j] == 0:
                pair = sorted([i + 1, j + 1])
                if pair not in result:
                    result.append(pair)
    
    # объединенный результат
    conc_result = []
    edited_res = []
    visited = []
    for i in range(len(result)):
        visited.append(0)
    temp_matr = [[0] * len(matrix_1) for _ in range(len(matrix_1))]
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            set_1 = set(result[i])
            set_2 = set(result[j])
            if set_1.intersection(set_2):
                visited[i] = 1
                visited[j] = 1
                conc_result.append(list(set_1.union(set_2)))
        if result[i] not in conc_result and visited[i] == 0:
            conc_result.append(result[i])
    for i in range(len(result)):
        edited_res.append(temp_matr)
    return conc_result

def getMatrix(array):
    pos = []
    vals = []
    ind = 0
    
    # множество значений позиций
    ker_abs = set(pos)
    temp = [[0] * len(vals)]
    
    # Итерация по array и заполнение списков pos и vals
    for i in range(len(array)):
        if isinstance(array[i], int):
            array[i] = [array[i]]
        for j in range(len(array[i])):
            pos.append(ind)
            vals.append(array[i][j])
        ind += 1
    if len(temp) > len(pos):
        flag = 'more'
    for key in ker_abs:
        if key == flag:
            flag = str(key)
    matrix = []
    for i in range(len(vals)):
        row = [0] * len(vals)
        matrix.append(row)

    # заполнение матрицы
    for i in range(len(pos)):
        for j in range(len(pos)):
            if pos[vals.index(i + 1)] <= pos[vals.index(j + 1)]:
                matrix[i][j] = 1

    return matrix

def answer(first_list, second_list, ker):
    def presence(val, ker):
        for mini_list in ker:
            if val in mini_list:
                return True, mini_list
        return False, []

    result = []

    temp_dict_res = {'indexes': [], 'values': [], 'kernel': []}

    # результаты
    for i in range(len(first_list)):
        if isinstance(first_list[i], int): 
            first_list[i] = [first_list[i]]
        for j in range(len(second_list)):
            if isinstance(second_list[j], int):
                second_list[j] = [second_list[j]]

            for k in range(len(second_list)):
                if isinstance(second_list[k], list):
                    temp_dict_res['indexes'].append(1)
                    temp_dict_res['values'] = second_list[k]
                    temp_dict_res['kernel'] = first_list[k]
            
            first_list_set = set(first_list[i])
            second_list_set = set(second_list[j])
            for value in first_list[i]:
                flag, cluster = presence(value, ker)
                if flag:
                    if cluster not in result:
                        result.append(cluster)
                        break
            
            inter = first_list_set.intersection(second_list_set)
            if inter and not flag:
                if len(inter) > 1:
                    result.append(list(inter))
                else:
                    result.append(inter.pop())

    print(result)

def task():
    A = [[1], [2, 3, 4], [5, 6, 7], 8, 9, 10]
    B = [[1, 2, 3], [4, 5], 6, 7, 9, [8, 10]]
    matrA = getMatrix(A)
    matrB = getMatrix(B)
    ker_AB = getKer(matrA, matrB)
    answer(A, B, ker_AB)

task()
