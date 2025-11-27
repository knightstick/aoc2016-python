from typing import Any, Counter

from aoc2016_python.utils import load_day_lines


test_input = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"""


def main():
    data = load_day_lines(6)

    print(part_one(data))
    print(part_two(data))


def part_one(data: list[str]):
    transposed = list(zip(*data))
    chars = [
        char for row in transposed for [(char, _)] in [Counter(row).most_common(1)]
    ]

    return "".join(chars)


def part_two(data: list[str]):
    transposed = list(zip(*data))
    chars = [char for row in transposed for [(char, _)] in [least_common(row)]]

    return "".join(chars)


def least_common(row: tuple[str]) -> list[tuple[str, int]]:
    return sorted(Counter(row).items(), key=lambda elem: (elem[1], elem[0]))[:1]


if __name__ == "__main__":
    main()
