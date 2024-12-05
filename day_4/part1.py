from numpy import array, fliplr


with open("input.txt") as f:
    input_str = f.read()


test_res = 18

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


matrix_dimension = 140

searched = ["XMAS", "SAMX"]
matrix = array([list(row) for row in input_str.split("\n")])
print(matrix)


verticals = ["".join(matrix[:, i]) for i in range(matrix.shape[1])]
horizontals = ["".join(matrix[i, :]) for i in range(matrix.shape[0])]
diagonals_r_u = ["".join(matrix.diagonal(i)) for i in range(0, matrix_dimension)]
diagonals_r_d = ["".join(matrix.diagonal(i)) for i in range(-1, -matrix_dimension, -1)]
diagonals_l_u = [
    "".join(fliplr(matrix).diagonal(i)) for i in range(0, matrix_dimension)
]
diagonals_l_d = [
    "".join(fliplr(matrix).diagonal(i)) for i in range(-1, -matrix_dimension, -1)
]


inputs = [
    verticals,
    horizontals,
    diagonals_r_u,
    diagonals_r_d,
    diagonals_l_u,
    diagonals_l_d,
]

print(inputs)

result = 0


def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


def find_word_in_list_of_str(inputlist: list, searched: list):
    res = 0

    for element in inputlist:
        for word in searched:
            res += occurrences(element, word)
    return res


for input in inputs:
    result += find_word_in_list_of_str(input, searched)


print(result)

# assert result == test_res, f"{result} != {test_res}"
