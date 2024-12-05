from numpy import array, fliplr


with open("input.txt") as f:
    input_str = f.read()


test_res = 9

test_input = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""


searched = ["MAS", "SAM"]
matrix = array([list(row) for row in input_str.split("\n")])

count = 0
for row_i in range(matrix.shape[0]):
    for col_i in range(matrix.shape[1]):
        submatrix = matrix[row_i : row_i + 3, col_i : col_i + 3]

        diagonal_str = "".join(submatrix.diagonal())
        other_diagonal_str = "".join(fliplr(submatrix).diagonal())

        if diagonal_str in searched and other_diagonal_str in searched:
            count += 1


print(count)
