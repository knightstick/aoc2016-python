from itertools import batched

from aoc2016_python.utils import load_day

test_input = """
  5  10  25  
"""


def main():
    data = load_day(3)

    print(run(data))
    print(run_two(data))


def run(input: str) -> str:
    triples = [sorted(map(int, line.split())) for line in input.strip().splitlines()]
    triangles = [(x, y, z) for x, y, z in triples if x + y > z]

    return str(len(triangles))


def run_two(input: str) -> str:
    lines = [tuple(map(int, line.split())) for line in input.strip().splitlines()]
    in_threes = batched(lines, n=3)
    triangles = [sorted(list(row)) for three in in_threes for row in zip(*three)]
    result = [(x, y, z) for x, y, z in triangles if x + y > z]

    return str(len(result))


if __name__ == "__main__":
    main()
