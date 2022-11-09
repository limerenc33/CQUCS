# -*- coding: utf-8 -*-#
import numpy as np
matrix_8_6 = []
for index_height in range(1, 9):
    temp_line = []
    for index_width in range(1, 7):
        temp_line.append(index_height + index_width)
    matrix_8_6.append(temp_line)
matrix_8_6 = np.asarray(matrix_8_6, dtype=np.uint8)
print(matrix_8_6)