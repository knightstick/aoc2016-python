from aoc2016_python.utils import load_day_lines


test_input = """
rect 3x2
rotate col x=1 by 1
rotate row y=0 by 4
rotate col x=1 by 1
"""

type Instruction = str
type Grid = list[list[str]]

WIDTH = 50
HEIGHT = 6


def main():
    instructions = load_day_lines(8)
    grid: list[list[str]] = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for instruction in instructions:
        run(grid, instruction)

    print(part_one(grid))
    print(part_two(grid))


def part_one(grid):
    return sum(1 for line in grid for char in line if char == "#")


def part_two(grid):
    return join_grid(grid)


def run(grid: list[list[str]], instruction: Instruction):
    match instruction.split(" "):
        case ["rect", dims]:
            [wide, tall] = dims.split("x")
            return rect(grid, int(wide), int(tall))
        case ["rotate", "column" | "col", xeq, "by", n] if int(n) > 0:
            [_, x] = xeq.split("=")
            return rotate_col(grid, int(x), int(n))
        case ["rotate", "row", yeq, "by", n]:
            [_, y] = yeq.split("=")
            return rotate_row(grid, int(y), int(n))
        case _:
            raise ValueError(f"Unhandled instruction: {instruction}")


def rect(grid: Grid, wide: int, tall: int):
    for row in range(tall):
        for col in range(wide):
            grid[row][col] = "#"


def rotate_row(grid: Grid, row: int, n: int):
    row_copy = list(char for char in grid[row])
    for i in range(WIDTH):
        grid[row][i] = row_copy[(i - n) % WIDTH]


def rotate_col(grid, col, n):
    col_copy = list(grid[i][col] for i in range(HEIGHT))
    for i in range(HEIGHT):
        grid[i][col] = col_copy[(i - n) % HEIGHT]


def transpose(grid: Grid) -> Grid:
    return [list(col) for col in zip(*grid)]


def join_grid(grid: Grid) -> str:
    return "\n".join(["".join(row) for row in grid])


def print_grid(grid: Grid):
    print(join_grid(grid))


if __name__ == "__main__":
    main()
