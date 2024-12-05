from re import RegexFlag, compile


regex = compile(r"mul\((\d{1,3}),(\d{1,3})\)", flags=RegexFlag.MULTILINE)


with open("input.txt") as f:
    input_str = f.read()


summ = 0
match_iter = regex.finditer(input_str)
for match in match_iter:
    a, b = map(int, match.groups())
    summ += a * b


print(summ)
