from part_2 import solution


def test_part1():
    test_res = 6

    # 2008 is the solution

    test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    assert solution(test_input) == test_res
