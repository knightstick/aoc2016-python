from typing import Iterator, cast, Literal, Callable
from aoc2016_python.utils import load_day

test_1 = """
ULL
RRDDD
LURDL
UUUUD
"""

KeypadNumber = Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D"]

VALID_INSTRUCTIONS = {"U", "R", "D", "L"}
Instruction = Literal["U", "R", "D", "L"]

KeypadMove = Callable[[KeypadNumber, Instruction], KeypadNumber]


def main():
    data = load_day(2)

    print(run(data))
    print(run(data, _keypad_move_thirteen))


def run(input: str, keypad_move: KeypadMove | None = None) -> str:
    if keypad_move is None:
        keypad_move = _keypad_move_nine

    lines: list[list[Instruction]] = [
        [parse_instruction(c) for c in line] for line in input.split()
    ]

    return "".join(keypad_numbers(lines, keypad_move))


def parse_instruction(char: str) -> Instruction:
    if char not in VALID_INSTRUCTIONS:
        raise ValueError(f"Invalid instruction: {char}")
    return cast(Instruction, char)


def keypad_numbers(
    instructions: list[list[Instruction]], keypad_move: KeypadMove
) -> Iterator[str]:
    position = "5"

    for instruction in instructions:
        position = _next_number_to_press(position, instruction, keypad_move)
        yield position


def _next_number_to_press(
    pos: KeypadNumber, instructions: list[Instruction], keypad_move
) -> KeypadNumber:
    for step in instructions:
        pos = keypad_move(pos, step)

    return pos


def _keypad_move_nine(pos: KeypadNumber, instruction: Instruction) -> KeypadNumber:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    match instruction, pos:
        case "U", "1":
            return "1"
        case "U", "2":
            return "2"
        case "U", "3":
            return "3"

        case "U", "4":
            return "1"
        case "U", "5":
            return "2"
        case "U", "6":
            return "3"

        case "U", "7":
            return "4"
        case "U", "8":
            return "5"
        case "U", "9":
            return "6"

        case "R", "1":
            return "2"
        case "R", "2":
            return "3"
        case "R", "3":
            return "3"

        case "R", "4":
            return "5"
        case "R", "5":
            return "6"
        case "R", "6":
            return "6"

        case "R", "7":
            return "8"
        case "R", "8":
            return "9"
        case "R", "9":
            return "9"

        case "D", "1":
            return "4"
        case "D", "2":
            return "5"
        case "D", "3":
            return "6"

        case "D", "4":
            return "7"
        case "D", "5":
            return "8"
        case "D", "6":
            return "9"

        case "D", "7":
            return "7"
        case "D", "8":
            return "8"
        case "D", "9":
            return "9"

        case "L", "1":
            return "1"
        case "L", "2":
            return "1"
        case "L", "3":
            return "2"

        case "L", "4":
            return "4"
        case "L", "5":
            return "4"
        case "L", "6":
            return "5"

        case "L", "7":
            return "7"
        case "L", "8":
            return "7"
        case "L", "9":
            return "8"

        case _, _:
            raise ValueError(f"Unsupported move: {instruction, pos}")


def _keypad_move_thirteen(pos: KeypadNumber, instruction: Instruction) -> KeypadNumber:
    #     1
    #   2 3 4
    # 5 6 7 8 9
    #   A B C
    #     D

    match instruction, pos:
        case "U", "1":
            return "1"
        case "U", "2":
            return "2"
        case "U", "3":
            return "1"
        case "U", "4":
            return "4"
        case "U", "5":
            return "5"
        case "U", "6":
            return "2"
        case "U", "7":
            return "3"
        case "U", "8":
            return "4"
        case "U", "9":
            return "9"
        case "U", "A":
            return "6"
        case "U", "B":
            return "7"
        case "U", "C":
            return "8"
        case "U", "D":
            return "B"

        case "R", "1":
            return "1"
        case "R", "2":
            return "3"
        case "R", "3":
            return "4"
        case "R", "4":
            return "4"
        case "R", "5":
            return "6"
        case "R", "6":
            return "7"
        case "R", "7":
            return "8"
        case "R", "8":
            return "9"
        case "R", "9":
            return "9"
        case "R", "A":
            return "B"
        case "R", "B":
            return "C"
        case "R", "C":
            return "C"
        case "R", "D":
            return "D"

        case "D", "1":
            return "3"
        case "D", "2":
            return "6"
        case "D", "3":
            return "7"
        case "D", "4":
            return "8"
        case "D", "5":
            return "5"
        case "D", "6":
            return "A"
        case "D", "7":
            return "B"
        case "D", "8":
            return "C"
        case "D", "9":
            return "9"
        case "D", "A":
            return "A"
        case "D", "B":
            return "D"
        case "D", "C":
            return "C"
        case "D", "D":
            return "D"

        case "L", "1":
            return "1"
        case "L", "2":
            return "2"
        case "L", "3":
            return "2"
        case "L", "4":
            return "3"
        case "L", "5":
            return "5"
        case "L", "6":
            return "5"
        case "L", "7":
            return "6"
        case "L", "8":
            return "7"
        case "L", "9":
            return "8"
        case "L", "A":
            return "A"
        case "L", "B":
            return "A"
        case "L", "C":
            return "B"
        case "L", "D":
            return "D"


if __name__ == "__main__":
    main()
