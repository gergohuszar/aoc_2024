from re import RegexFlag, compile


regex = compile(
    r"(?P<mul>mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\))|(?P<enable>do\(\))|(?P<disable>don't\(\))",
    flags=RegexFlag.MULTILINE,
)


with open("input.txt") as f:
    input_str = f.read()


summ = 0
match_iter = regex.finditer(input_str)

enable = True

for m in match_iter:
    if m.group("enable"):
        enable = True
    elif m.group("disable"):
        enable = False
    else:
        if enable:
            a = int(m.group("a"))
            b = int(m.group("b"))

            summ += a * b


print(summ)
