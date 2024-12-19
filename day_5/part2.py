import time


def is_rule_applicable(a: int, b: int, update: list[int]) -> bool:
    return a in update and b in update


def is_update_satisfy_rule(a: int, b: int, update: list[int]) -> bool:
    return update.index(a) < update.index(b)


def is_one_rule_not_satisfied(rules, update: list[int]) -> bool:
    for rule in rules:
        a, b = rule
        if not is_update_satisfy_rule(a, b, update):
            return True
    return False


def solution(input: str) -> int:
    collect_lists = time.time()
    input_list: list[str] = input.splitlines()

    last_ordering_rules_index = input_list.index("")

    ordering_rules = input_list[:last_ordering_rules_index]
    ordering_rules = [
        (int(a), int(b)) for rule in ordering_rules for a, b in [rule.split("|")]
    ]

    collected_page_numbers = []

    page_numbers_of_update = input_list[last_ordering_rules_index + 1 :]
    # measure runtime
    collect_lists_end = time.time()

    for update in page_numbers_of_update:
        a = update.split(",")
        update_int: list[int] = list(map(int, a))

        wrong_order = False

        applicable_rules = [
            rule
            for rule in ordering_rules
            if is_rule_applicable(rule[0], rule[1], update_int)
        ]
        wrong_order = False
        rule_not_satisfied = True

        while rule_not_satisfied:
            for rule in applicable_rules:
                a, b = rule

                x_index = update_int.index(a)
                y_index = update_int.index(b)

                if x_index > y_index:
                    wrong_order = True
                    popped = update_int.pop(x_index)
                    update_int.insert(y_index, popped)

            rule_not_satisfied = is_one_rule_not_satisfied(applicable_rules, update_int)

        if wrong_order:
            collected_page_numbers.append(update_int[len(update_int) // 2])
    end = time.time()

    print("Time: ", collect_lists_end-collect_lists)

    return sum(collected_page_numbers)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
        print(solution(input_str))
