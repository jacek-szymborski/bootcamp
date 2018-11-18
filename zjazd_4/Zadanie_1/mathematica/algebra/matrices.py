def add_matrices(m1,m2):

    result = []
    for row_i in range(len(m1)):
        new_row = []
        for col_i in range(len(m1[row_i])):
            new_row.append(m1[row_i][col_i] + m2[row_i][col_i])
        result.append(new_row)
    return result

def sub_matrices(m1,m2):

    result = []
    for row_i in range(len(m1)):
        new_row = []
        for col_i in range(len(m1[row_i])):
            new_row.append(m1[row_i][col_i] - m2[row_i][col_i])
        result.append(new_row)
    return result


m1 = [
        [1, 2, 3],
        [7, 8, 9]
    ]

m2 = [
        [4, 5, 6],
        [10, 11, 12]
    ]


result = add_matrices(m1,m2)
print(result)
result_sub = sub_matrices(m1,m2)
print(result_sub)