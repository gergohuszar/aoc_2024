from itertools import product


def solution(input: str) -> int:
    input_list: list[str] = input.splitlines()

    results_and_elements = [
        (item.split(":")[0], item.split(":")[1].strip().split()) for item in input_list
    ]

    good_results = []

    for result, elements in results_and_elements:
        operators_product = list(product("*+", repeat=len(elements) - 1))
        i_res = int(result)

        for operators in operators_product:
            calc_res = 0

            for i in range(len(operators)):
                if calc_res == 0:
                    calc_res = eval(elements[i] + operators[i] + elements[i + 1])
                else:
                    calc_res = eval(elements[i + 1] + operators[i] + str(calc_res))

            if calc_res == i_res:
                good_results.append(i_res)
                break

    return sum(good_results)


with open("input.txt") as f:
    input_str = f.read()
    print(solution(input_str))
