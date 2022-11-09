# -*- coding: utf-8 -*-#
import numpy as np
matrix_8_6 = []
for index_height in range(1, 9):
    temp_line = []
    for index_width in range(1, 7):
        temp_line.append(index_height + index_width)
    matrix_8_6.append(temp_line)
matrix_8_6 = np.asarray(matrix_8_6, dtype=np.uint8)

matrix_6_12 = np.random.randint(20, size=(6, 12))

matrix_8_12 = np.dot(matrix_8_6, matrix_6_12)
print(matrix_8_6)
print(matrix_6_12)
print(matrix_8_12)

# 自己实现
def matrix_dot(matrix_a, matrix_b):
    a_col = matrix_a.shape[1]
    b_row = matrix_b.shape[0]
    print(a_col, b_row)

    result_matrix = np.zeros(shape=(matrix_a.shape[0], matrix_b.shape[1]))
    if not a_col == b_row:
        print("两个矩阵的维度不匹配")
        return -1
    else:
        for index_i in range(matrix_a.shape[0]):
            # matrix_a的第i行数据
            matrix_a_data = matrix_a[index_i]
            for index_j in range(matrix_b.shape[1]):
                matrix_b_data = matrix_b[:, index_j]
                c_i_j = matrix_a_data * matrix_b_data
                c_i_j = np.sum(c_i_j)
                result_matrix[index_i][index_j] = c_i_j
    return result_matrix

result = matrix_dot(matrix_8_6, matrix_6_12)
print(result)