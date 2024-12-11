def is_rule_applicable(a: int, b: int, update: list[int]) -> bool:
    return a in update and b in update


def is_update_satisfy_rule(a: int, b: int, update: list[int]) -> bool:
    return update.index(a) < update.index(b)


def solution(input: str) -> int:
    input_list: list[str] = input.splitlines()

    last_ordering_rules_index = input_list.index("")

    ordering_rules = input_list[:last_ordering_rules_index]
    ordering_rules = [
        (int(a), int(b)) for rule in ordering_rules for a, b in [rule.split("|")]
    ]

    collected_page_numbers = []

    page_numbers_of_update = input_list[last_ordering_rules_index + 1 :]

    for update in page_numbers_of_update:
        a = update.split(",")
        update_int: list[int] = list(map(int, a))

        for rule in ordering_rules:
            x, y = rule

            if is_rule_applicable(x, y, update_int) and not is_update_satisfy_rule(
                x, y, update_int
            ):
                break
        else:
            collected_page_numbers.append(update_int[len(update_int) // 2])

    return sum(collected_page_numbers)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
        print(solution(input_str))
