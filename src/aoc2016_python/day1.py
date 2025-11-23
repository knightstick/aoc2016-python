from collections import namedtuple
from functools import reduce
from typing import Iterator, Literal

from aoc2016_python.utils import load_day

Right = namedtuple("Right", ["steps"])
Left = namedtuple("Left", ["steps"])

Direction = Right | Left

Location = namedtuple("Location", ["North", "East"])

Heading = Literal["N", "E", "S", "W"]

State = namedtuple("State", ["location", "heading"])


def main():
    data = load_day(1)
    print(run_part_one(data))
    print(run_part_two(data))


def run_part_one(input: str) -> str:
    location, _ = move(_parse_directions(input))

    return str(sum(map(abs, location)))


def run_part_two(input: str) -> str:
    first_revisted = next(move_with_revisit(_parse_directions(input)))

    return str(sum(map(abs, first_revisted)))


def _parse_directions(input: str) -> list[Direction]:
    return [_parse_one(s.strip()) for s in input.split(", ")]


def _parse_one(dir: str) -> Right | Left:
    match list(dir):
        case ["R", *numbers]:
            return Right(int("".join(numbers)))
        case ["L", *numbers]:
            return Left(int("".join(numbers)))
        case _:
            raise RuntimeError(f"Malformed Direction: {dir}")


def move(directions: list[Direction]) -> State:
    state = State(Location(0, 0), "N")
    return reduce(_move_one, directions, state)


def _move_one(state: State, direction: Direction) -> State:
    (north, east), _ = state
    new_heading = turn(state, direction)
    (dn, de) = direction_vector(new_heading)
    i = steps(direction)

    return State(Location(north + dn * i, east + de * i), new_heading)


def move_with_revisit(directions: list[Direction]) -> Iterator[Location]:
    state = State(Location(0, 0), "N")

    visited = set()
    visited.add(state.location)

    for direction in directions:
        steps, state = _moves(state, direction)
        for step in steps:
            if step in visited:
                yield step
            else:
                visited.add(step)


def _moves(state: State, direction: Direction) -> tuple[list[Location], State]:
    (north, east), _ = state

    new_heading = turn(state, direction)
    (dn, de) = direction_vector(new_heading)

    path = [
        Location(north + dn * i, east + de * i) for i in range(1, steps(direction) + 1)
    ]

    return (path, State(path[-1], new_heading))


def steps(direction: Direction) -> int:
    match direction:
        case Right(steps):
            return steps
        case Left(steps):
            return steps


def turn(state: State, direction: Direction) -> Heading:
    _, heading = state

    match heading, direction:
        case "N", Right(_):
            return "E"
        case "E", Right(_):
            return "S"
        case "S", Right(_):
            return "W"
        case "W", Right(_):
            return "N"
        case "N", Left(_):
            return "W"
        case "E", Left(_):
            return "N"
        case "S", Left(_):
            return "E"
        case "W", Left(_):
            return "S"
        case _, _:
            raise RuntimeError(f"Unhandled turn: {heading, direction}")


def direction_vector(heading) -> tuple[int, int]:
    match heading:
        case "N":
            return (1, 0)
        case "E":
            return (0, 1)
        case "S":
            return (-1, 0)
        case "W":
            return (0, -1)
        case _:
            raise RuntimeError(f"Unhandled heading: {heading}")


if __name__ == "__main__":
    main()
